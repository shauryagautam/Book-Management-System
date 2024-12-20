from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'isbn', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_publication_year(self):
        year = self.cleaned_data['publication_year']
        if year < 1000 or year > 9999:
            raise forms.ValidationError("Please enter a valid 4-digit year.")
        return year

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        if not isbn.isdigit() or len(isbn) != 13:
            raise forms.ValidationError("ISBN must be a 13-digit number.")
        return isbn

