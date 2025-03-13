from django.db import models

# Create your models here.

class ObjemLS(models.Model):
    title = models.CharField(max_length=100, verbose_name='Обьем и лс')

    def __str__(self):
        return self.title

class Cvet(models.Model):
    title = models.CharField(max_length=100, verbose_name='Цвет')

    def __str__(self):
        return self.title

class Comp(models.Model):
    title = models.CharField(max_length=100, verbose_name='Комплектация')

    def __str__(self):
        return self.title

class Cars(models.Model):
    title = models.CharField(max_length=100, verbose_name='Модель')
    cvet = models.ForeignKey(to=Cvet,  verbose_name='Цвет', on_delete=models.CASCADE)
    objemLS = models.ForeignKey(to=ObjemLS, verbose_name='Обьем и лс', on_delete=models.CASCADE)
    comp = models.ForeignKey(to=Comp, verbose_name='Комплектация', on_delete=models.CASCADE)
    foto = models.FileField(verbose_name='Фото',upload_to='cars/', null=True, blank=True)
    year = models.IntegerField(verbose_name='Год')
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return self.title

class Users(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя клиента')
    telephone = models.IntegerField(verbose_name='Номер телефона')
    comment = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        return self.name