from django import forms
from .models import UPSB, Battery


class PostUPS(forms.ModelForm):
	class Meta:
	    model = UPSB
	    fields = ('modUps', 'dateU', 'obitN', 'commentU', 'state', 'obitInsBat1', 'obitInsBat2', 'obitOutBat1', 'obitOutBat2','released',)
class PostBat(forms.ModelForm):
	class Meta:
	    model = Battery
	    fields = ('obitBN', 'modBat', 'state', 'commentB',)






