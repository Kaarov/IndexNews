from django.contrib import admin
from django.db.models import QuerySet
from news.models import *


@admin.register(AboutService)
class AboutServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'active', 'image', 'description', ]
    list_display_links = ['title', ]
    list_per_page = 5
    search_fields = ['title', ]
    ordering = ['-id', ]

    def has_change_permission(self, request, obj=None):
        return False


class SloganItemsAdmin(admin.TabularInline):
    model = SloganItems
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Slogan)
class SloganAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'active']
    list_display_links = ['title', ]
    list_per_page = 10
    search_fields = ['title', ]
    inlines = [SloganItemsAdmin]

    def has_delete_permission(self, request, obj=None):
        return False


class AboutUsItemsAdmin(admin.TabularInline):
    model = AboutUsItems
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'active']
    list_display_links = ['title', ]
    list_per_page = 10
    search_fields = ['title', ]
    inlines = [AboutUsItemsAdmin]

    def has_delete_permission(self, request, obj=None):
        return False


class ServicesItemsAdmin(admin.TabularInline):
    model = ServicesItems
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'active']
    list_display_links = ['title', ]
    list_per_page = 10
    search_fields = ['title', ]
    inlines = [ServicesItemsAdmin]

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'active']
    list_display_links = ['title', ]
    list_per_page = 10
    search_fields = ['title', ]


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'active']
    list_display_links = ['title', ]
    list_per_page = 15
    search_fields = ['title', ]


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'active', 'image', 'description', 'created', ]
    list_display_links = ['title', ]
    list_per_page = 10
    search_fields = ['title', ]


@admin.register(PhoneNumbers)
class PhoneNumbersAdmin(admin.ModelAdmin):
    list_display = ['id', 'phonenumber', 'active']
    list_display_links = ['phonenumber', ]
    list_per_page = 15
    search_fields = ['phonenumber', ]


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['id', 'gmail', 'active', 'address', ]
    list_display_links = ['gmail', ]
    list_per_page = 15
    search_fields = ['gmail', ]


