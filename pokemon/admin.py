from django.contrib import admin
from .models import Pokemon


class PokemonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hp', 'active',
                    )
    list_filter = ('type', 'active')
    search_fields = ('name', 'name_fr', 'name_ar', 'name_jp')
    ordering = ('name',)
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {
            'fields': ('name', 'type', 'hp', 'active')
        }),
        ('Localizations', {
            'classes': ('collapse',),
            'fields': ('name_fr', 'name_ar', 'name_jp')
        }),
        ('Dates', {
            'classes': ('collapse',),
            'fields': ('created_at', 'modified_at')
        })
    )
    readonly_fields = ('created_at', 'modified_at')
    save_on_top = True
    save_as = True
    inlines = []
    filter_horizontal = ()
    prepopulated_fields = {}
    radio_fields = {}
    list_editable = ('active',)
    list_per_page = 25
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = True
    # ...

    # Register your models here.
admin.site.register(Pokemon, PokemonAdmin)
