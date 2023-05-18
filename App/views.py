from django.shortcuts import render, get_object_or_404
from .models import Post, PostImage
from django.views import generic


# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


# class DetailView(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'post_detail.html', {
        'post':post,
        'photos':photos
    })



