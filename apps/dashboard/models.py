from django.db import models


# Create your models here.


class SubCategory(models.Model):
    content = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    type = models.IntegerField(choices=[
        (1, 'karniz'),
        (2, 'kalso'),
        (3, 'karona'),
        (4, 'noj'),
        (5, 'baget'),
        (6, 'dori_aparat'),
    ])

    def __str__(self):
        return f"{self.content}"

#
# class Product(models.Model):
#     name = models.CharField(max_length=128)
#     price = models.IntegerField()
#     brend = models.CharField(max_length=128)
#
#     class Meta:
#         abstract = True
#
#
# class Karniz(Product):
#     category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, limit_choices_to={
#         "type": 1
#     })
#     quantity = models.IntegerField()
#     razmer = models.CharField(max_length=128)
#     material = models.CharField(max_length=128)
#
#
# class Kalso(Product):
#     category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, limit_choices_to={
#         "type": 2
#     })
#     quantity = models.IntegerField()
#     razmer = models.CharField(max_length=128)
#     material = models.CharField(max_length=128)
#
