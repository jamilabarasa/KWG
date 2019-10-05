from django.contrib import admin
from .models import Member,New,Comment,Burial
# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display=('name','category','date_joined','idno')
    list_filter=('category','date_joined')
    search_fields=('name','contact','idno')

admin.site.register(New)
admin.site.register(Burial)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','body','created','updated')
    list_filter = ('created','updated')
    search_fields = ('post',)
