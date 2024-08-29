from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blogTaller/post_list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', id=post.id)
    else:
        form = CommentForm()

    return render(request, 'blogTaller/post_detail.html', {'post': post, 'comments': comments, 'form': form})

def post_edit(request, id=None):
    if id:
        post = get_object_or_404(Post, id=id)
    else:
        post = Post()

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', id=post.id)  
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blogTaller/post_edit.html', {'form': form, 'post': post})
