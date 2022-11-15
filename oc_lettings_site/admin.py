from django.contrib import admin

from app_lettings.models import Letting, Address
from app_profiles.models import Profile


admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
