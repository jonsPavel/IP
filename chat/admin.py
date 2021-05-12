from chat.models import MyBanner
from django.contrib import admin


class MyBannerAdmin(admin.ModelAdmin):
    fields=['id','path','url','cover']
    list_filter=['id']

admin.site.register(MyBanner,MyBannerAdmin)