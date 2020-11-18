from django.db import models


class SubscribersList(models.Model):
    subscriber_email = models.EmailField(null=False)

    def __str__(self):
        return self.subscriber_email
