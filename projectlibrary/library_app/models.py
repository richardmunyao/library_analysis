from django.db import models

# Create your models here.

class BookInfo(models.Model):
    title = models.TextField()
    goodr_id = models.TextField(default=0)
    author = models.TextField()
    isbn = models.TextField()
    my_rating = models.TextField()
    avg_rating = models.TextField()
    pages = models.TextField()
    date_added = models.TextField()
    shelf = models.TextField()
    # genre = models.TextField() #Add later
    # description = models.TextField() #Add later

# to upload CSV document
class Document(models.Model):
    document = models.FileField(upload_to='user_uploads/%Y-%m-%d/') #change to CSVs/
    uploaded_at = models.DateTimeField(auto_now_add=True)
