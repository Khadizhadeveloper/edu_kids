from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Course, Student, Teacher
from .forms import StudentForm


def home(request):
    courses = Course.objects.filter(is_active=True)
    teachers = Teacher.objects.all()
    return render(request, 'main/home.html', {
        'courses': courses,
        'teachers': teachers
    })


def courses(request):
    courses = Course.objects.filter(is_active=True)
    return render(request, 'main/courses.html', {'courses': courses})


def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'main/teachers.html', {'teachers': teachers})


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = StudentForm()

    return render(request, 'main/contact.html', {'form': form})


def success(request):
    return render(request, 'main/success.html')


def api_courses(request):
    courses = Course.objects.filter(is_active=True)
    data = [
        {
            'id': course.id,
            'title': course.title,
            'description': course.description,
            'price': float(course.price),
            'level': course.get_level_display(),
            'image': course.image.url if course.image else None
        }
        for course in courses
    ]
    return JsonResponse(data, safe=False)