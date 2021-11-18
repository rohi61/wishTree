from django.contrib import admin
from .models import groop_action_history,groop_list,groop_member_list

admin.site.register(groop_member_list)
admin.site.register(groop_action_history)
admin.site.register(groop_list)
# Register your models here.
