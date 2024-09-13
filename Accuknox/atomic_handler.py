from django.db import transaction

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    with transaction.atomic():
        instance.related_model.objects.create(...)