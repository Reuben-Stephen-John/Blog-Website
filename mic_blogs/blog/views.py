from django.shortcuts import render
from django.db.models import Q
from .models import BlogPage

def search_view(request):
    query = request.GET.get('q', '')
    if query:
        # Perform the search using Q objects to search multiple fields
        results = BlogPage.objects.filter(
            Q(title__icontains=query)|Q(intro__icontains=query) | Q(body__icontains=query)
        ).live().order_by('-first_published_at')
        blogs=[]
    else:
        results = []
    blogs = BlogPage.objects.all().order_by('-date')[:15]

    return render(request, 'blog/search_results.html', {'results': results, 'query': query,'blogs':blogs})

def home_view(request):
    latest_blog = BlogPage.objects.all().order_by('-date')[:1].first()
    blogs = BlogPage.objects.all().order_by('-date')[1:16]

    return render(request, 'blog/home_view.html', {'latest_blog': latest_blog, 'blogs': blogs})

def about_view(request):
    return render(request, 'blog/about.html')

def contact_view(request):
    return render(request, 'blog/contact.html')
