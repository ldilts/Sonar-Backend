import datetime

from django.db import models
from django.utils import timezone
# from gcm.utils import get_device_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import signals

# @receiver(post_save, sender=Log)
def my_callback(sender, **kwargs):
    print("Request finished!")
    # Device = get_device_model()
    # device = Device.objects.get(dev_id=241120152203)
    # device.send_message(notification={"sound":"Default", "badge":"1", "title":"Sonar", "body":"Door notification!"})
    # print("Notification sent!")

# Create your models here.
class Distance(models.Model):
    dist_id = models.IntegerField(default=0)
    dist_distance = models.FloatField(default=0.0)
    dist_date = models.DateTimeField('date published', blank=True)

    def __str__(self):
    	return str(self.dist_id)

    def was_published_recently(self):
        return self.dist_date >= timezone.now() - datetime.timedelta(days=1)
        was_published_recently.admin_order_field = 'dist_date'
    	was_published_recently.boolean = True
    	was_published_recently.short_description = 'Published recently?'

signals.post_save.connect(my_callback, sender=Distance)
