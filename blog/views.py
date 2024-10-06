from django.shortcuts import render
from .models import BlogPost
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    posts = BlogPost.objects.all().order_by('-event_date')
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'blog/post.html', {'post': post})

def section_view(request, section):
    posts = BlogPost.objects.filter(section=section).order_by('-event_date')
    return render(request, 'blog/section.html', {'posts': posts, 'section': section})
