from django.contrib import admin
from django.utils.html import format_html
from .models import Course, Student, Teacher


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'level', 'duration', 'is_active', 'display_image')
    list_filter = ('level', 'is_active', 'price')
    search_fields = ('title', 'description')
    list_editable = ('price', 'is_active')
    readonly_fields = ('display_image',)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="60" style="object-fit: cover;" />', obj.image.url)
        return "Нет изображения"

    display_image.short_description = 'Изображение'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age', 'phone', 'email', 'course', 'registered_at')
    list_filter = ('course', 'age', 'registered_at')
    search_fields = ('name', 'surname', 'email', 'phone')
    readonly_fields = ('registered_at',)
    date_hierarchy = 'registered_at'

    def full_name(self, obj):
        return f"{obj.name} {obj.surname}"

    full_name.short_description = 'ФИО'


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialty', 'experience', 'display_photo')
    list_filter = ('specialty', 'experience')
    search_fields = ('name', 'surname', 'specialty')
    readonly_fields = ('display_photo',)

    def full_name(self, obj):
        return f"{obj.name} {obj.surname}"

    full_name.short_description = 'ФИО'

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="80" height="80" style="object-fit: cover; border-radius: 50%;" />',
                               obj.photo.url)
        return "Нет фото"

    display_photo.short_description = 'Фото'



class OkurmenKidsAdminSite(admin.AdminSite):
    site_header = "Okurmen Kids Administration"
    site_title = "Okurmen Kids Admin Portal"
    index_title = "Добро пожаловать в систему управления"

    def index(self, request, extra_context=None):

        from django.db.models import Count
        extra_context = extra_context or {}

        stats = {
            'total_courses': Course.objects.count(),
            'active_courses': Course.objects.filter(is_active=True).count(),
            'total_students': Student.objects.count(),
            'total_teachers': Teacher.objects.count(),
            'recent_students': Student.objects.order_by('-registered_at')[:5],
            'courses_by_level': Course.objects.values('level').annotate(count=Count('id'))
        }

        extra_context['stats'] = stats
        return super().index(request, extra_context)

