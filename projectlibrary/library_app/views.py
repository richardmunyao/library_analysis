from django.shortcuts import render, redirect
# from django.contrib.postgres.search import SearchQuery
from django.http import JsonResponse
from library_app.models import BookInfo
from library_app.forms import DocumentForm, UploadFileForm
from django.core.paginator import Paginator
import pandas as pd

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

def library_page(request):
    # Fill in logic to fetch data and display it in table
    book_object = BookInfo.objects.all()
    #paginate. Too many books
    paginator = Paginator(book_object, 25) # Show 25 books per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
    "book_instance" : page_obj
    }
    return render(request, 'library_page.html', context)


# show chart of subject frequency (ex: 50 books have subject tag: 'fiction')
def chart_page(request):
    subj = []
    hits = []
    # all_books = BookInfo.objects.all()
    subjects_query_set = BookInfo.objects.values('subjects')
    # print(subjects_query_set)
    # for subj in subjects_query_set:
    #     print(subj)
    # Gonna convert our query set to pandas data frame (df).
    # Because this is currently the only way I know how to proceed
    # Using logic in subject_counts.py from isbn_updater
    print("***********************************")
    pd.set_option('display.max_rows', None) # don't truncate rows when I do print()
    df = pd.DataFrame(subjects_query_set)
    # print("DF:",df)
    print("***********************************")
    #Splits subjects by '~' and counts occurences. Bulds key, value pair, e.g {'fantasy':3}
    df_count = df.subjects.str.get_dummies(sep="~").sum().sort_values(ascending=False)
    # drop some nonsense categories
    nonsense_categories = ['accessible book', 'protected daisy', '=', 'general', '"', 'ficción', 'nan']
    df_count = df_count.drop(nonsense_categories)
    #show only top X (20) categories
    top_x = df_count.head(20)
    print(top_x)
    # convert to list so we can draw chart in js
    subj = top_x.keys().tolist()
    hits = top_x.values.tolist()

    context = {
    "subj" : subj,
    "hits" : hits
    }

    return render(request, 'chart_page.html', context)



# Expound on clicked segment of pie chart
def chart_expound(request):
    if request.method == 'POST':
        print("Method is POST")
        if 'label' in request.POST:
            label = request.POST['label']
            value = request.POST['value']
            print(label, value)

            # Searching our Database for matching label
            book_result = BookInfo.objects.filter(subjects__icontains=label).values()
            print("Found: ",len(book_result))
            response = {
            "result" : 'ok',
            "message" : f'Found {len(book_result)}',
            "book_result": list(book_result) # convert book_result to list, so that it is JSON serializable
            }

            return JsonResponse(response, safe=False) #False because QuerySet is not JSON serializable
    response={
    "result" : 'fail',
    "message" : 'not post?'
    }

    # return HttpResponse(json.dumps(response), content_type="application/json")
    return JsonResponse(response)
