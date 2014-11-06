from django.contrib import admin
from mmdb.models import Person, Work, Relationship, RelationshipType


class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['person_first_name', 'person_last_name']}),
        (None, {'fields': ['person_birth_date']}),
    ]


class RelationshipTypeAdmin(admin.ModelAdmin):
    model = RelationshipType
    fieldsets = [
        (None, {'fields': ['rel_name']})
    ]


class RelationshipInline(admin.TabularInline):
    model = Relationship
    extra = 3


class WorkAdmin(admin.ModelAdmin):
    list_display = ['work_type', 'work_name', 'work_parent']
    inlines = [RelationshipInline]


admin.site.register(Person, PersonAdmin)
admin.site.register(RelationshipType, RelationshipTypeAdmin)
admin.site.register(Work, WorkAdmin)
