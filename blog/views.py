# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect

from course.models import CourseCategory
from .models import *
from .forms import CommentForm
from userauths.models import Dashboard_User
from django.contrib.auth.models import User


def category_list(request):
    blogcategories = BlogCategory.objects.all()
    categories = CourseCategory.objects.all()
    user = request.user
    if request.user.is_authenticated:
        auser = User.objects.get(username=user)  
        dash_user = Dashboard_User.objects.get(user_id=auser.id)
        photo = dash_user.photo
        return render(request, 'blog.html', {'is_blog': True, 'blogcategories': blogcategories, 'categories': categories,'photo':photo})
    return render(request, 'blog.html', {'is_blog': True, 'blogcategories': blogcategories, 'categories': categories})

def post_list_by_category(request, category_id):
    category = get_object_or_404(BlogCategory, pk=category_id)
    posts = Post.objects.filter(category=category)
    categories = CourseCategory.objects.all()
    postCategories=BlogCategory.objects.all()
    recent_posts = Post.objects.order_by('-pub_date')[:5]
    user = request.user
    if request.user.is_authenticated:
        auser = User.objects.get(username=user)  
        dash_user = Dashboard_User.objects.get(user_id=auser.id)
        photo = dash_user.photo
        return render(request, 'posts.html', {'categories': categories,'postCategories':postCategories,'category': category, 'posts': posts, 'is_blog_details':True, 'recent_posts': recent_posts, 'photo':photo})
    return render(request, 'posts.html', {'categories': categories,'postCategories':postCategories,'category': category, 'posts': posts, 'is_blog_details':True, 'recent_posts': recent_posts})

#     comments_count = [Comment.objects.filter(post=post).count() for post in posts]
#     return render(request, 'posts.html', {'categories': categories,'category': category, 'posts': posts, 'is_blog_details':True, 'recent_posts': recent_posts, 'comments_count' : comments_count})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    comments_count = Comment.objects.filter(post=post).count()
    user=request.user
    detailCategories=BlogCategory.objects.all()
    categories = CourseCategory.objects.all()
    recent_posts = Post.objects.order_by('-pub_date')[:5]

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            return redirect('blog:post_detail', post_id=post_id)
    else:
        form = CommentForm()
    user = request.user
    if request.user.is_authenticated:
        auser = User.objects.get(username=user)  
        dash_user = Dashboard_User.objects.get(user_id=auser.id)
        photo = dash_user.photo
        return render(request, 'post_detail.html', {'categories': categories,'detailCategories': detailCategories,'post': post, 'comments': comments, 'form': form,'is_blog_details':True, 'user':user, 'recent_posts': recent_posts, 'comments_count':comments_count, 'photo':photo})
    return render(request, 'post_detail.html', {'categories': categories,'detailCategories': detailCategories,'post': post, 'comments': comments, 'form': form,'is_blog_details':True, 'user':user, 'recent_posts': recent_posts, 'comments_count':comments_count})

