from django.shortcuts import render, redirect
from .forms import DocumentForm
from .utils import perform_data_cleaning
from django.shortcuts import render


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            perform_data_cleaning(form.cleaned_data)
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })


def index_view(request):
    return render(request, 'home.html')

