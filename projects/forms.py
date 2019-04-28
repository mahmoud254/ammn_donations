from django import forms
from projects.models import Projects
from projects.models import Category
from django.contrib.admin import widgets
class DocumentForm(forms.Form):
    title = forms.CharField(label='Title',required=True)
    tags = forms.CharField(label='enter tags separated by #',required=True)
    details =forms.CharField(widget=forms.Textarea,label='Details',required=True)
    total_target=forms.IntegerField(required=True)
    start_date=forms.DateField(required=True,widget=widgets.AdminDateWidget)
    end_date=forms.DateField(required=True,widget=widgets.AdminDateWidget)
    document=forms.FileField(required=True)
    result = [(q["id"], q['categories']) for q in Category.objects.values()]
    category_id = forms.ChoiceField(choices=result, required=True )