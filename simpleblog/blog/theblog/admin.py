from django.contrib import admin

# Register your models here.
from .models import Post, Category, Profile, Banner, BgImg

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Banner)
admin.site.register(BgImg)

