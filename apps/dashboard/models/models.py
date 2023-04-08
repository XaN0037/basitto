from django.db import models

from apps.api.models import User
from .products import *



class Contacts(models.Model):
    phone = models.CharField(max_length=128)
    phone2 = models.CharField(max_length=128, blank=True, null=True)
    phone3 = models.CharField(max_length=128, blank=True, null=True)
    phone4 = models.CharField(max_length=128, blank=True, null=True)
    phone5 = models.CharField(max_length=128, blank=True, null=True)
    facebook = models.CharField(max_length=128, blank=True, null=True)
    instagram = models.CharField(max_length=128, blank=True, null=True)
    telegram = models.CharField(max_length=128, blank=True, null=True)
    youtube = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return f"{self.phone}"


#
class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    product_subctg_id = models.IntegerField()
    quantity = models.IntegerField(default=1)
    summa = models.IntegerField(blank=True, default=0)
    updated_dt = models.DateTimeField(auto_now_add=False, auto_now=True)
    create_dt = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False)


class Prosaved(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    subctg_id = models.IntegerField()
    updated_dt = models.DateTimeField(auto_now_add=False, auto_now=True)
    create_dt = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    subctg_id = models.IntegerField()
    text = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.text)[:30]


class Like(models.Model):
    commentary = models.ForeignKey(Comment, related_name="like", on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='requirement_comment_likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Banner(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='banner')

    def __str__(self):
        return f"{self.name}"
