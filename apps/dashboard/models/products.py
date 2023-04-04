from django.db import models


# Create your models here.


class SubCategory(models.Model):
    content_uz = models.CharField(max_length=128)
    content_ru = models.CharField(max_length=128)
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
        return f"{self.content_uz} | {self.content_ru}"


class Product(models.Model):
    status = models.BooleanField(default=True)
    name_uz = models.CharField(max_length=128)
    name_ru = models.CharField(max_length=128)
    price = models.IntegerField()
    quantity = models.IntegerField()
    brend = models.CharField(max_length=128)
    made_in_uz = models.CharField(max_length=128)
    made_in_ru = models.CharField(max_length=128)
    material_uz = models.CharField(max_length=128)
    material_ru = models.CharField(max_length=128)
    size = models.CharField(max_length=128)
    weight = models.CharField(max_length=128)
    model_number = models.CharField(max_length=128)
    unit_measurements_uz = models.CharField(max_length=128)
    unit_measurements_ru = models.CharField(max_length=128)
    package_weighte = models.CharField(max_length=128)
    package_length_sm = models.CharField(max_length=128)
    package_heigt_sm = models.CharField(max_length=128)
    razmer = models.CharField(max_length=128)
    type_uz = models.CharField(max_length=128)
    type_ru = models.CharField(max_length=128)
    material = models.CharField(max_length=128)
    capacity = models.CharField(max_length=128)

    class Meta:
        abstract = True


"""Karniz"""


class Karniz(Product):
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, limit_choices_to={
        "type": 1
    })
    discount_price = models.IntegerField(null=True, blank=True)
    shaped_uz = models.CharField(max_length=128)
    shaped_ru = models.CharField(max_length=128)
    method_of_sale_uz = models.CharField(max_length=128)
    method_of_sale_ru = models.CharField(max_length=128)
    diameter_sm = models.CharField(max_length=128)
    length = models.CharField(max_length=128)
    characteristics_uz = models.CharField(max_length=128)
    characteristics_ru = models.CharField(max_length=128)
    description_uz = models.CharField(max_length=128)
    description_ru = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        if self.discount_price:
            self.status = False
        else:
            self.status = True
        return super(Karniz, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name_uz} | {self.name_ru}"


class KarnizImg(models.Model):
    img = models.ImageField()
    product = models.ForeignKey(Karniz, on_delete=models.CASCADE, null=True, related_name='images')


"""Kalso"""


class Kalso(Product):
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, limit_choices_to={
        "type": 2
    })
    discount_price = models.IntegerField(null=True, blank=True)

    material_uz = models.CharField(max_length=128)
    material_ru = models.CharField(max_length=128)
    style_uz = models.CharField(max_length=128)
    style_ru = models.CharField(max_length=128)
    Type_of_curtain_accessories_uz = models.CharField(max_length=128)
    Type_of_curtain_accessories_ru = models.CharField(max_length=128)
    diameter_sm = models.CharField(max_length=128)
    length = models.CharField(max_length=128)
    CN_uz = models.CharField(max_length=128)
    CN_ru = models.CharField(max_length=128)
    description_uz = models.CharField(max_length=128)
    description_ru = models.CharField(max_length=128)


    def save(self, *args, **kwargs):
        if self.discount_price:
            self.status = False
        else:self.status = True
        return super(Kalso, self).save(*args,**kwargs)

    def __str__(self):
        return f"{self.name_uz} | {self.name_ru}"


class KalsoImg(models.Model):
    img = models.ImageField()
    product = models.ForeignKey(Kalso, on_delete=models.CASCADE, null=True, related_name='images')


"""Karona"""


class Karona(Product):
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, limit_choices_to={
        "type": 3
    })
    discount_price = models.IntegerField(null=True, blank=True)
    Method_of_sale_uz = models.CharField(max_length=128)
    Method_of_sale_ru = models.CharField(max_length=128)
    diameter_sm = models.CharField(max_length=128)
    length = models.CharField(max_length=128)
    capacity = models.CharField(max_length=128)
    description_uz = models.CharField(max_length=128)
    description_ru = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        if self.discount_price:
            self.status = False
        else:
            self.status = True
        return super(Karona, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name_uz} | {self.name_ru}"


class KaronaImg(models.Model):
    img = models.ImageField()
    product = models.ForeignKey(Karona, on_delete=models.CASCADE, null=True, related_name='images')


class Noj(Product):
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, limit_choices_to={
        "type": 4
    })
    discount_price = models.IntegerField(null=True, blank=True)
    individual_production = models.CharField(max_length=128)
    certification_uz = models.CharField(max_length=128)
    certification_ru = models.CharField(max_length=128)
    diameter_sm = models.CharField(max_length=128)
    length = models.CharField(max_length=128)
    weight = models.CharField(max_length=128)
    appropriate_curtain_type = models.CharField(max_length=128)
    style_uzstyle_uz = models.CharField(max_length=128)
    style_ru = models.CharField(max_length=128)
    description_uz = models.CharField(max_length=128)
    description_ru = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        if self.discount_price:
            self.status = False
        else:
            self.status = True
        return super(Noj, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name_uz} | {self.name_ru}"

    # def __str__(self):
    #     return {self.name_uz, self.name_ru}


class NojImg(models.Model):
    img = models.ImageField()
    product = models.ForeignKey(Noj, on_delete=models.CASCADE, null=True, related_name='images')


class Baget(Product):
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, limit_choices_to={
        "type": 5
    })
    discount_price = models.IntegerField(null=True, blank=True)
    row = models.CharField(max_length=128)
    length = models.CharField(max_length=128)
    cornice_width = models.CharField(max_length=128)
    baguette_width = models.CharField(max_length=128)
    cornice_type_uz = models.CharField(max_length=128)
    cornice_type_ru = models.CharField(max_length=128)
    suspension_type_uz = models.CharField(max_length=128)
    suspension_type_ru = models.CharField(max_length=128)
    tip_uz = models.CharField(max_length=128)
    tip_ru = models.CharField(max_length=128)
    weight = models.CharField(max_length=128)
    rotation_uz = models.CharField(max_length=128)
    rotation_ru = models.CharField(max_length=128)
    completely_finished_uz = models.CharField(max_length=128)
    completely_finished_ru = models.CharField(max_length=128)
    cover_uz = models.CharField(max_length=128)
    cover_ru = models.CharField(max_length=128)
    description_uz = models.CharField(max_length=128)
    description_ru = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        if self.discount_price:
            self.status = False
        else:
            self.status = True
        return super(Baget, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name_uz} | {self.name_ru}"


class BagetImg(models.Model):
    img = models.ImageField()
    product = models.ForeignKey(Baget, on_delete=models.CASCADE, null=True, related_name='images')


"""Dori apparat"""


class DoriAparat(Product):
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, limit_choices_to={
        "type": 6
    })
    discount_price = models.IntegerField(null=True, blank=True)
    the_length_of_the_sprayer_uz = models.CharField(max_length=128)
    the_length_of_the_sprayer_ru = models.CharField(max_length=128)
    hose_length_uz = models.CharField(max_length=128)
    hose_length_ru = models.CharField(max_length=128)
    total_weight_uz = models.CharField(max_length=128)
    total_weight_ru = models.CharField(max_length=128)
    container_capacity_uz = models.CharField(max_length=128)
    container_capacity_ru = models.CharField(max_length=128)
    work_expenses_uz = models.CharField(max_length=128)
    work_expenses_ru = models.CharField(max_length=128)
    adjusting_the_sprayer_uz = models.CharField(max_length=128)
    adjusting_the_sprayer_ru = models.CharField(max_length=128)
    status_uz = models.CharField(max_length=128)
    status_ru = models.CharField(max_length=128)
    how_to_transport_the_sprayer_uz = models.CharField(max_length=128)
    how_to_transport_the_sprayer_ru = models.CharField(max_length=128)
    spray_type_uz = models.CharField(max_length=128)
    spray_type_ru = models.CharField(max_length=128)
    description_uz = models.CharField(max_length=128)
    description_ru = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        if self.discount_price:
            self.status = False
        else:
            self.status = True
        return super(DoriAparat, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name_uz} | {self.name_ru}"


class DoritImg(models.Model):
    img = models.ImageField()
    product = models.ForeignKey(DoriAparat, on_delete=models.CASCADE, null=True, related_name='images')
