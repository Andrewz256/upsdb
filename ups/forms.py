from django import forms
from .models import UPSB, Battery


class PostUPS(forms.ModelForm):
    class Meta:
        model = UPSB
        fields = ('modUps', 'dateU', 'obitN', 'state', 'obitInsBat1', 'obitInsBat2', 'obitOutBat1', 'obitOutBat2','released',  'commentU',)
        widgets = {
	        # 'obitInsBat1': forms.TextInput(),
	        # 'obitInsBat2': forms.TextInput(),
	        # 'obitOutBat1': forms.TextInput(),
	        # 'obitOutBat2': forms.TextInput(),
	        'commentU': forms.Textarea(),
	    }
        labels = {
	      'obitInsBat1': "Insert_Battery_1",
	      'obitInsBat2': "Insert_Battery_2",
	      'obitOutBat1': "Remove_Battery_1",
	      'obitOutBat2': "Remove_Battery_1",
	      'obitN': "Obit ##",
	      'modUps': "Model",
	      'released': "in stock?",
	      'commentU': "Comment",
	      'dateU': "Date",
	    }
class PostBat(forms.ModelForm):
    class Meta:
         model = Battery
         fields = ('dateB','obitBN', 'modBat', 'state', 'commentB',)
         widgets = {
	       'commentB': forms.Textarea(),
	    }
         labels = {
	       'commentB': "Comment",
	       'dateB': "Date",
	       'obitBN': "Obit ##",
	       'modBat': "Model",
	    }






