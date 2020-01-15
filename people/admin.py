from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from people.models import Person


class PersonInline(admin.StackedInline):
    model = Person
    can_delete = False
    verbose_name_plural = 'people'


class UserAdmin(UserAdmin):
    inlines = (PersonInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
