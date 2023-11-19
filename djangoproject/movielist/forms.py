
from django import forms
from .models import Movies

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['moviename', 'direcname', 'language','year','rating','poster']
class MovieSearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False)
    filter_by_name = forms.BooleanField(required=False)
    filter_by_director = forms.BooleanField(required=False)
    filter_by_release_year = forms.BooleanField(required=False)
    filter_by_language = forms.BooleanField(required=False)
    filter_by_rating = forms.BooleanField(required=False)
class MovieUpdateForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['moviename', 'direcname', 'language','year','rating']