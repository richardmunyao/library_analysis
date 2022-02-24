from django import forms
from library_app.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document',)
