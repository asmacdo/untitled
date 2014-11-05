from django.contrib import admin
from mmdb.models import Person, Work, Relationship


class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['person_first_name', 'person_last_name']}),
        (None, {'fields': ['person_birth_date']}),
    ]


class RelationshipInline(admin.TabularInline):
    model = Relationship
    extra = 3


class WorkAdmin(admin.ModelAdmin):
    fields = ['work_name', 'work_type', 'work_parent']
    inlines = [RelationshipInline]


admin.site.register(Person, PersonAdmin)
admin.site.register(Work, WorkAdmin)
