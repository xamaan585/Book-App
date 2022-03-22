from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponseRedirect 
# Create your views here.
def index(request):


	products = Product.objects.all()
	if request.method == 'POST':
			form = ProductForm(request.POST, request.FILES)
			if form.is_valid():
					post = form.save(commit=False)
					post.user = request.user
					post.save()
					return HttpResponseRedirect(request.path_info)
	else:
			form = ProductForm()
	params = {
        'products':products,
				'form': form, 
       
        }
	return render(request, 'index.html', params)
