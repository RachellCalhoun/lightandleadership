from django.contrib import admin

from .models import (
    OurStory, OurTeam, EduProgram, EthicalPost, VolunteerPeru, VolunteerOpenPosition,
    VolunteerAbout, CustomPage, Home, FooterInfo, DonateSection, Menu, SubMenu, HomeLink,
    Apply
)
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE


class OurStoryAdmin(admin.ModelAdmin):
    fields = ['order', 'img', 'text', 'color']
    list_display=('order','img','text', 'color')

class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','order','color','img','text')
    list_editable = ('order',)

class OurTeamAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'img', 'peru_team', 'us_team', 'board_team']
    list_display = ('title', 'peru_team', 'us_team', 'board_team')

class EduProgramAdmin(admin.ModelAdmin):
    fields = ['row_style', 'category', 'order', 'title', 'img', 'color', 'text']
    list_display = ('id', 'category', 'order','title','row_style')
    list_editable = ('row_style', 'order')
    list_filter = ['category']


class EthicalPostAdmin(admin.ModelAdmin):
    fields = ['order', 'title', 'img', 'text']
    list_display = ('order', 'title' )

class MCEFlatPageForm(FlatpageForm):

    class Meta:
        model = FlatPage
        widgets = {
            'content' : TinyMCE(attrs={'cols': 100, 'rows': 15}),
        }
        exclude = []


class MCEFlatPageAdmin(FlatPageAdmin):
    form = MCEFlatPageForm


class VolunteerPeruAdmin(admin.ModelAdmin):
    fields = ['category', 'order', 'color', 'title', 'img', 'text']
    list_display = ('id', 'category', 'order','title')
    list_editable = ('order',)
    list_filter = ('category', )

class VolunteerOpenPositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')

class VolunteerAboutAdmin(admin.ModelAdmin):
    list_display = ('order', 'title' )

class CustomPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'order','title')
    list_editable = ('order',)
    list_filter = ('category',)


class DonateSectionAdmin(admin.ModelAdmin):
    fields = ['category', 'order', 'color', 'title', 'img', 'text', 'paypal_button']
    list_display = ('id', 'category', 'order', 'title')
    list_editable = ('order',)
    list_filter = ('category',)

class SubMenuInline(admin.TabularInline):
    model = SubMenu
    extra = 3

class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    fieldsets = [(None, {'fields': ['title', 'order']}), ]
    inlines = [SubMenuInline]

class HomeLinkAdmin(admin.ModelAdmin):
    list_display = ('order','title', 'color')

class ApplyAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')

admin.site.register(Apply, ApplyAdmin)
admin.site.register(OurStory, OurStoryAdmin)
admin.site.register(OurTeam, OurTeamAdmin)
admin.site.register(EduProgram, EduProgramAdmin)
admin.site.register(EthicalPost, EthicalPostAdmin)
admin.site.register(VolunteerAbout, VolunteerAboutAdmin)
admin.site.register(VolunteerPeru, VolunteerPeruAdmin)
admin.site.register(VolunteerOpenPosition, VolunteerOpenPositionAdmin)
admin.site.register(CustomPage, CustomPageAdmin)
admin.site.register(Home, HomeAdmin)
admin.site.register(FooterInfo)
admin.site.register(DonateSection, DonateSectionAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(HomeLink, HomeLinkAdmin)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, MCEFlatPageAdmin)
