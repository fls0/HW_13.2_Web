from django.forms import CharField, ModelForm, TextInput, DateField, DateInput, Textarea, Field
from .models import Author, Quote, Tag


class AddAuthorForm(ModelForm):
    fullname = CharField(max_length=50, min_length=5,
                            widget=TextInput(attrs={"class": "form-control", "id": "InputFullname"}))
    born_date = DateField(widget=DateInput(attrs={"class": "form-control", "id": "InputBornDate"}))
    born_location = CharField(max_length=50, min_length=5,
                            widget=TextInput(attrs={'cols': 30, 'rows': 10, "class": "form-control", "id": "InputBornLocation"}))
    description = CharField(widget=Textarea(attrs={"class": "form-control", "id": "InputDescription"}))

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

class AddQuoteForm(ModelForm):
    quote = CharField(max_length=300, widget=Textarea(attrs={'cols': 30, 'rows': 10, "class": "form-control", "id": "InputQuote"}))
    tags = CharField(max_length=300, widget=TextInput(attrs={"class": "form-control", "id": "InputTags"}))
    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]

class ViewAuthorForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']
