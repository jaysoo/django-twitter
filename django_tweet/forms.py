from django.utils.translation import ugettext_lazy as _
from django import forms
from models import TwitterAccount

class TwitterForm(forms.ModelForm):
    class Meta:
        model = TwitterAccount
