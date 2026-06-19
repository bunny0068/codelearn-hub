from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.core.paginator import Paginator
from .models import Post, Comment
from .forms import PostForm, CommentForm

def blog(request):
    search = request.GET.get('search')
    if search:
        posts = Post.objects.filter(
            title__icontains=search
        ).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {
        'title': 'Blog',
        'posts': posts
    }
    return render(
        request,
        'blog/blog.html',
        context
    )

def post_detail(request, pk):

    post = get_object_or_404(Post, pk=pk)

    comments = Comment.objects.filter(
        post=post
    ).order_by('-created_at')

    if request.method == "POST":

        form = CommentForm(request.POST)

        if form.is_valid():

            comment = form.save(commit=False)

            comment.post = post
            comment.author = request.user

            comment.save()

            return redirect(
                'blog:post_detail',
                pk=post.pk
            )

    else:

        form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form
    }

    return render(
        request,
        'blog/post_detail.html',
        context
    )




@login_required
def create_post(request):
    form = PostForm()
    context = {'form': form}
    return render(request,'blog/create_post.html',context)

@login_required 
@login_required
def create_post(request):

    if request.method == "POST":

        form = PostForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            post = form.save(commit=False)

            post.author = request.user

            post.save()

            return redirect('blog:blogpage')

    else:

        form = PostForm()

    context = {
        'form': form
    }

    return render(
        request,
        'blog/create_post.html',
        context
    )

@login_required
def update_post(request, pk):
    return render(request, 'blog/update_post.html')
    

@login_required
def update_post(request, pk):

    post = get_object_or_404(
        Post,
        pk=pk
    )

    if request.user != post.author:
        return redirect('blog:blogpage')

    form = PostForm(instance=post)

    if request.method == "POST":
        form = PostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if form.is_valid():
            form.save()
            return redirect('blog:blogpage')

    context = {
        'form': form
    }

    return render(
        request,
        'blog/update_post.html',
        context
    )

    if request.method == "POST":

        form = PostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if form.is_valid():
            form.save()
            return redirect(
                'blog:blogpage'
            )

    else:

        form = PostForm(
            instance=post
        )

    context = {
        'form': form
    }

    return render(
        request,
        'blog/update_post.html',
        context
    )

@login_required
@login_required
def delete_post(request, pk):

    post = get_object_or_404(Post, pk=pk)

    if request.user != post.author:
        return redirect('blog:blogpage')

    if request.method == "POST":
        post.delete()
        return redirect('blog:blogpage')

    context = {
        'post': post
    }

    return render(
        request,
        'blog/delete_post.html',
        context
    )

def signup(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('blog:login')

    else:

        form = UserCreationForm()

    context = {
        'form': form
    }

    return render(
        request,
        'blog/signup.html',
        context
    )

@login_required
def delete_comment(request, pk):

    comment = get_object_or_404(
        Comment,
        pk=pk
    )

    if request.user != comment.author:
        return redirect('blog:blogpage')

    if request.method == "POST":

        post_pk = comment.post.pk

        comment.delete()

        return redirect(
            'blog:post_detail',
            pk=post_pk
        )

    context = {
        'comment': comment
    }

    return render(
        request,
        'blog/delete_comment.html',
        context
    )

@login_required
def update_comment(request, pk):

    comment = get_object_or_404(
        Comment,
        pk=pk
    )

    if request.user != comment.author:
        return redirect('blog:blogpage')

    form = CommentForm(instance=comment)

    if request.method == "POST":

        form = CommentForm(
            request.POST,
            instance=comment
        )

        if form.is_valid():
            form.save()

            return redirect(
                'blog:post_detail',
                pk=comment.post.pk
            )

    context = {
        'form': form
    }

    return render(
        request,
        'blog/update_comment.html',
        context
    )

@login_required
def profile(request):

    posts = Post.objects.filter(
        author=request.user
    )

    context = {
        'posts': posts
    }

    return render(
        request,
        'blog/profile.html',
        context
    )