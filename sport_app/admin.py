from django.contrib import admin
from .models import Trainer, Section, Athlete, Schedule, Subscription

admin.site.register(Trainer)
admin.site.register(Section)
admin.site.register(Athlete)
admin.site.register(Schedule)
admin.site.register(Subscription)