from django.db import models

# Create your models here.

class BookInfo(models.Model):

    goodr_id = models.TextField(default=0)
    title = models.TextField()
    author = models.TextField()
    isbn = models.TextField()
    my_rating = models.TextField()
    avg_rating = models.TextField()
    pages = models.TextField()
    date_added = models.TextField()
    shelf = models.TextField()
    subjects = models.TextField()
    # genre = models.TextField() # (now called subjects)
    # description = models.TextField() #Add later

# to upload and save CSV document. Inactive for now.
class Document(models.Model):
    document = models.FileField(upload_to='user_uploads/%Y-%m-%d/') #change to CSVs/
    uploaded_at = models.DateTimeField(auto_now_add=True)
