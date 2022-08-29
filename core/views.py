from django.shortcuts import render

# Create your views here.
from .models import Movimentacao
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import MovimentacaoSerializer, MovimentacaoSerializer2

def mov(request):
    mov = Movimentacao.objects.all()
    pagina = request.GET.get('page', 1)
    paginacao = Paginator(mov, 5)
    
    try:
        movs = paginacao.page(pagina)
    except PageNotAnInteger:
        movs = paginacao.page(1)
    except EmptyPage:
        movs = paginacao.page(paginacao.num_pages)
        
    context = {'movs': mov}
    # print(dir(movs.paginator))
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)

    return render(request, 'movimentacao.html', context)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly,])
def mov2(request):
    mov = Movimentacao.objects.all()
    serializer = MovimentacaoSerializer2(mov, many=True)
    return Response(serializer.data)

class MovViewSet(viewsets.ModelViewSet):
    serializer_class = MovimentacaoSerializer
    queryset = Movimentacao.objects.all()
    
    
    def get_queryset(self):
        return self.queryset.filter(deleted_at=None)
    
    def get_serializer_class(self):
        serializer_map = {
            "list": MovimentacaoSerializer2,
            "retrieve": MovimentacaoSerializer2,
            "create": MovimentacaoSerializer,
            "update": MovimentacaoSerializer
        }
        return serializer_map.get(self.action, super().get_serializer_class())
    
    def list(self, request):
        queryset = self.get_queryset()
        # return Response(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)