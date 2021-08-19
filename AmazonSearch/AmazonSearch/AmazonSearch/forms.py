from django import forms

from .models import *

class CheckForm(forms.Form):
    # For BooleanFields, required=False means that Django's validation
    # will accept a checked or unchecked value, while required=True
    # will validate that the user MUST check the box.
    FilterByOwnPublisher = forms.BooleanField(required=False)
	
class KeyForm(forms.Form):
    keykey = forms.ModelChoiceField(queryset=KeyWord.objects.exclude(keyword_text = 'keyword').values_list('keyword_text' , flat=True) )
