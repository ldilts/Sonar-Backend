import datetime

from django.db import models
from django.utils import timezone
from gcm.utils import get_device_model

# Create your models here.
class Log(models.Model):
    log_id = models.IntegerField(default=0)
    log_open = models.BooleanField(default=False)
    log_date = models.DateTimeField('date published')

    def __str__(self):
    	return str(self.log_id)

    def was_published_recently(self):
        return self.log_date >= timezone.now() - datetime.timedelta(days=1)
        was_published_recently.admin_order_field = 'log_date'
    	was_published_recently.boolean = True
    	was_published_recently.short_description = 'Published recently?'

    # def save(self, *args, **kwargs):
    #     'faz alguma coisa'
    #     super(Log, self).save(*args, **kwargs)


# @receiver(post_save, sender=Log)
# def func(sender, **kwargs):