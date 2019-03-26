from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.forms.widgets import SelectDateWidget, CheckboxSelectMultiple

from .models import Menu, Item, Ingredient
from django.conf import settings

# VALIDATORS (EXTRA CREDIT)
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_season(value):
    if len(value) < 4:
        raise ValidationError(
            _('" %(value)s " is not descriptive enough for your menu.'),
            params={'value': value},
        )
    if value.isnumeric():
        raise ValidationError(
            _('Season may not be only digits.'),
            params={'value': value},
        )


# FORMS
class MenuForm(forms.ModelForm):
    season = forms.CharField(label='Season:', validators=[validate_season])
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
