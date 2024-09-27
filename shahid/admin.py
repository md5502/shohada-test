import uuid

from django.contrib import admin
from django.utils.text import slugify

from .models import Shahid


class ShahidAdmin(admin.ModelAdmin):
    list_display = ("name", "lname", "martyrdom_location", "martyrdom_date", "slug", "qr_code_image")

    # Do not display 'slug' in the form, it will be generated automatically
    exclude = ("slug",)

    readonly_fields = ("qr_code_image",)

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(f" {str(uuid.uuid4()).split("-")[0]} {obj.name} {obj.lname} ",allow_unicode=True)
        super().save_model(request, obj, form, change)


# Register the Shahid model and the ShahidAdmin class
admin.site.register(Shahid, ShahidAdmin)
