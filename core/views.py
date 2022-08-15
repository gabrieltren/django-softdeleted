from django.shortcuts import render

# Create your views here.
from .models import Movimentacao
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def mov(request):
    mov = Movimentacao.objects.all()
    pagina = request.GET.get('page', 1)
    paginacao = Paginator(mov, 1)
    
    try:
        movs = paginacao.page(pagina)
    except PageNotAnInteger:
        movs = paginacao.page(1)
    except EmptyPage:
        movs = paginacao.page(paginacao.num_pages)
        
    context = {'movs': movs}
    print(dir(movs.paginator))
    return render(request, 'mov.html', context)