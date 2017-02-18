from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .models import Post

from .forms import PostForm
# Create your views here.
def post_list(request):
    queryset_list=Post.objects.all()#.order_by("-timestamp")
    paginator = Paginator(queryset_list, 2) # Show 25 contacts per page
    page_request_var="page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context={
    "object_list":queryset,
    "title":"list",
    "page_request_var" : page_request_var
    }
    return render(request,"index.html",context)


def post_create(request):
    form=PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    # else:
    #     messages.error(request,"not successful")

    context={
    "form":form
    }
    return render(request,"post_form.html",context)

def post_update(request,id=None):

    instance=get_object_or_404(Post,id=id )

    form=PostForm(request.POST or None,request.FILES or None,instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"Successfully updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    # else:
    #     messages.error(request,"not Successfully updated")
    context={
    "instance":instance,
    "form":form,
    "title":instance.title
    }

    return render(request,"post_form.html",context)

def post_retrieve(request,id):

    instance=get_object_or_404(Post,id=id)
    context={
    "title":instance.title,
    "instance":instance
    }
    return render(request,"post_detail.html",context)


def post_delete(request,id):
    instance=get_object_or_404(Post,id=id)
    instance.delete()

    messages.success(request,"Successfully deleted")

    return redirect("posts:list")