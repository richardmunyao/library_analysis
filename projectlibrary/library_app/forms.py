from django import forms
from library_app.models import Document

#Uses ModelForm to save CSV. Inactive for now.
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document',)
        labels = {
            "document": "Select your CSV",
        }

class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50) #perhaps can use later?
    file = forms.FileField(label="Select CSV:")
