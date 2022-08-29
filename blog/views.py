from django.shortcuts import render
from django.http import JsonResponse 

# Create your views here.

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post




    
def posts(request, *args, **kwargs):
    post = Post.objects.all()
    page = request.GET.get('page', 1)
    is_paginated = request.GET.get('is_paginator', True)
    paginator = Paginator(post, 5)
    context = dict()
    
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    print(dir(posts.paginator))
    
    context = {
        'posts': posts,
        "is_paginated": is_paginated
    }
    
    # return render(request, 'posts.html', context)


