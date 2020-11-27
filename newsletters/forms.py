from django import forms
from django.forms import ModelForm
from newsletters.models import SubscribersList


class SubscribeForm(ModelForm):
    class Meta:
        model = SubscribersList
        fields = ['subscriber_email']

    subscriber_email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Въведи своята електранна поща',
                                                                      }))
