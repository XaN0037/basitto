# from django.db import models
#
# from apps.api.models import User
# from .products import Product
#
#
#
# class Basket(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     summa = models.IntegerField(blank=True, default=0)
#     # img = models.ImageField()
#     # serializer exclude ichida turadi, items ichiga tiqmisila
#     updated_dt = models.DateTimeField(auto_now_add=False, auto_now=True)
#     create_dt = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False)
#
#     def save(self, *args, **kwargs):
#         self.summa = self.product.price * self.quantity
#         return super(Basket, self).save(*args, **kwargs)
#
#
# class Prosaved(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     updated_dt = models.DateTimeField(auto_now_add=False, auto_now=True)
#     create_dt = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False)
#
#     def __str__(self):
#         return f"{self.product.name}"
#
#
# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     text = models.TextField(max_length=1024)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return str(self.text)[:30]
#
#
# class Like(models.Model):
#     commentary = models.ForeignKey(Comment, related_name="like", on_delete=models.CASCADE)
#     like = models.BooleanField(default=False)
#     dislike = models.BooleanField(default=False)
#     user = models.ForeignKey(User, related_name='requirement_comment_likes', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#
# class Banner(models.Model):
#     name = models.CharField(max_length=128)
#     image = models.ImageField(upload_to='banner')
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class Discount(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     procent = models.IntegerField(blank=True, null=True, default=0)
#     price = models.IntegerField()
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#
#     def __str__(self):
#         return f"{self.product.name}"
#
#     def save(self, *args, **kwargs):
#         self.procent = (self.price / self.product.price) * 100
#         print("\n", self.procent, '\n')
#         return super(Discount, self).save(*args, **kwargs)
