from django.contrib import admin
from .models import Account, UserProfile, Blog, ContactForm



# Register your models here.
admin.site.register(Account)
admin.site.register(UserProfile)
admin.site.register(Blog)
admin.site.register(ContactForm)

