from django import forms
from projects.models import Projects
from projects.models import Category
from django.contrib.admin import widgets
class DocumentForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'enter project title'}),required=True)
    tags = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'enter tags separated by #'}),required=True)
    details =forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'enter project details'}),label='Details',required=True)
    total_target=forms.IntegerField(required=True,widget=forms.TextInput(attrs={'placeholder': 'enter total target in dollars'}))
    start_date=forms.DateField(required=True,widget=widgets.AdminDateWidget)
    end_date=forms.DateField(required=True,widget=widgets.AdminDateWidget)
    document=forms.FileField(required=True)
    result = [(q["id"], q['categories']) for q in Category.objects.values()]
    category_id = forms.ChoiceField(choices=result, required=True )
