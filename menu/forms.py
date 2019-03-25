from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.forms.widgets import SelectDateWidget, CheckboxSelectMultiple

from .models import Menu, Item, Ingredient
from django.conf import settings

class MenuForm(forms.ModelForm):
    season = forms.CharField(label='Season:')
    items = forms.ModelMultipleChoiceField(
        label='Available Flavors:',
        queryset=Item.objects.all(),
        widget=CheckboxSelectMultiple()
        )
    expiration_date = forms.DateField(
        label='Expiration Date:',
        widget=forms.SelectDateWidget(
            years=list(range(2010, 2030))))

    class Meta:
        model = Menu
        exclude = ('created_date',)