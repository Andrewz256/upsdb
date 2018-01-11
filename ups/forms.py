from django import forms
from .models import UPSB, Battery


class PostUPS(forms.ModelForm):
	class Meta:
	    model = UPSB
	    fields = ('modUps', 'dateU', 'obitN', 'state', 'obitInsBat1', 'obitInsBat2', 'obitOutBat1', 'obitOutBat2','released',  'commentU',)
	    widgets = {
	        'obitInsBat1': forms.TextInput(),
	        'obitInsBat2': forms.TextInput(),
	        'obitOutBat1': forms.TextInput(),
	        'obitOutBat2': forms.TextInput(),
	        'commentU': forms.Textarea(),
	    }
class PostBat(forms.ModelForm):
	class Meta:
	    model = Battery
	    fields = ('obitBN', 'modBat', 'state', 'commentB',)
	    widgets = {
	       'commentB': forms.Textarea(),
	    }






