from django.contrib import admin

from .models import Line, Station, Stop

# Register your models here.
admin.site.register(Line)
admin.site.register(Station)
admin.site.register(Stop)
