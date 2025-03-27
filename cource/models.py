from django.db import models


class Teacher(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    role = models.CharField(max_length=255, verbose_name='Роль')
    image = models.ImageField(max_length=255, verbose_name='Фотография')

    def __str__(self):
        return self.full_name


class Classes(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Учитель", related_name="classes")
    name = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фотография')
    price = models.IntegerField(verbose_name='Цена')
    age = models.CharField(max_length=50, verbose_name='Возраст')
    time = models.CharField(max_length=50, verbose_name='Время')
    capacity = models.IntegerField(verbose_name='Вместимость')



    def __str__(self):
        return self.name
