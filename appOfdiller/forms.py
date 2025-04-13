from django.db.models import Model

from .models import *
from django.forms import ModelForm, TextInput, Textarea, NumberInput, CheckboxInput, Select
from django import forms



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

class ArticleForm2(ModelForm):
    class Meta:
        model = TestDrive
        fields = ['title','name','telephone','comment','prover']
        widgets = {
            'title': Select(attrs={'class':'form-control','placeholder':'Выберите модель'}),
            'name': TextInput(attrs={'class':'form-control','placeholder':'Имя'}),

            'telephone': NumberInput(attrs={'class':'form-control','placeholder':'Телефон'}),

            'comment': Textarea(attrs={'class':'form-control','placeholder':'Комментарий'}),
            'prover': CheckboxInput(attrs={'class':'form-control'}),

        }

class PoiskForm(forms.Form):
    modeli = forms.ModelChoiceField(queryset=Modeli.objects.all(), required=False, label='Модель')
    cvet = forms.ModelChoiceField(queryset=Cvet.objects.all(), required=False, label='Цвет')
    comp = forms.ModelChoiceField(queryset=Comp.objects.all(), required=False, label='Коммплектация')