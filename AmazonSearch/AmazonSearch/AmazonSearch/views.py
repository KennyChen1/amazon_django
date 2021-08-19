from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import *
from .forms import *


def index(request):
	form = CheckForm(request.POST or None)
	keykeykey = KeyForm()
	
			
	if request.method == 'POST':
		post = request.POST.get('keykey')
		searches = Search.objects.filter(keyword_text__exact = post)
		some_var = request.POST.getlist('FilterByOwnPublisher')
		if some_var:
			asin = (Title.objects.values_list('asin' , flat=True))
			
			searches =  searches.filter(asin__in=asin)
		else:
			print('no')
			
		searches = searches.exclude(keyword_text = 'keyword').values_list().values()
		return render(request, "template/index.html",  locals())
	else:
		
		keywords = (KeyWord.objects.values_list('keyword_text' , flat=True))	
		return render(request, "template/index.html",  locals())
