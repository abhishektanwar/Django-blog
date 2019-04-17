from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


posts=[

    {
        'author':'abhishek',
        'title':'blog post 1',
        'content':'first blog post',
        'date_posted':'august 15,2015'
    },
    {
        'author':'vibe',
        'title':'blog post 2',
        'content':'second blog post',
        'date_posted':'august 16,2015'
    }
]


def home(request):
    
    context={
        'posts': posts
    }
    return render(request,'blog/home.html',context)
    
def about(request):
    return render(request,'blog/about.html',{'title':'About'})    