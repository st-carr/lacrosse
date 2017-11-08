from django import forms
from django.forms import ModelForm
from .models import Player
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class FlagPlayerForm(forms.Form):
    user_report = forms.CharField(max_length=1000, widget=forms.Textarea)
    def clean_flag_player(self):
        data = self.cleaned_data['user_report']
        # Remember to always return the cleaned data.
        return data


class EditPlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['number', 'name', 'height', 'weight', 'position', 'state', 'year', 'high_school', 'hs_type', 'city']


class AddPlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['number', 'name', 'height', 'weight', 'position', 'state', 'year', 'high_school', 'hs_type', 'city']
