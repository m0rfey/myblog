from django.contrib import admin
from django import forms

from menu.models import Menu, MenuItem

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    #fields = ['menu', 'order', 'link_url', 'title', 'login_required', 'anonymous_only']
    #filter_horizontal = ['menu']
    #filter_horizontal =['menu']
    ordering = ('order',)

class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline,]
    #fields = ['name', 'slug', 'base_url', 'description']


admin.site.register(Menu, MenuAdmin)
#admin.site.register(MenuItem, MenuItemInline)
