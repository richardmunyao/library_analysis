# library_analysis. A Django project to analyze contents of a user's Goodreads exported library.
This is my first attempt at documentation.<br/>
Hopefully I should be able to make sense of this project some time later. <br/>
This is a Django project.<br/>
The project name is `project_library` and it has one app, called `library_app`
The goal is to analyze a user's Goodreads exported library. You can export your goodreads library in csv format using the instructions given [here](https://help.goodreads.com/s/article/How-do-I-import-or-export-my-books-1553870934590): <br/>
Once you have a CSV file, upload it on the [homepage](http://127.0.0.1:8000/) <br/>
### Processeses in background: <br/>
The homepage is rendered by `library_app/views.py`, specifically `def landing_page(request):` <br/>
This renders the html template `landing_page.html` together with a `UploadFileForm` defined in `library_app/forms.py` to allow file upload <br/>
###### Important: <br/>
I added:
```
MEDIA_URL = 'CSVs/'

MEDIA_ROOT = (
    BASE_DIR / "projectlibrary" / MEDIA_URL
)
```
to the bottom of `project_library/settings.py` to define path to uploaded CSVs <br/>

Once the file is uploaded, a script, `procsv` found in: `library_app/scripts/procsv.py` is called. This script reads the CSV file using Pandas and creates a `BookInfo` object (defined in `library_app/models.py`) for each book, and saves it. <br/>
Then a success page is rendered.

On the website, we have a `Library Page` This shows a table of all the books that were in the CSV, now in our database as `BookInfo` objects. </br>
This is handled in `library_app/views.py` by the function `def library_page(request):`. <br/>
The function fetches all `BookInfo` objects, and using `Paginator` from `django.core.paginator` , I display 25 books per page (there could be hunddreds).

Then we have a `Charts` page also on the website. This is handled by two methods: `def chart_page()` and `def chart_expound()` <br/>

##### Logic for function chart_page():
Our goal with this function is to build to lists; 'subject' vs 'count'. Example: `[fiction, fantasy, magic, ...]` and `[12, 50, 11 ...]` So that we can eventually plot a pie chart. <br/>
This function builds a query set of all `BookInfo` objects column 'subjects' <br/>
We then convert into a pandas dataframe. This is because so far, this is the only way I found to split the 'subjects' by **~** and count number of times each subject type appears for all `BookInfo` objects. <br/>
The reason why I split the different book subjects by this separator: **~** is because some book descriptions have commas in them too. <br/>
Example: **Half of a Yellow Sun** has the following subjects:
```
nigeria, fiction
fiction
fiction, historical
general,
new york times reviewed
historical fiction
war
anisfield-wolf book award winner
```
Each line above represents how I got the subject data. So I had to split them using **~**. Perhaps this represents a flaw in how I fetched and populated book subject info (see isbn_updater project on my profile). Anyway, it caused me lots of headaches. _Look into this when I refactor, how to make it better. Also how to use many to many relationship structure in Django for book subjects._

Moving on, after I convert this info into dataframes, I clean it; `df_count = df_count.drop(nonsense_categories)` and make two lists: `subj[]` and the number of times the subject appears `hits[]`

This is passed as context to `chart_page.html` <br/>

##### Logic for chart_page.html:
I used chartjs for the chart display.
In the config part of the script, I obtain the `subj[]` and `hits[]` sent from views.py.<br/>
**todo** _Unfortunately as written, the template is open to HTML injection. This is because if the data contains </script> anywhere, the rest of the result will be parsed as extra HTML. We call this HTML injection_  <br/>
To allow user to expound on the clicked portion of pie chart, another javascript function, `expound()` is called with arguments as `label`(subject) and count. <br/>
This will be passed to `views.py/chart_expound()` <br/>
In `chart_page.html` we also create a modal, and populate its one paragraph with a string that contains book titles, separated by line breaks `<br/>` <br/>


##### Logic for function chart_expound():
We get the `label`(subject) from the javascript function mentioned above: `function expound()` <br/>
We do a simple search on all objects in our DB
```
book_result = BookInfo.objects.filter(subjects__icontains=label).values()
```
We convert this queryset.values() to list, then pass it as JSON response to the javascript function that called it - `function expound()` <br/>
For now, we only loop through first 10 results, and display this info in the modal.
<br/>
<br/>
Fin.
<br/>
<br/>

This was a very basic project now that I write this documentation, and I don't see why it took me so long. But I was out of practice, and slow learning is still better than no learning. <br/>
It is in no way whatsoever done, with lots of work left. But I learnt a lot from this. <br/>
Richard Munyao <br/>
richard.munyao@gmail.com
