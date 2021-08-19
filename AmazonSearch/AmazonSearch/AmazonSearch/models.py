from django.db import models
from django.forms import ModelForm

class KeyWord(models.Model):
    keyword_text = models.CharField(max_length=128)

class KeyWordForm(ModelForm):
	class Meta:
		model = KeyWord
		fields = ['keyword_text']

class Title(models.Model):
	asin = models.CharField(max_length=16, default='0')
	title_text = models.CharField(max_length=128)
	publisher = models.CharField(max_length=128)
	marketingservices = models.CharField(max_length=1)
	batch = models.CharField(max_length=16)

#class TitleForm(ModelForm):
#	class Meta:
#		model = Title
#		fields = ['asin', 'title_text', 'publisher', 'marketingservices', 'batch']

class Search(models.Model):
	keyword_text = models.CharField(max_length=128)
	date = models.CharField(max_length=128)
	page = models.CharField(max_length=16)
	position = models.CharField(max_length=16)
	title_text = models.CharField(max_length=128)
	author = models.CharField(max_length=128)
	publisher = models.CharField(max_length=128)
	pages = models.CharField(max_length=16)
	publication_date = models.CharField(max_length=128)
	sales_rank = models.CharField(max_length=16)
	image_link = models.CharField(max_length=256)
	asin = models.CharField(max_length=16)
	
#class SearchForm(ModelForm):
#	class Meta:
#		model = Search
#		fields = ['keyword_text', 'date', 'page', 'position', 'title_text', 'author', 'publisher', 'pages', 'publication_date', 'sales_rank', 'image_link', 'asin']

