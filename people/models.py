from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from lists.models import List


class Person(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField()
    dob = models.DateField()
    location = models.CharField(max_length=100)
    web = models.URLField()
    avatar = models.URLField()

    def custom_lists(self):
        lists = List.objects.filter(user=self.user, type=List.CUSTOM)

        return lists

    def favorite_list(self):
        favorite_list = List.objects.get(
            user=self.user,
            type=List.FAVORITE
        )

        return favorite_list

    def seen_list(self):
        seen_list = List.objects.get(
            user=self.user,
            type=List.SEEN
        )

        return seen_list

    def must_see_list(self):
        must_see_list = List.objects.get(
            user=self.user,
            type=List.MUST_SEE
        )

        return must_see_list


@receiver(post_save, sender=User)
def create_standard_lists(sender, instance, created, **kwargs):
    if created:
        favorite_list = List.objects.create(
            user=instance,
            name='Favorite',
            description='A list with movies of the favorite movies of the user.',
            type=List.FAVORITE
        )

        seen_list = List.objects.create(
            user=instance,
            name='Seen',
            description='A list with movies of the seen movies of the user.',
            type=List.SEEN
        )

        must_see_list = List.objects.create(
            user=instance,
            name='Must See',
            description='A list with movies of the must-see movies of the user.',
            type=List.MUST_SEE
        )
