from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Post
from .models import ViewsSummary

admin.site.register(Post)
admin.site.register(ViewsSummary)

class SaleSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/view_summary_change_list.html'
    date_hierarchy = 'created'

