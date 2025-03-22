from .models import *
from django.forms import ModelForm, TextInput, Textarea, NumberInput, CheckboxInput


class ArticleForm(ModelForm):
    class Meta:
        model = Users
        fields = ['name','telephone','comment','prover']
        widgets = {
            'name': TextInput(attrs={'class':'form-control','placeholder':'Имя'}),

            'telephone': NumberInput(attrs={'class':'form-control','placeholder':'Телефон'}),

            'comment': Textarea(attrs={'class':'form-control','placeholder':'Комментарий'}),
            'prover': CheckboxInput(attrs={'class':'form-control'}),

        }