from django.contrib import admin
from .models import Admin, Agent, Client

admin.site.register(Admin)
admin.site.register(Agent)
admin.site.register(Client)