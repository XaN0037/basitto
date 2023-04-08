from django.contrib import admin

# from apps.dashboard.models.models import Banner
from apps.dashboard.models import *

# Register your models here.


"""Karniz IMG"""


class KarnizImgInline(admin.StackedInline):
    model = KarnizImg
    extra = 1

class KarnizColorImgInline(admin.StackedInline):
    model = KarnizColor
    extra = 1

class KarnizAdmin(admin.ModelAdmin):
    inlines = [KarnizImgInline,KarnizColorImgInline]


"""Kalso IMG"""


class KalsoImgInline(admin.StackedInline):
    model = KalsoImg
    extra = 1

class KalsoColorImgInline(admin.StackedInline):
    model = KalsoColor
    extra = 1

class KalsoAdmin(admin.ModelAdmin):
    inlines = [KalsoImgInline,KalsoColorImgInline]


"""Karona Img"""


class KaronaImgInline(admin.StackedInline):
    model = KaronaImg
    extra = 1

class KaronaColorImgInline(admin.StackedInline):
    model = KaronaColor
    extra = 1

class KaronaAdmin(admin.ModelAdmin):
    inlines = [KaronaImgInline,KaronaColorImgInline]


"""Noj"""


class NojaImgInline(admin.StackedInline):
    model = NojImg
    extra = 1

class NojColorImgInline(admin.StackedInline):
    model = NojColor
    extra = 1

class NojAdmin(admin.ModelAdmin):
    inlines = [NojaImgInline,NojColorImgInline]

    """bagget img"""


class BagetImgInline(admin.StackedInline):
    model = BagetImg
    extra = 1

class BagetColorImgInline(admin.StackedInline):
    model = BagetColor
    extra = 1

class BagetAdmin(admin.ModelAdmin):
    inlines = [BagetImgInline,BagetColorImgInline]


"""Dori Img"""


class DoriImgInline(admin.StackedInline):
    model = DoritImg
    extra = 1

class DoriColorImgInline(admin.StackedInline):
    model = Dori_Apparat_Color
    extra = 1

class DoriAdmin(admin.ModelAdmin):
    inlines = [DoriImgInline,DoriColorImgInline]


admin.site.register(SubCategory)
admin.site.register(Contacts)

admin.site.register(Karniz, KarnizAdmin)
admin.site.register(Kalso, KalsoAdmin)
admin.site.register(Karona, KaronaAdmin)
admin.site.register(Noj, NojAdmin)
admin.site.register(Baget, BagetAdmin)
admin.site.register(DoriAparat, DoriAdmin)
# admin.site.register(Discount)
admin.site.register(Banner)
