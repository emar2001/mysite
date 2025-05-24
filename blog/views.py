from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post
def blog_view(request):
    posts = Post.objects.filter(status = 1)
    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pk):
    posts = Post.objects.filter(status = 1)
    post = get_object_or_404(posts, pk=pk)
    post.counted_views += 1
    post.save()
    context = {'post':post, 'pk':pk}
    return render(request, 'blog/blog-single.html', context)

def test(request,pid):
    #posts = Post.objects.get(id = pid)
    posts = get_object_or_404(Post,pk = pid)
    context = {'post' : posts}
    return render(request, 'test.html', context)
