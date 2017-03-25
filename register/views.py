from .models import Post
from .forms import PostForm
from django.shortcuts import redirect, render, get_object_or_404
from hashlib import sha256


def post_list(request):
    posts = Post.objects.order_by('username')
    return render(request, 'register/post_list.html', {'posts': posts})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.password = sha256(form.cleaned_data['password'].encode('UTF-8')).hexdigest()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'register/post_edit.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'register/post_detail.html', {'post': post})
