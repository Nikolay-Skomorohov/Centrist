from django.forms import ModelForm
from newsletters.models import SubscribersList


class SubscribeForm(ModelForm):
    class Meta:
        model = SubscribersList
        fields = ['subscriber_email']
