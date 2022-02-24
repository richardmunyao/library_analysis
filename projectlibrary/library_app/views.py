from django.shortcuts import render
from library_app.models import BookInfo
from library_app.forms import DocumentForm
# Create your views here.

def landing_page(request):
    print("Showing landing page")
    if request.method == 'POST':
        print("PoSTinGGG!")
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print("Valid!")
            form.save()
        else:
            print("Not Valid!",form.errors)
            return redirect('landing_page')
    else:
        form = DocumentForm()
    return render(request, 'landing_page.html', {'form':form})
    
