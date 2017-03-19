from django.shortcuts import render,redirect
from .models import BlogPost
from django.shortcuts import get_object_or_404 
from .forms import BlogPostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
#function base view
def home(request):
	template_name = 'index.html'
	blogs = BlogPost.objects.all() #queryset --> return all objects of Blogpost
	context = {'title':'Home', 'name':'krishna', 'blogs':blogs}
	 #curly braces is dictionary, () = tuple,[] = list
	return render(request, template_name, context)

def contact(request):
	template_name = 'contact.html'
	context = {'title':'Contact'}
	return render(request, template_name, context)


def about(request):
	template_name = 'about.html'
	context = {'title':'About'}
	return render(request, template_name, context)

@login_required
def createblog(request):
	if request.method== 'POST':
		form = BlogPostForm(request.POST,request.FILES)
		
		if form.is_valid():
			form = form.save(commit=False)
			form.author = request.user
			form.save()
			return redirect('home')
	else:
		form = BlogPostForm()
	context = {'form': form}
	template_name = 'blog_create.html'
	return render(request, template_name, context)
    	
			
		

def detail(request, pk):
	template_name = 'post.html'
	blog= get_object_or_404(BlogPost, pk=pk)
	context = {'blog':blog}
	return render(request, template_name, context)



def signup(request):
	template_name="registration/signup.html"
	if request.method=="POST":
	    form = UserCreationForm(request.POST)
	    if form.is_valid():
	    	form.save()
	    	return redirect('home')
	else:
		form=UserCreationForm()
	context = {'form': form}
	return render(request,template_name,context)
		
		
