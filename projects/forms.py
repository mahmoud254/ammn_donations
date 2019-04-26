from django import forms
from projects.models import Document,Projects

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
    title = forms.CharField(label='title', max_length=100)
    comment = forms.CharField(widget=forms.Textarea,label='Your comment', max_length=100)