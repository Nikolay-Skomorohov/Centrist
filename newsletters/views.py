from django.shortcuts import render, redirect
from newsletters.models import SubscribersList
from newsletters.forms import SubscribeForm


def newsletter(request):
    if request.method == "GET":
        context = {
            "form": SubscribeForm(),
        }
        return render(request, "newsletters/newsletter.html", context)

    elif request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("newsletter")
        context = {
            "form": form,
        }

        return render(request, "newsletters/newsletter.html", context)

    elif request.method == "DELETE":
        if SubscribersList.objects.filter(subscriber_email=request.POST):
            SubscribersList.objects.filter(
                subscriber_email=request.POST
            ).delete()
        else:
            raise Exception("Невалидна електранна поща!")
        return redirect("newsletter")
