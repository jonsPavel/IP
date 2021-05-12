from django.db import models


# class Banner(models.Model):
#     title = models.CharField(max_length=150)
#     cover = models.ImageField(upload_to='images/')
#     book = models.FileField(upload_to='banners/')
#
#     def __str__(self):
#         return self.title

class MyBanner(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    path = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='images/',verbose_name='Изображение')

    def __str__(self):
        return self.id