from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.decorators.http import require_POST

from newsletters.models import SubscribersList
from newsletters.forms import SubscribeForm


def newsletter(request):
    template = loader.get_template('newsletters/newsletter.html')
    context = {'form': SubscribeForm(),
               }
    return HttpResponse(template.render(context, request))


@require_POST
def subscribe(request):
    email_input = request.POST['subscriber_email']
    if SubscribersList.objects.filter(subscriber_email=email_input):
        raise Exception("Електранната поща вече съществува в базата данни!")
    else:
        new_subscriber = SubscribersList(subscriber_email=email_input)
        new_subscriber.save()

    return HttpResponseRedirect(reverse('newsletter'))


def unsubscribe(request):
    if request.method == "DELETE":
        email_input = request.POST['subscriber_email']
        if SubscribersList.objects.filter(subscriber_email=email_input):
            SubscribersList.objects.filter(subscriber_email=email_input).delete()
        else:
            raise Exception("Невалидна електранна поща!")
        return HttpResponseRedirect(reverse('newsletter'))
