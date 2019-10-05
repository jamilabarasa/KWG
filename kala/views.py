from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Member, New , Comment
from .forms import CommentForm
from django.contrib import messages
# Create your views here.
@login_required
def shownews(request):
    posts = New.objects.order_by('-published')
    return render (request,'news.html',{'posts':posts})

@login_required
def dasboard(request):
    return render(request,'dashboard.html',{'section':dasboard})

@login_required
def pwd(request):
    return render(request,'passwd.html')

@login_required
def bill(request):
    return render(request,'billing.html')

@login_required
def about(request):
    return render(request,'about.html')

@login_required
def add_comment(request,pk):
    post = get_object_or_404(New,pk=pk),
    comment = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('about')
    else:
        form = CommentForm()
    return render(request,'comment.html',{'form':form,'comment':comment})
