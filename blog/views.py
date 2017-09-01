from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Blog, Category, MailBox
import os
from django.shortcuts import redirect


# Create your views here.
def index(request):
    #Box = MailBox()
    #Box.fillUp()
    master=os.listdir("Data/")
    master.sort()
    features=[]
    for mess in master:
        f = open("Data/"+mess,"r",encoding="utf8")
        features.append(f.read())
        f.close()

    return render_to_response('index.html', {
        'emails': features[:-10:-1]
    })

def update(request):
    box= MailBox()
    box.update()
    return redirect('blogIndex')

def view_post(request, slug):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })
