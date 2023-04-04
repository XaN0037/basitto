from django.db import models

from apps.api.models import User
from .products import *


#
#
class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    product_subctg_id = models.IntegerField()
    quantity = models.IntegerField(default=1)
    summa = models.IntegerField(blank=True, default=0)
    updated_dt = models.DateTimeField(auto_now_add=False, auto_now=True)
    create_dt = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False)


# class Prosaved(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product_id = models.IntegerField()
#     product_subctg_id = models.IntegerField()
#     updated_dt = models.DateTimeField(auto_now_add=False, auto_now=True)
#     create_dt = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    product_subctg_id = models.IntegerField()
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

#
# class Discount(models.Model):
#     karniz = models.ForeignKey(Karniz, blank=True, null=True, on_delete=models.CASCADE)
#     kalso = models.ForeignKey(Kalso, blank=True, null=True, on_delete=models.CASCADE)
#     baget = models.ForeignKey(Baget, blank=True, null=True, on_delete=models.CASCADE)
#     karona = models.ForeignKey(Karona, blank=True, null=True, on_delete=models.CASCADE)
#     noj = models.ForeignKey(Noj, blank=True, null=True, on_delete=models.CASCADE)
#     dori_apparat = models.ForeignKey(DoriAparat, blank=True, null=True, on_delete=models.CASCADE)
#
#     procent = models.IntegerField(blank=True, null=True, default=0)
#     price = models.IntegerField()
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#
#     def __str__(self):
#         s = ''
#         if self.karona:
#             s += "self.karona.name , "
#         if self.kalso:
#             s += "self.kalso.name , "
#         if self.baget:
#             s += "self.baget.name, "
#         if self.karona:
#             s += "self.karona.name, "
#         if self.noj:
#             s += "self.noj.name ,"
#         if self.dori_apparat:
#             s += "self.dori_apparat.name ,"
#         return f"{s}"
#
# #     def __str__(self):
# #         return f"{self.product.name}"
# # #
# #     def save(self, *args, **kwargs):
# #         product =''
# #         ctg = SubCategory.objects.filter(pk=self.product_subctg_id).first()
# #         if ctg.type == 1:
# #             product =Karniz.objects.filter(pk=self.product_id).first()
# #         elif ctg.type == 2:
# #             product = Kalso.objects.filter(pk=self.product_id).first()
# #         elif ctg.type == 3:
# #             product = Karona.objects.filter(pk=self.product_id).first()
# #         elif ctg.type == 4:
# #             product = Noj.objects.filter(pk=self.product_id).first()
# #         elif ctg.type == 5:
# #             product = Baget.objects.filter(pk=self.product_id).first()
# #         elif ctg.type == 6:
# #             product = DoriAparat.objects.filter(pk=self.product_id).first()
# #         product.status = False
# #
# #
# #         self.procent = (self.price / self.product.price) * 100
# #         print("\n", self.procent, '\n')
# #         return super(Discount, self).save(*args, **kwargs)
# # #
# # #     def __str__(self):
# # #         product = ''
# # #         ctg = SubCategory.objects.filter(pk=self.product_subctg_id).first()
# # #         print('\n','bu ctg',ctg,'\n')
# # #         if ctg.type == 1:
# # #             product = Karniz.objects.filter(pk=self.product_id).first()
# # #         elif ctg.type == 2:
# # #             product = Kalso.objects.filter(pk=self.product_id).first()
# # #         elif ctg.type == 3:
# # #             product = Karona.objects.filter(pk=self.product_id).first()
# # #         elif ctg.type == 4:
# # #             product = Noj.objects.filter(pk=self.product_id).first()
# # #         elif ctg.type == 5:
# # #             product = Baget.objects.filter(pk=self.product_id).first()
# # #         elif ctg.type == 6:
# # #             product = DoriAparat.objects.filter(pk=self.product_id).first()
# # #
# # #         return f"{product.name_uz}"
