from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

# Create your views here.
def index(request):
	allposts = Blogpost.objects.all()
	params = {
	'allposts': allposts 
	}
	return render(request, 'blog/index.html',params)
def blogpost(request):
	# title = head0 = head1 = head2 = chead0 = chead1 = chead2 = pub_date = ""
	return render(request, 'blog/blogpost.html')