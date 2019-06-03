from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.

# posts=[
#     {
#         'author':'cour',
#         'title':'name',
#         'date':'August 14'
#     },
#     {
#         'author':'cour',
#         'title':'name',
#         'date':'August 4'
#     }
# ]

# def home(request):
#     template=loader.get_template('blog/home.html')
#     context={'posts' : Post.objects.all(),
#         'title':'home',
#         }
#     return HttpResponse(template.render(context,request))

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #it looks for template in 
                                     #app/model_viewtype.html ,but we are telling here explicitly
    context_object_name = 'posts'
    ordering =['-date_posted'] #change the order of post based on date, - puts latest posts first

class PostDetailView(DetailView):
    model = Post
#LoginRequiredMixin -> user is logged in
#UserPassesTestMixin -> user is owner of that content  
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post    
    fields = ['title','content']
    #to tell authod id
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model= Post
    fields = ['title','content']
    #to tell authod id
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    #to chk if author is updating a post or not
    def test_func(self):
        post = self.get_object() #to get the post to update
        if self.request.user == post.author :
            return True
        return False    


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url='/'
    #to chk if author is updating a post or not
    def test_func(self):
        post = self.get_object() #to get the post to update
        if self.request.user == post.author :
            return True
        return False

    

def about(request):
    template=loader.get_template('blog/about.html')
    context={
        'title':'about',
    }
    return HttpResponse(template.render(context,request))