from django.contrib import admin
# 게시글(Post) Model을 불러옵니다
from .models import Post, Photo, Comment

# Register your models here.

# Photo 클래스를 inline으로 나타낸다.
class PhotoInline(admin.TabularInline):
    model = Photo

# Post 클래스는 해당하는 Photo 객체를 리스트로 관리하는 한다. 
class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]

# 관리자(admin)가 게시글(Post)에 접근 가능
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)