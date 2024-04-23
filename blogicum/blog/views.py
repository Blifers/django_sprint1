from django.shortcuts import render


def index(request):
    template = 'index.html'
    return render(request, template)


def post_detail(request):
    template = 'detail.html'
    return render(request, template)


def category_posts(request):
    template = 'category.html'
    return render(request, template)
