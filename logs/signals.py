# from django.db.models import Log
# from gcm.utils import get_device_model
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from logs.models import Log

# @receiver(post_save, sender=Log)
# def my_callback(sender, **kwargs):
#     print("Request finished!")
#     # Device = get_device_model()
#     # device = Device.objects.get(dev_id=241120152203)
#     # device.send_message(notification={"sound":"Default", "badge":"1", "title":"Sonar", "body":"Door notification!"})