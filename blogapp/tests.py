from django.test import TestCase

# Create your tests here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from django.contrib import messages
from .forms import ContactForm
from django.core.paginator import Paginator
from .models import Category
# Create your views here.

def home(request):
    max_view_post = Blog.objects.latest('views')
    latest_post = Blog.objects.latest('id')
    entertainment_posts = Blog.objects.filter(category='Entertainment').order_by('-views')
    sports_posts = Blog.objects.filter(category='Sports').order_by('-views')
    recent_posts = Blog.objects.order_by('-id')
    popular_posts = Blog.objects.order_by('-views')
    # Paginator
    paginator = Paginator(recent_posts, 5)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    if page.has_previous():
        prev_page_url = '/?page='+str(page.previous_page_number())
    else:
        prev_page_url = ''
    if page.has_next():
        next_page_url = '/?page='+str(page.next_page_number())
    else:
        next_page_url = ''
    params = {'max_view_post':max_view_post, 'latest_post':latest_post, 'recent_posts':page.object_list, 'page':page, 
            'prev_page_url':prev_page_url, 'next_page_url':next_page_url, 'popular_posts':popular_posts, 
            'entertainment_posts':entertainment_posts, 'sports_posts':sports_posts}
    return render(request, 'blogapp/index.html', params)

def category(request):
    return render(request, 'blogapp/categories.html')

def about(request):
    return render(request, 'blogapp/about.html')

def contact(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            messages.info(request, "Message Has Been Sent Successfully. We will response you soon!!!")
            return redirect('/')
        else:
            messages.error(request, "Some error while filling the form.")
            return redirect('/contact')
    else:
        form = ContactForm()
        return render(request, 'blogapp/contact.html', {'form':form})

def fullpost(request, id):
    full_post = Blog.objects.get(id=id)
    full_post.views = full_post.views+1
    full_post.save()
    popular_posts = Blog.objects.order_by('-views')[:5]
    params = {'full_post':full_post, 'popular_posts':popular_posts}
    return render(request, 'blogapp/fullpost.html', params)

def trendingpost(request):
    trending_posts = Blog.objects.order_by('-views')[:10]
    params = {'trending_posts': trending_posts}
    return render(request, 'blogapp/trendingpost.html', params)

def searchpost(request):
    query = request.GET['query']
    if len(query)>20:
        messages.error(request, "Search Query shulob be less than 20 characters.")
        return render(request, 'blogapp/search.html')
    else:
        search_posts_title = Blog.objects.filter(title__icontains=query)
        search_posts_desc = Blog.objects.filter(description__icontains=query)
        search_posts_cat = Blog.objects.filter(category__icontains=query)
        search_posts = search_posts_title | search_posts_cat | search_posts_desc
        if len(search_posts)==0:
            messages.error(request, "Blog Not Found")
            return render(request, 'blogapp/search.html')
        else:
            params = {'search_posts':search_posts}
            return render(request, 'blogapp/search.html', params)


def technology(request):
    tech_posts = Blog.objects.filter(category='Technology').order_by('-id')
    popular_tech_posts = Blog.objects.filter(category='Technology').order_by('-views')[:2]
    params = {'tech_posts':tech_posts, 'popular_tech_posts':popular_tech_posts}
    return render(request, 'blogapp/technology.html', params)

def sports(request):
    sports_posts = Blog.objects.filter(category='Sports').order_by('-id')
    popular_sports_posts = Blog.objects.filter(category='Sports').order_by('-views')[:2]
    params = {'sports_posts':sports_posts, 'popular_sports_posts':popular_sports_posts}
    return render(request, 'blogapp/sports.html', params)

def news(request):
    news_posts = Blog.objects.filter(category='News').order_by('-id')
    popular_news_posts = Blog.objects.filter(category='News').order_by('-views')[:2]
    params = {'news_posts':news_posts, 'popular_news_posts':popular_news_posts}
    return render(request, 'blogapp/news.html', params)

def entertainment(request):
    entertain_posts = Blog.objects.filter(category='Entertainment').order_by('-id')
    popular_entertain_posts = Blog.objects.filter(category='Entertainment').order_by('-views')[:2]
    params = {'entertain_posts':entertain_posts, 'popular_entertain_posts':popular_entertain_posts}
    return render(request, 'blogapp/entertainment.html', params)

def politics(request):
    politics_posts = Blog.objects.filter(category='Politics').order_by('-id')
    popular_politics_posts = Blog.objects.filter(category='Politics').order_by('-views')[:2]
    params = {'politics_posts':politics_posts, 'popular_politics_posts':popular_politics_posts}
    return render(request, 'blogapp/politics.html', params)