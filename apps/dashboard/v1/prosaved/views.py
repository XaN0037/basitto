from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.api.v1.auth.servise import BearerAuth
from base.formats import *
from apps.dashboard.models import *


class ProsavedView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerAuth,)

    def get(self, requests, *args, **kwargs):
        user_product_saved = Prosaved.objects.filter(user_id=requests.user.id).first()
        if not user_product_saved:
            return Response({
                "Error": " bu user maxsulot saqlamagan"
            })
        else:
            result = []
            for i in Prosaved.objects.all().filter(user_id=requests.user.id):
                result.append(prosaved_format(i))

        return Response(result)

    def post(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        product_type = data['type']

        nott = 'type' if 'type' not in data else 'product_id' if 'product_id' not in data else None

        if nott:
            return Response({"Error": f"{nott} kiritilmagan"})

        if product_type == "karniz":
            formatt = karniz_format
            product = Karniz.objects.filter(pk=data['product_id'], status=True).first()

        elif product_type == "kalso":
            formatt = kalso_format
            product = Kalso.objects.filter(pk=data['product_id'], status=True).first()

        elif product_type == "karona":
            formatt = karona_format
            product = Karona.objects.filter(pk=data['product_id'], status=True).first()

        elif product_type == "noj":
            formatt = noj_format
            product = Noj.objects.filter(pk=data['product_id'], status=True).first()

        elif product_type == "baget":
            formatt = baget_format
            product = Baget.objects.filter(pk=data['product_id'], status=True).first()

        elif product_type == "dori_aparat":
            formatt = dori_format
            product = DoriAparat.objects.filter(pk=data['product_id'], status=True).first()

        else:
            return Response({"Error": "bunaqa type mavjud emas"})

        # subctg = SubCategory.objects.filter(pk=data['sub_category_id']).first()
        # if not subctg:
        #     return Response({
        #         "Error": "bunaqa sub category mavjud emas"
        #     })

        if not product:
            return Response({"Error": " bu sub categoryda bunaqa product mavjud emas"})

        product_saved = Prosaved.objects.filter(product_id=product.id).first()

        if product_saved:
            return Response({
                "Error": "bunaqa id_li product allaqachon saqlangan"
            })

        root = Prosaved()
        root.user = user
        root.product_id = product.id
        root.subctg_id = product.category.id
        root.save()

        return Response({'success': prosaved_format(root),
                         'product': formatt(product)})

    def delete(self, request, *args, **kwargs):
        data = request.data
        if not data:
            return Response({
                "Error": "saved_id kiritilmagan"
            })

        saved_id = data['saved_id']

        product_saved_id = Prosaved.objects.filter(pk=saved_id).first()

        if not product_saved_id:
            return Response({
                "Error": "bunaqa id li product saqlanmagan"
            })

        if product_saved_id:
            product_saved_id.delete()
            return Response({
                "Success": "saqlangan product o'chirib tashlandi"
            })

