import re
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
import gender_guesser.detector as gender

from app.models import Student


@receiver(pre_save, sender=Student)
def normal_name(sender, instance, **kwargs):
    fullname = " ".join((instance.name, instance.surname))
    instance.normalized_name = re.sub('[^\w\s]|_', '', fullname).lower()   # noqa


@receiver(pre_save, sender=Student)
def gender_control(sender, instance, **kwargs):
    detect = gender.Detector()
    instance.sex = detect.get_gender(instance.name)


@receiver(pre_delete, sender=Student)
def cancel_deletion(sender, instance, **kwargs):
    raise Exception("don't delete")
