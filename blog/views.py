from django.shortcuts import render, redirect
from .models import Blog
from .models import comment
from .forms import CommentForm
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

def home(request):
    posts = Blog.objects.filter().order_by('date')
    return render(request, 'index.html', {'posts' : posts})

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == 'POST' or request.method == 'FILES':
        post = Blog()
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.photo = request.FILES['photo']
        post.date = timezone.now()
        post.save()
    return redirect('home')

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    comment_form = comment()
    return render(request, 'detail.html', {'blog_detail' : blog_detail , 'comment_form' : comment_form})

def makecomment(request, blog_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit = False)
        finished_form.post = get_object_or_404(Blog, pk = blog_id)
        finished_form.save()
    return redirect('detail', blog_id)


