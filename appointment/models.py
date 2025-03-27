from django.db import models

class Appointment(models.Model):
    guardian_name = models.CharField(
        max_length=255,
        verbose_name='Имя родителя'
    )
    guardian_email = models.EmailField(
        verbose_name='Email родителя'
    )
    child_name = models.CharField(
        max_length=255,
        verbose_name='Имя ребенка'
    )
    child_age = models.PositiveIntegerField(
        verbose_name='Возраст ребенка'
    )
    message = models.TextField(
        verbose_name='Сообщение родителя'
    )

    def __str__(self):
        return f'{self.guardian_name} - {self.child_name}'

    class Meta:
        verbose_name = 'Запись на приём'
        verbose_name_plural = 'Записи на приёмы'


class Review(models.Model):
    client_image = models.ImageField(
        verbose_name='Фотография клиента',
        upload_to='client_image/'
    )
    client_name = models.CharField(
        verbose_name='ФИО клиента',
        max_length=255
    )
    role = models.CharField(
        verbose_name='Профессия клиента',
        max_length=255
    )
    text = models.TextField(
        verbose_name='Отзыв'
    )