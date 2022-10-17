from django.contrib import admin
from .models import Movies, Comments
from django.utils.safestring import mark_safe

# Register your models here.
# login: addmin
# password: 1234minda8
admin.site.register(Comments)

admin.site.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ['title', 'photo', 'rating', 'release_date', 'age_rest', 'directory', 'article']

    def image_show(self, obj):
        if obj.photo:
            return mark_safe("<img src = '{}' width = '60' />".format(obj.photo.url))
        return "None"

    image_show.__name__ = "Picture"
