from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.api.v1.auth.servise import BearerAuth
from base.formats import *
from apps.dashboard.models import *


class BasketView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerAuth,)

    def post(self, request, *args, **kwargs):

        global formatt
        data =request.data
        product_id = data['product_id']
        product_type = data['type']
        user = request.user

        nott = 'type' if 'type' not in data else 'product_id' if 'product_id' not in data \
            else 'sub_category_id' if 'sub_category_id' not in data else None

        if nott:
            return Response({"Error": f"{nott} kiritilmagan"})

        # product_type = product_type[0].upper() + product_type[1:]

        if product_type == "karniz":
            formatt = karniz_format
            product = Karniz.objects.filter(pk=data['product_id'], category_id=data['sub_category_id'],
                                                  status=True).first()
        elif product_type == "kalso":
            formatt = kalso_format
            product = Kalso.objects.filter(pk=data['product_id'], category_id=data['sub_category_id'],
                                            status=True).first()
        elif product_type == "karona":
            formatt = karona_format
            product = Karona.objects.filter(pk=data['product_id'], category_id=data['sub_category_id'],
                                            status=True).first()
        elif product_type == "noj":
            formatt = noj_format
            product = Noj.objects.filter(pk=data['product_id'], category_id=data['sub_category_id'],
                                            status=True).first()
        elif product_type == "baget":
            formatt = baget_format
            product = Baget.objects.filter(pk=data['product_id'], category_id=data['sub_category_id'],
                                            status=True).first()
        elif product_type == "dori_aparat":
            formatt = dori_format
            product = DoriAparat.objects.filter(pk=data['product_id'], category_id=data['sub_category_id'],
                                            status=True).first()
        else:
            return Response({"Error": "bunaqa type mavjud emas"})

        subctg = SubCategory.objects.filter(pk=data['sub_category_id']).first()
        if not subctg:
            return Response({
                "Error": "bunaqa sub category mavjud emas"
            })

        if not product:
            return Response({"Error": " bu sub categoryda bunaqa product mavjud emas"})

        basket = Basket.objects.filter(user_id=user.id).filter(product_id=product_id,
                                                               product_subctg_id=data["sub_category_id"]).first()
        if basket:
            basket.quantity += 1
            basket.summa = basket.quantity * product.price
            basket.save()
            return Response({"success": "edit",
                             'basket': basket_format(basket),
                             'product': formatt(product)})

        root = Basket()
        root.user = user
        root.product_id = data['product_id']
        root.product_subctg_id = data["sub_category_id"]
        root.summa = product.price
        root.save()

        return Response({"success": "saved",
                         'basket': basket_format(root),
                         'product': formatt(product)})






        # if product_type == "Karniz":
        #     subctg = SubCategory.objects.filter(pk=data['sub_category_id']).first()
        #     if not subctg:
        #         return Response({
        #             "Error": "bunaqa sub category mavjud emas"
        #         })
        #
        #     product = product_type.objects.filter(pk=data['product_id'], category_id=data['sub_category_id'],
        #                                  status=True).first()
        #     if not product:
        #         return Response({
        #
        #             "Error": " bu sub categoryda bunaqa product mavjud emas"
        #         })
        #     basket = Basket.objects.filter(user_id=user.id).filter(product_id=product_id,
        #                                                            product_subctg_id=data["sub_category_id"]).first()
        #     if basket:
        #         basket.quantity += 1
        #         basket.summa = basket.quantity * product.price
        #         basket.save()
        #         return Response({"success": "edit",
        #                          'basket': basket_format(basket),
        #                          'product': karniz_format(product)})
        #
        #     root = Basket()
        #     root.user = user
        #     root.product_id = data['product_id']
        #     root.product_subctg_id = data["sub_category_id"]
        #     root.summa = product.price
        #     root.save()
        #
        #     return Response({"success": "saved",
        #                      'basket': basket_format(root),
        #                      'product': karniz_format(product)})
        #
        # if data['type'] == "kalso":
        #     subctg = SubCategory.objects.filter(pk=data['sub_category_id']).first()
        #     if not subctg:
        #         return Response({
        #             "Error": "bunaqa sub category mavjud emas"
        #         })
        #
        #     product = Kalso.objects.filter(pk=data['product_id'], category_id=data['sub_category_id'],
        #                                  status=True).first()
        #     if not product:
        #         return Response({
        #
        #             "Error": " bu sub categoryda bunaqa product mavjud emas"
        #         })
        #     basket = Basket.objects.filter(user_id=user.id).filter(product_id=product_id,
        #                                                            product_subctg_id=data["sub_category_id"]).first()
        #     if basket:
        #         basket.quantity += 1
        #         basket.summa = basket.quantity * product.price
        #         basket.save()
        #         return Response({"success": "edit",
        #                          'basket': basket_format(basket),
        #                          'product': kalso_format(product)})
        #
        #     root = Basket()
        #     root.user = user
        #     root.product_id = data['product_id']
        #     root.product_subctg_id = data["sub_category_id"]
        #     root.summa = product.price
        #     root.save()
        #
        #     return Response({"success": "saved",
        #                      'basket': basket_format(root),
        #                      'product': noj_format(product)})
        #
        #
        #
        #
        # if data['type'] == "karona":
        #     subctg = SubCategory.objects.filter(pk=data['sub_category_id']).first()
        #     if not subctg:
        #         return Response({
        #             "Error": "bunaqa sub category mavjud emas"
        #         })
        #
        #     product = Karona.objects.filter(pk=data['product_id'], category_id=data['sub_category_id'],
        #                                  status=True).first()
        #     if not product:
        #         return Response({
        #
        #             "Error": " bu sub categoryda bunaqa product mavjud emas"
        #         })
        #     basket = Basket.objects.filter(user_id=user.id).filter(product_id=product_id,
        #                                                            product_subctg_id=data["sub_category_id"]).first()
        #     if basket:
        #         basket.quantity += 1
        #         basket.summa = basket.quantity * product.price
        #         basket.save()
        #         return Response({"success": "edit",
        #                          'basket': basket_format(basket),
        #                          'product': karona_format(product)})
        #
        #     root = Basket()
        #     root.user = user
        #     root.product_id = data['product_id']
        #     root.product_subctg_id = data["sub_category_id"]
        #     root.summa = product.price
        #     root.save()
        #
        #     return Response({"success": "saved",
        #                      'basket': basket_format(root),
        #                      'product': karona_format(product)})
        #
        #
        #
        #
        #
        # if data['type'] == "noj":
        #     subctg = SubCategory.objects.filter(pk=data['sub_category_id']).first()
        #     if not subctg:
        #         return Response({
        #             "Error": "bunaqa sub category mavjud emas"
        #         })
        #
        #     product = Noj.objects.filter(pk=data['product_id'], category_id=data['sub_category_id'], status=True).first()
        #     if not product:
        #         return Response({
        #
        #             "Error": " bu sub categoryda bunaqa product mavjud emas"
        #         })
        #     basket = Basket.objects.filter(user_id=user.id).filter(product_id=product_id,product_subctg_id=data["sub_category_id"]).first()
        #     if basket:
        #         basket.quantity += 1
        #         basket.summa = basket.quantity * product.price
        #         basket.save()
        #         return Response({"success":"edit",
        #                         'basket': basket_format(basket),
        #                          'product': noj_format(product)})
        #
        #     root = Basket()
        #     root.user = user
        #     root.product_id = data['product_id']
        #     root.product_subctg_id = data["sub_category_id"]
        #     root.summa = product.price
        #     root.save()
        #
        #
        #     return Response({"success":"saved",
        #                     'basket': basket_format(root),
        #                      'product': noj_format(product)})
        #
        #
        #
        #
        #
        # if data['type'] == "baget":
        #     subctg = SubCategory.objects.filter(pk=data['sub_category_id']).first()
        #     if not subctg:
        #         return Response({
        #             "Error": "bunaqa sub category mavjud emas"
        #         })
        #
        #     product = Baget.objects.filter(pk=data['product_id'], category_id=data['sub_category_id'],
        #                                  status=True).first()
        #     if not product:
        #         return Response({
        #
        #             "Error": " bu sub categoryda bunaqa product mavjud emas"
        #         })
        #     basket = Basket.objects.filter(user_id=user.id).filter(product_id=product_id,
        #                                                            product_subctg_id=data["sub_category_id"]).first()
        #     if basket:
        #         basket.quantity += 1
        #         basket.summa = basket.quantity * product.price
        #         basket.save()
        #         return Response({"success": "edit",
        #                          'basket': basket_format(basket),
        #                          'product': baget_format(product)})
        #
        #     root = Basket()
        #     root.user = user
        #     root.product_id = data['product_id']
        #     root.product_subctg_id = data["sub_category_id"]
        #     root.summa = product.price
        #     root.save()
        #
        #     return Response({"success": "saved",
        #                      'basket': basket_format(root),
        #                      'product': baget_format(product)})
        #
        # if data['type'] == "dori_aparat":
        #     subctg = SubCategory.objects.filter(pk=data['sub_category_id']).first()
        #     if not subctg:
        #         return Response({
        #             "Error": "bunaqa sub category mavjud emas"
        #         })
        #
        #     product = DoriAparat.objects.filter(pk=data['product_id'], category_id=data['sub_category_id'],
        #                                     status=True).first()
        #     if not product:
        #         return Response({
        #
        #             "Error": " bu sub categoryda bunaqa product mavjud emas"
        #         })
        #     basket = Basket.objects.filter(user_id=user.id).filter(product_id=product_id,
        #                                                            product_subctg_id=data["sub_category_id"]).first()
        #     if basket:
        #         basket.quantity += 1
        #         basket.summa = basket.quantity * product.price
        #         basket.save()
        #         return Response({"success": "edit",
        #                          'basket': basket_format(basket),
        #                          'product': dori_format(product)})
        #
        #     root = Basket()
        #     root.user = user
        #     root.product_id = data['product_id']
        #     root.product_subctg_id = data["sub_category_id"]
        #     root.summa = product.price
        #     root.save()
        #
        #     return Response({"success": "saved",
        #                      'basket': basket_format(root),
        #                      'product': karniz_format(product)})
        # return Response({
        #     "Error": "typeni to'gri kirit"
        # })


    def get(self, request, *args, **kwargs):
        user = request.user

        basket = Basket.objects.filter(user_id=request.user.id).first()


        if not basket:
            return Response({
                "Error": " bu user maxsulot bron qilmagan"
            })
        else:
            result = []
            for i in Basket.objects.all().filter(user_id=request.user.id):
                result.append(basket_format_get(i))

        result = {
            "summa": sum([x['summa'] for x in result]),
            "data": result
        }
        return Response(result)


    def put(self, request, *args, **kwargs):

        bron_id = request.data['bron_id']
        quantity = request.data['quantity']
        if not bron_id:
            return Response({
                "Error": "bron_id kiritilmagan"
            })
        bron = Basket.objects.filter(pk=bron_id, user=request.user).first()

        if not bron:
            return Response({
                "Error": "bunaqa idli bron savatda mavjut emas"
            })

        if not quantity:
            return Response({
                "Error": "quantity kiritilmagan"
            })
        product = ''
        subctg = SubCategory.objects.filter(pk=bron.product_subctg_id).first()
        if subctg.type == 1:
            product = Karniz.objects.filter(pk=bron.product_id).first()
        elif subctg.type == 2:
            product = Kalso.objects.filter(pk=bron.product_id).first()
        elif subctg.type == 3:
            product = Karona.objects.filter(pk=bron.product_id).first()
        elif subctg.type == 4:
            product =Noj.objects.filter(pk=bron.product_id).first()
        elif subctg.type == 5:
            product = Baget.objects.filter(pk=bron.product_id).first()
        elif subctg.type == 6:
            product = DoriAparat.objects.filter(pk=bron.product_id).first()



        bron.quantity = quantity
        bron.summa = quantity*product.price

        bron.save()
        return Response({
            "data": basket_format(bron)
        })



    def delete(self, request, *args, **kwargs):

        bron_id = request.data['bron_id']

        user = request.user
        if not bron_id:
            return Response({
                "Error": "bron_id kiritilmagan"
            })
        basket = Basket.objects.filter(pk=bron_id, user_id=user.id).first()

        if not basket:
            return Response({
                "Error": " bu id da bron topilmadi"
            })

        if basket:
            basket.delete()
            return Response({
                "Success": "Bron qilingan tarif o'chirib tashlandi"
            })




    #
    #
    #
    #
    #     if not product_id:
    #         return Response({
    #             "Error": "product_id kiritilmagan"
    #         })
    #
    #     product = Product.objects.filter(pk=product_id).first()
    #
    #     if not product:
    #         return Response({
    #             "Error": "bunaqa idli product mavjut emas"
    #         })
    #
    #     basket = Basket.objects.filter(user_id=user.id).filter(product_id=product_id).first()
    #     # img = ProductImg.objects.filter(product_id=product_id)
    #     if basket:
    #         basket.quantity += 1
    #         basket.summa = basket.quantity * product.price
    #         basket.save()
    #
    #         return Response({'success': basket_format(basket)})
    #
    #     root = Basket()
    #     root.user = user
    #     root.product = product
    #     root.summa = product.price
    #     root.save()
    #
    #     return Response({'success': basket_format(root)})
    #
    # def put(self, request, *args, **kwargs):
    #
    #     bron_id = request.data['bron_id']
    #     quantity = request.data['quantity']
    #     if not bron_id:
    #         return Response({
    #             "Error": "bron_id kiritilmagan"
    #         })
    #     bron = Basket.objects.filter(pk=bron_id, user=request.user).first()
    #
    #     if not bron:
    #         return Response({
    #             "Error": "bunaqa idli bron savatda mavjut emas"
    #         })
    #
    #     if not quantity:
    #         return Response({
    #             "Error": "quantity kiritilmagan"
    #         })
    #
    #     bron.quantity = quantity
    #
    #     bron.save()
    #     return Response({
    #         "data": basket_format(bron)
    #     })
    #
    # def delete(self, request, *args, **kwargs):
    #
    #     bron_id = request.data['bron_id']
    #
    #     user = request.user
    #     if not bron_id:
    #         return Response({
    #             "Error": "bron_id kiritilmagan"
    #         })
    #     basket = Basket.objects.filter(pk=bron_id, user_id=user.id).first()
    #
    #     if not basket:
    #         return Response({
    #             "Error": " bu id da bron topilmadi"
    #         })
    #
    #     if basket:
    #         basket.delete()
    #         return Response({
    #             "Success": "Bron qilingan tarif o'chirib tashlandi"
    #         })
    #
    #
    # def get(self, request, *args, **kwargs):
    #     user = request.user
    #
    #     user_basket = Basket.objects.filter(user_id=request.user.id).first()
    #     if not user_basket:
    #         return Response({
    #             "Error": " bu user maxsulot bron qilmagan"
    #         })
    #     else:
    #         result = []
    #         for i in Basket.objects.all().filter(user_id=request.user.id):
    #             result.append(basket_format(i))
    #
    #     result = {
    #         "summa": sum([x['summa'] for x in result]),
    #         "data": result
    #     }
    #     return Response(result)
