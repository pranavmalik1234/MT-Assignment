from django.contrib import admin
from .models import user_score,levels,tests,extendeduser

class Testsadmin(admin.ModelAdmin):
    readonly_fields=('created',)

# Register your models here.
admin.site.register(user_score)
admin.site.register(levels)
admin.site.register(tests)
admin.site.register(extendeduser)
