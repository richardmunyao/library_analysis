from django.shortcuts import render, redirect
from library_app.models import BookInfo
from library_app.forms import DocumentForm, UploadFileForm

# Non-Imaginary function to handle an uploaded file.
from library_app.scripts.procsv import handle_uploaded_file

# Create your views here.

# Uses a script to process uploaded CSV. Doesn't save the file.
def landing_page(request):
    if request.method == 'POST':
        print("!!Doing METHOD==POST")
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print("!!form is VALID")
            handle_uploaded_file(request.FILES['file'])
            return redirect('success_page')
        else:
            print("!!form is NOT VALID!",form.errors)
            return redirect('landing_page')
    else:
        form = UploadFileForm()
    return render(request, 'landing_page.html', {'form':form})



def success_page(request):
    return render(request, 'success_page.html', {})
