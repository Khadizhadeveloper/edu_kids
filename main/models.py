from django.db import models


class Course(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Начинающий'),
        ('intermediate', 'Средний'),
        ('advanced', 'Продвинутый'),
    ]

    title = models.CharField(max_length=200, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание')
    duration = models.CharField(max_length=100, verbose_name='Длительность')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, verbose_name='Уровень')
    image = models.ImageField(upload_to='courses/', verbose_name='Изображение')
    is_active = models.BooleanField(default=True, verbose_name='Активный')

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    registered_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return f"{self.name} {self.surname}"


class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    specialty = models.CharField(max_length=200, verbose_name='Специализация')
    experience = models.IntegerField(verbose_name='Опыт работы (лет)')
    photo = models.ImageField(upload_to='teachers/', verbose_name='Фото')

    def __str__(self):
        return f"{self.name} {self.surname}"