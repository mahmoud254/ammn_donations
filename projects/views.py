from django.shortcuts import render
from projects.forms import DocumentForm
# Create your views here.

def show_projects(request):
    return render(request, 'projects/index.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'projects/model_form_upload.html', {
        'form': form
    })