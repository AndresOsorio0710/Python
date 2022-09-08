from django.contrib import admin


class PersonAdmin(admin.ModelAdmin):
    search_fields = ["phone_number","email","firts_name","last_name"]
    list_display = ["last_name","first_name","email","gender"]
    list_filter = ["gender"]
    list_per_page = 10