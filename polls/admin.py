from django.contrib import admin

# Register your models here.

from polls.models import Poll


__author__ = 'smuravko'


class PollAdmin(admin.ModelAdmin):
    pass
    # list_display = ('first_name', 'last_name', 'email', 'max_request_count',
    #                 'request_count', )


admin.site.register(Poll, PollAdmin)
