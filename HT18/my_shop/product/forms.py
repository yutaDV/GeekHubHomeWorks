from django.forms import ModelForm, Textarea
from django import forms

from .models import ScrapingTask


class NewIdsForm(ModelForm):
   class Meta:
      model = ScrapingTask
      fields = ('New_ids',)
      widgets = {'New_ids': Textarea(attrs={'cols': 30, 'rows': 20}),}
