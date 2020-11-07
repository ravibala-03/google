from django import forms
from  .models  import SearchResult


class SearchForm(forms.ModelForm):
    class Meta():
       model= SearchResult
       fields = '__all__'

class UpdateForm(forms.ModelForm):
    class Meta():
       model= SearchResult
       fields = '__all__'