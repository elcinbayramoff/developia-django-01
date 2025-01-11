from django.contrib import admin
from .models import Task, Category
# Register your models here.

# admin.site.register([Task,Category])

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','title','description', 'category','deadline', 'status', 'created_at', 'updated_at')
    list_editable = ('status',)
    list_filter = ('category', 'deadline')
    search_fields = ('title','description')
    ordering = ('title',)
    # readonly_fields = ('deadline',)
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...