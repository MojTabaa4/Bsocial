from django.contrib import admin


@admin.register
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'date_of_birth', 'photo']
