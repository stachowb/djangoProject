from django.contrib import admin
from .models import ProspectProfile, ProspectSkillset, Skills

admin.site.register(ProspectProfile)
admin.site.register(ProspectSkillset)
admin.site.register(Skills)