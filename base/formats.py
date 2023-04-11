from collections import OrderedDict

from apps.dashboard.models import *

from src.settings import MEDIA_URL


def format(data=None):
    return OrderedDict([
        ('id', data.id),
        ('name', data.name),
        ('email', data.email),
        ('mobile', data.mobile),
    ])


def subcategory_format(data=None):


    ctg_type = {
        1: 'karniz',
        2: 'kalso',
        3: 'karona',
        4: 'noj',
        5: 'baget',
        6: 'dori_aparat'
    }
    return OrderedDict([
        ('id', data.id),
        ('content_uz', data.content_uz),
        ('content_ru', data.content_ru),
        ('slug', data.slug),
        ('type', ctg_type[data.type])
    ])



def colorformat(data):
    return OrderedDict([
        ('id', data.id),
        ('name_uz', data.name_uz),
        ('name_ru', data.name_ru),
        ('img', data.img.url),
    ])


def karniz_format(data=None):
    images = KarnizImg.objects.select_related('product').filter(product=data)
    colors = KarnizColor.objects.select_related('product').filter(product=data)
    image = []
    for i in images:
        image.append({
            "img": "" if not i.img else i.img.url,
        })

    color = []
    for i in colors:
        color.append({
            "color": "" if not i.img else colorformat(i),
        })
    return OrderedDict([
        ('sub_ctg', None if not data.category else subcategory_format(data.category)),
        ('prod_id', data.id),
        ('status', data.status),
        ('name_uz', data.name_uz),
        ('name_ru', data.name_ru),
        ('price', data.price),
        ('discount_price', data.discount_price),
        ('brend', data.brend),


        ('quantity', data.quantity),
        ('made_in_uz', data.made_in_uz),
        ('made_in_ru', data.made_in_ru),
        ('material_uz', data.material_uz),
        ('material_ru', data.material_ru),
        ('size', data.size),
        ('weight', data.weight),
        ('model_number', data.model_number),
        ('unit_measurements_uz', data.unit_measurements_uz),
        ('unit_measurements_ru', data.unit_measurements_ru),
        ('package_weighte', data.package_weighte),
        ('package_length_sm', data.package_length_sm),
        ('package_heigt_sm', data.package_heigt_sm),
        ('razmer', data.razmer),
        ('type_uz', data.type_uz),
        ('type_ru', data.type_ru),
        ('material', data.material),
        ('capacity', data.capacity),

        ('shaped_uz', data.shaped_uz),
        ('shaped_ru', data.shaped_ru),
        ('method_of_sale_uz', data.method_of_sale_uz),
        ('method_of_sale_ru', data.method_of_sale_ru),
        ('diameter_sm', data.diameter_sm),
        ('length', data.length),
        ('characteristics_uz', data.characteristics_uz),
        ('characteristics_ru', data.characteristics_ru),

        ('description_uz', data.description_uz),
        ('description_ru', data.description_ru),

        ('img', image),
        ('color', color),


    ])


def kalso_format(data=None):
    images = KalsoImg.objects.select_related('product').filter(product=data)
    colors = KalsoColor.objects.select_related('product').filter(product=data)
    color = []
    for i in colors:
        color.append({
            "color": "" if not i.img else colorformat(i),
        })
    image = []
    for i in images:
        image.append({
            "img": "" if not i.img else i.img.url,
        })

    return OrderedDict([
        ('prod_id', data.id),
        ('sub_ctg', None if not data.category else subcategory_format(data.category)),
        ('status', data.status),
        ('brend', data.brend),

        ('name_uz', data.name_uz),
        ('name_ru', data.name_ru),
        ('price', data.price),
        ('discount_price', data.discount_price),
        ('quantity', data.quantity),
        ('made_in_uz', data.made_in_uz),
        ('made_in_ru', data.made_in_ru),
        ('material_uz', data.material_uz),
        ('material_ru', data.material_ru),
        ('size', data.size),
        ('weight', data.weight),
        ('model_number', data.model_number),
        ('unit_measurements_uz', data.unit_measurements_uz),
        ('unit_measurements_ru', data.unit_measurements_ru),
        ('package_weighte', data.package_weighte),
        ('package_length_sm', data.package_length_sm),
        ('package_heigt_sm', data.package_heigt_sm),
        ('razmer', data.razmer),
        ('type_uz', data.type_uz),
        ('type_ru', data.type_ru),
        ('material', data.material),
        ('capacity', data.capacity),

        ('material_uz', data.material_uz),
        ('material_ru', data.material_ru),
        ('style_uz', data.style_uz),
        ('style_ru', data.style_ru),
        ('Type_of_curtain_accessories_uz', data.Type_of_curtain_accessories_uz),
        ('Type_of_curtain_accessories_ru', data.Type_of_curtain_accessories_ru),
        ('diameter_sm', data.diameter_sm),
        ('length', data.length),
        ('CN_uz', data.CN_uz),
        ('CN_ru', data.CN_ru),
        ('description_uz', data.description_uz),
        ('description_ru', data.description_ru),

        ('img', image),
        ('color', color)


    ])


def karona_format(data=None):
    images = KaronaImg.objects.select_related('product').filter(product=data)
    colors = KaronaColor.objects.select_related('product').filter(product=data)
    image = []
    for i in images:
        image.append({
            "img": "" if not i.img else i.img.url,
        })
    color = []
    for i in colors:
        color.append({
            "color": "" if not i.img else colorformat(i),
        })



    return OrderedDict([
        ('sub_ctg', None if not data.category else subcategory_format(data.category)),
        ('prod_id', data.id),

        ('status', data.status),
        ('name_uz', data.name_uz),
        ('name_ru', data.name_ru),
        ('price', data.price),
        ('brend', data.brend),

        ('discount_price', data.discount_price),
        ('quantity', data.quantity),
        ('made_in_uz', data.made_in_uz),
        ('made_in_ru', data.made_in_ru),
        ('material_uz', data.material_uz),
        ('material_ru', data.material_ru),
        ('size', data.size),
        ('weight', data.weight),
        ('model_number', data.model_number),
        ('unit_measurements_uz', data.unit_measurements_uz),
        ('unit_measurements_ru', data.unit_measurements_ru),
        ('package_weighte', data.package_weighte),
        ('package_length_sm', data.package_length_sm),
        ('package_heigt_sm', data.package_heigt_sm),
        ('razmer', data.razmer),
        ('type_uz', data.type_uz),
        ('type_ru', data.type_ru),
        ('material', data.material),
        ('capacity', data.capacity),

        ('Method_of_sale_uz', data.Method_of_sale_uz),
        ('Method_of_sale_ru', data.Method_of_sale_ru),
        ('diameter_sm', data.diameter_sm),
        ('length', data.length),
        ('capacity', data.capacity),

        ('description_uz', data.description_uz),
        ('description_ru', data.description_ru),
        ('img', image),
        ('color', color),

    ])


def noj_format(data=None):
    images = NojImg.objects.select_related('product').filter(product=data)
    colors = NojColor.objects.select_related('product').filter(product=data)
    image = []
    for i in images:
        image.append({
            "img": "" if not i.img else i.img.url,
        })
    color = []
    for i in colors:
        color.append({
            "color": "" if not i.img else colorformat(i),
        })


    return OrderedDict([
        ('sub_ctg', None if not data.category else subcategory_format(data.category)),
        ('prod_id', data.id),
        ('status', data.status),
        ('name_uz', data.name_uz),
        ('name_ru', data.name_ru),
        ('price', data.price),
        ('brend', data.brend),

        ('quantity', data.quantity),
        ('discount_price', data.discount_price),
        ('made_in_uz', data.made_in_uz),
        ('made_in_ru', data.made_in_ru),
        ('material_uz', data.material_uz),
        ('material_ru', data.material_ru),
        ('size', data.size),
        ('weight', data.weight),
        ('model_number', data.model_number),
        ('unit_measurements_uz', data.unit_measurements_uz),
        ('unit_measurements_ru', data.unit_measurements_ru),
        ('package_weighte', data.package_weighte),
        ('package_length_sm', data.package_length_sm),
        ('package_heigt_sm', data.package_heigt_sm),
        ('razmer', data.razmer),
        ('type_uz', data.type_uz),
        ('type_ru', data.type_ru),
        ('material', data.material),
        ('capacity', data.capacity),

        ('individual_production', data.individual_production),
        ('certification_uz', data.certification_uz),
        ('certification_ru', data.certification_ru),
        ('diameter_sm', data.diameter_sm),
        ('length', data.length),
        ('weight', data.weight),
        ('appropriate_curtain_type', data.appropriate_curtain_type),
        ('style_uzstyle_uz', data.style_uzstyle_uz),
        ('style_ru', data.style_ru),

        ('description_uz', data.description_uz),
        ('description_ru', data.description_ru),
        ('img', image),
        ('color', color),

    ])


def baget_format(data=None):
    images = BagetImg.objects.select_related('product').filter(product=data)
    colors = BagetColor.objects.select_related('product').filter(product=data)
    image = []
    color = []
    for i in colors:
        color.append({
            "color": "" if not i.img else colorformat(i),
        })
    for i in images:
        image.append({
            "img": "" if not i.img else i.img.url,
        })
    return OrderedDict([
        ('sub_ctg', None if not data.category else subcategory_format(data.category)),
        ('prod_id', data.id),
        ('status', data.status),
        ('name_uz', data.name_uz),
        ('name_ru', data.name_ru),
        ('price', data.price),
        ('brend', data.brend),

        ('discount_price', data.discount_price),
        ('quantity', data.quantity),
        ('made_in_uz', data.made_in_uz),
        ('made_in_ru', data.made_in_ru),
        ('material_uz', data.material_uz),
        ('material_ru', data.material_ru),
        ('size', data.size),
        ('weight', data.weight),
        ('model_number', data.model_number),
        ('unit_measurements_uz', data.unit_measurements_uz),
        ('unit_measurements_ru', data.unit_measurements_ru),
        ('package_weighte', data.package_weighte),
        ('package_length_sm', data.package_length_sm),
        ('package_heigt_sm', data.package_heigt_sm),
        ('razmer', data.razmer),
        ('type_uz', data.type_uz),
        ('type_ru', data.type_ru),
        ('material', data.material),
        ('capacity', data.capacity),

        ('row', data.row),
        ('length', data.length),
        ('cornice_width', data.cornice_width),
        ('baguette_width', data.baguette_width),
        ('cornice_type_uz', data.cornice_type_uz),
        ('cornice_type_ru', data.cornice_type_ru),
        ('suspension_type_uz', data.suspension_type_uz),
        ('suspension_type_ru', data.suspension_type_ru),
        ('tip_uz', data.tip_uz),
        ('tip_ru', data.tip_ru),
        ('weight', data.weight),
        ('rotation_uz', data.rotation_uz),
        ('rotation_ru', data.rotation_ru),
        ('completely_finished_uz', data.completely_finished_uz),
        ('completely_finished_ru', data.completely_finished_ru),
        ('cover_uz', data.cover_uz),
        ('cover_ru', data.cover_ru),

        ('description_uz', data.description_uz),
        ('description_ru', data.description_ru),
        ('img', image),
        ('color', color),

    ])


def dori_format(data=None):
    images = DoritImg.objects.select_related('product').filter(product=data)
    colors = Dori_Apparat_Color.objects.select_related('product').filter(product=data)
    image = []
    color = []
    for i in colors:
        color.append({
            "color": "" if not i.img else colorformat(i),
        })
    for i in images:
        image.append({
            "img": "" if not i.img else i.img.url,
        })

    return OrderedDict([
        ('sub_ctg', None if not data.category else subcategory_format(data.category)),
        ('prod_id', data.id),
        ('status', data.status),
        ('name_uz', data.name_uz),
        ('name_ru', data.name_ru),
        ('price', data.price),
        ('brend', data.brend),

        ('quantity', data.quantity),
        ('discount_price', data.discount_price),
        ('made_in_uz', data.made_in_uz),
        ('made_in_ru', data.made_in_ru),
        ('material_uz', data.material_uz),
        ('material_ru', data.material_ru),
        ('size', data.size),
        ('weight', data.weight),
        ('model_number', data.model_number),
        ('unit_measurements_uz', data.unit_measurements_uz),
        ('unit_measurements_ru', data.unit_measurements_ru),
        ('package_weighte', data.package_weighte),
        ('package_length_sm', data.package_length_sm),
        ('package_heigt_sm', data.package_heigt_sm),
        ('razmer', data.razmer),
        ('type_uz', data.type_uz),
        ('type_ru', data.type_ru),
        ('material', data.material),
        ('capacity', data.capacity),

        ('the_length_of_the_sprayer_uz', data.the_length_of_the_sprayer_uz),
        ('the_length_of_the_sprayer_ru', data.the_length_of_the_sprayer_ru),
        ('hose_length_uz', data.hose_length_uz),
        ('hose_length_ru', data.hose_length_ru),
        ('total_weight_uz', data.total_weight_uz),
        ('total_weight_ru', data.total_weight_ru),
        ('container_capacity_uz', data.container_capacity_uz),
        ('container_capacity_ru', data.container_capacity_ru),
        ('work_expenses_uz', data.work_expenses_uz),
        ('work_expenses_ru', data.work_expenses_ru),
        ('adjusting_the_sprayer_uz', data.adjusting_the_sprayer_uz),
        ('adjusting_the_sprayer_ru', data.adjusting_the_sprayer_ru),
        ('status_uz', data.status_uz),
        ('status_ru', data.status_ru),
        ('how_to_transport_the_sprayer_uz', data.how_to_transport_the_sprayer_uz),
        ('how_to_transport_the_sprayer_ru', data.how_to_transport_the_sprayer_ru),
        ('spray_type_uz', data.spray_type_uz),
        ('spray_type_ru', data.spray_type_ru),

        ('description_uz', data.description_uz),
        ('description_ru', data.description_ru),
        ('img', image),
        ('color', color),

    ])


def basket_format_get(data):
    print('as')
    subctg = SubCategory.objects.filter(pk=data.product_subctg_id).first()
    product = ''
    if subctg.type == 1:
        product = karniz_format(Karniz.objects.filter(pk=data.product_id).first())
    elif subctg.type == 2:
        product = kalso_format(Kalso.objects.filter(pk=data.product_id).first())
    elif subctg.type == 3:
        product = karona_format(Karona.objects.filter(pk=data.product_id).first())
    elif subctg.type == 4:
        product = noj_format(Noj.objects.filter(pk=data.product_id).first())
    elif subctg.type == 5:
        product = baget_format(Baget.objects.filter(pk=data.product_id).first())
    elif subctg.type == 6:
        product = dori_format(DoriAparat.objects.filter(pk=data.product_id).first())

    return OrderedDict([
        ('basket_id', data.id),
        ('product', product),
        ('subctg_id', data.product_subctg_id),

        ('user_id', data.user.id),
        ('soni', data.quantity),
        ('summa', data.summa),
        ('updated_dt', data.updated_dt),
        ('create_dt', data.create_dt),
    ])


def basket_format(data):
    return OrderedDict([
        ('basket_id', data.id),
        ('subctg_id', data.product_subctg_id),

        ('user_id', data.user.id),
        ('soni', data.quantity),
        ('summa', data.summa),
        ('updated_dt', data.updated_dt),
        ('create_dt', data.create_dt),
    ])


def comment_format(data):
    return OrderedDict([
        ('comment_id', data.id),
        ('user', None if not data.user else format(data.user)),
        ('product', data.product_id),
        ('text', data.text),
        ('created_at', data.created_at),
        ('like', Like.objects.select_related('commentary', 'user').filter(commentary_id=data.id, like=True).count()),
        ('dislike', Like.objects.select_related('commentary', 'user').filter(commentary_id=data.id, dislike=True).count()),
    ])


def banner_format(data):
    return OrderedDict([
        ('id',data.id),
        ('name',data.name),
        ('image',data.image.url),
    ])


def contact_format(data):
    return OrderedDict([
        ("phone", data.phone),
        ("phone2", data.phone2),
        ("phone3", data.phone3),
        ("phone4", data.phone4),
        ("phone5", data.phone5),
        ("facebook", data.facebook),
        ("instagram", data.instagram),
        ("telegram", data.telegram),
        ("youtube", data.youtube),
    ])


def prosaved_format(data):
    return OrderedDict([
        ('prosaved_id', data.id),
        ('user', format(data.user)),
        ('updated_dt', data.updated_dt),
        ('create_dt', data.create_dt),
    ])


def prosaved_format_get(data):
    subctg = SubCategory.objects.filter(pk=data.subctg_id).first()
    product = ''
    if subctg.type == 1:
        product = karniz_format(Karniz.objects.filter(pk=data.product_id).first())
    elif subctg.type == 2:
        product = kalso_format(Kalso.objects.filter(pk=data.product_id).first())
    elif subctg.type == 3:
        product = karona_format(Karona.objects.filter(pk=data.product_id).first())
    elif subctg.type == 4:
        product = noj_format(Noj.objects.filter(pk=data.product_id).first())
    elif subctg.type == 5:
        product = baget_format(Baget.objects.filter(pk=data.product_id).first())
    elif subctg.type == 6:
        product = dori_format(DoriAparat.objects.filter(pk=data.product_id).first())

    return OrderedDict([
        ('prosaved_id', data.id),
        ('product_id', product),
        ('user', format(data.user)),
        ('updated_dt', data.updated_dt),
        ('create_dt', data.create_dt),
    ])


#
#
# def subcategory_format(data):
#     return OrderedDict([
#         ('id', data.id),
#         ('name', data.name_uz),
#         ('name', data.name_ru),
#         ('ctg', None if not data.ctg else category_format(data.ctg)),
#     ])
#
#
# def tkan_format(data):
#     return OrderedDict([
#         ('id', data.id),
#         ('product', product_format(data.product)),
#         ('user_id', data.tkan_name),
#         ('soni', data.tkan_material),
#         ('summa', data.tkan_price),
#
#     ])
#
#
# def product_format(data):
#     images = ProductImg.objects.select_related('product').filter(product_id=data.id).values('img')
#     tkan = TkanImg.objects.select_related('product').filter(product_id=data.id).values('img')
#     color = ColorImg.objects.select_related('product').filter(product=data)
#     dis = Discount.objects.select_related('product').filter(product=data).first()
#     # character = Character.objects.select_related('product').filter(product=data).first()
#     if dis:
#         dis = discount_format(dis)
#     else:
#         dis = {}
#     colors = []
#     for i in color:
#         colors.append({
#             "imgs": "" if not i.img else i.img.url,
#             "name": i.color
#         })
#
#     return OrderedDict([
#         ('id', data.id),
#         ('sub_ctg', None if not data.sub_ctg else subcategory_format(data.sub_ctg)),
#         ('name_uz', data.name_uz),
#         ('name_ru', data.name_ru),
#         ('code', data.code),
#         ('price', data.price),
#         ('credit', data.credit),
#         ('bonus', data.bonus),
#         ('size', data.size),
#         # ('waranty_uz', data.waranty_uz),
#         ('waranty', data.waranty),
#         ('collection_uz', data.collection_uz),
#         ('collection_ru', data.collection_ru),
#         ('matras_uz', data.matras_uz),
#         ('matras_ru', data.matras_ru),
#         ('xususiyatlari_uz', data.xususiyatlari_uz),
#         ('xususiyatlari_ru', data.xususiyatlari_ru),
#         ('qoshimchalari_uz', data.qoshimchalari_uz),
#         ('qoshimchalari_ru', data.qoshimchalari_ru),
#         ('balandligi', data.balandligi),
#         ('mehanizm', data.mehanizm_uz),
#         ('mehanizm', data.mehanizm_ru),
#         ('massa', data.massa),
#         ('maqsad_uz', data.maqsad_uz),
#         ('maqsad_ru', data.maqsad_ru),
#         ('razmer', data.razmer),
#         ('qattiqlik_uz', data.qattiqlik_uz),
#         ('qattiqlik_ru', data.qattiqlik_ru),
#         ('brand', data.brand),
#
#
#         ('images', [] if not images else [MEDIA_URL + x['img'] for x in images]),
#         ('tkans', [] if not tkan else [MEDIA_URL + x['img'] for x in tkan]),
#         ('color', colors),
#         ('dis', dis)
#
#     ])
#
#
# def character_format(data):
#     return OrderedDict([
#         ('id', data.waranty),
#         ('collection', data.collection),
#         ('matras', data.matras),
#         ('xususiyatlari', data.xususiyatlari),
#         ('qoshimchalari', data.qoshimchalari),
#         ('balandligi', data.balandligi),
#         ('mehanizm', data.mehanizm),
#         ('maqsad', data.maqsad),
#         ('razmer', data.razmer),
#         ('qattiqlik', data.qattiqlik),
#         ('brand', data.brand),
#
#     ])
#
#
#
#
# def colorimg_format(data):
#     return OrderedDict([
#         ('product', data.product),
#         ('color', data.color),
#         ('img', data.img.url),
#
#     ])
#
#
# def tkanImg_format(data):
#     return OrderedDict([
#         ('product', data.product),
#         ('tkan', data.tkan),
#         ('img', data.img.url),
#
#     ])
#
#
# def comment_format(data):
#     return OrderedDict([
#         ('comment_id', data.id),
#         ('user', None if not data.user else format(data.user)),
#         ('product', data.product.id),
#         ('text', data.text),
#         ('created_at', data.created_at),
#         ('like', Like.objects.select_related('commentary', 'user').filter(commentary_id=data.id, like=True).count()),
#         ('dislike', Like.objects.select_related('commentary', 'user').filter(commentary_id=data.id, dislike=True).count()),
#     ])
#
#
#
# def like_dislike_format(data):
#     print('\n','bu like',data.like,'\n')
#     return OrderedDict([
#
#
#
#     ])
#
#
# def discount_format(data):
#     return OrderedDict([
#         ('id', data.id),
#         ('procent', data.procent),
#         ('start_date', data.start_date),
#         ('end_date', data.end_date),
#     ])
#
# def banner_format(data):
#     return OrderedDict([
#         ('id',data.id),
#         ('name',data.name),
#         ('image',data.image.url),
#     ])
#
# # def format_course(data, lang=None):
# #     images = CourseImage.objects.select_related('course').filter(course_id=data.id).values('image')
# #
# #     return OrderedDict([
# #         ('id', data.id),
# #         ('category', data.course_category),
# #         ('image', data.image if not data.image else data.image.url),
# #         ('video', data.video if not data.video else data.video.url),
# #         ('title', data.title.get(lang) if lang else data.title),
# #         ('years', data.years),
# #         ('months', data.months),
# #         ('about', data.about.get(lang) if lang else data.about),
# #         ('images', [] if not images else [MEDIA_URL + x['image'] for x in images])
# #     ])
