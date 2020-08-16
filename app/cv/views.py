from django.shortcuts import render
from .forms import PostForm
from .models import Post
from django.views.generic import View
from django.shortcuts import redirect
import uuid

class AddPost(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'index.html', context={'form':form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        return render(request, 'index.html', context={'form':form})

class ShowPosts(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'show_posts.html', context={'posts':posts})
