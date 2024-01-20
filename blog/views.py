# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Post, Comment
from .forms import CommentForm


def category_list(request):
    categories = Category.objects.all()
    print(categories)
    return render(request, 'blog.html', {'is_blog': True, 'categories': categories})

def post_list_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = Post.objects.filter(category=category)
    categories=Category.objects.all()
    recent_posts = Post.objects.order_by('-pub_date')[:5]
    return render(request, 'posts.html', {'categories': categories,'category': category, 'posts': posts, 'is_blog_details':True, 'recent_posts': recent_posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    user=request.user
    categories=Category.objects.all()
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

    return render(request, 'post_detail.html', {'categories': categories,'post': post, 'comments': comments, 'form': form,'is_blog_details':True, 'user':user, 'recent_posts': recent_posts})
