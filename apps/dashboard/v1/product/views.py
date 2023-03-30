from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response
from apps.dashboard.models import *
from base.formats import *


class ProductView(ListCreateAPIView):

    def get(self, requests, pk=None, ctg=None, *args, **kwargs):
        data = requests.data

        if data['type'] == "karniz":
            subctg = SubCategory.objects.filter(pk=data['sub_category_id']).first()
            if not subctg:
                return Response({
                    "Error": "bunaqa sub category mavjud emas"
                })

            product = Karniz.objects.filter(pk=pk, category_id=subctg.id, status=True).first()
            if not product:
                return Response({

                    "Error": " bu sub categoryda bunaqa product mavjud emas"
                })

            return Response({
                "prod": karniz_format(product)
            })

        if data['type'] == "kalso":
            subctg = SubCategory.objects.filter(pk=data['sub_category_id']).first()
            if not subctg:
                return Response({
                    "Error": "bunaqa sub category mavjud emas"
                })

            product = Kalso.objects.filter(pk=pk, category_id=subctg.id, status=True).first()
            if not product:
                return Response({
                    'ctg':subcategory_format(subctg),

                    "Error": " bu sub categoryda bunaqa product mavjud emas"
                })

            return Response({
                "prod": kalso_format(product)
            })

        if data['type'] == "karona":
            subctg = SubCategory.objects.filter(pk=data['sub_category_id']).first()
            if not subctg:
                return Response({
                    "Error": "bunaqa sub category mavjud emas"
                })

            product = Karona.objects.filter(pk=pk, category_id=subctg.id, status=True).first()
            if not product:
                return Response({

                    "Error": " bu sub categoryda bunaqa product mavjud emas"
                })

            return Response({
                "prod": karona_format(product)
            })





        if data['type'] == "noj":
            subctg = SubCategory.objects.filter(pk=data['sub_category_id']).first()
            if not subctg:
                return Response({
                    "Error": "bunaqa sub category mavjud emas"
                })

            product = Noj.objects.filter(pk=pk, category_id=subctg.id, status=True).first()
            if not product:
                return Response({

                    "Error": " bu sub categoryda bunaqa product mavjud emas"
                })

            return Response({
                "prod": noj_format(product)
            })

        if data['type'] == "baget":
            subctg = SubCategory.objects.filter(pk=data['sub_category_id']).first()
            if not subctg:
                return Response({
                    "Error": "bunaqa sub category mavjud emas"
                })

            product = Baget.objects.filter(pk=pk, category_id=subctg.id, status=True).first()
            if not product:
                return Response({

                    "Error": "bunaqa product mavjud emas"
                })

            return Response({
                "prod": baget_format(product)
            })

        if data['type'] == "dori_aparat":
            subctg = SubCategory.objects.filter(pk=data['sub_category_id']).first()
            if not subctg:
                return Response({
                    "Error": "bunaqa sub category mavjud emas"
                })

            product = DoriAparat.objects.filter(pk=pk, category_id=subctg.id, status=True).first()
            if not product:
                return Response({

                    "Error": "bunaqa product mavjud emas"
                })


            return Response({
                "prod": dori_format(product)
            })

        return Response({
            "Error": "typeni to'gri kirit"
        })







    # def post(self, requests, pk=None,*args, **kwargs):
    #     data = requests.data
    #     product = Karniz.objects.filter(pk=pk).filter(category_id=SubCategory.objects.filter(pk=data['sub_category_id'])).first()
    #     return Response({
    #             "Error": "bunaqa sub category mavjud emas"
    #         })
    #

    # if  pk:
    #     try:
    #         product = Product.objects.filter(pk=pk).first()
    #         result = karniz_format(product)
    #     except:
    #         result = "bu subcategory da maxsulot topilmadi"
    #
    # else:
    #     result = []
    #     for i in Product.objects.all():
    #         result.append(karniz_format(i))
    #
    # return Response(result)

    # def put(self, requests, pk, *args, **kwargs):
    #
    #     data = requests.data
    #     new = Product.objects.get(pk=pk)
    #     serializer = self.get_serializer(data=data, instance=new, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     root = serializer.save()
    #     return Response(product_format(root))
    #
    # def delete(self, requests, pk, *args, **kwargs):
    #     prod= Product.objects.filter(pk=pk).first()
    #     if prod:
    #         # prod.delete()
    #         result = "product o'chirildi"
    #     else:
    #         result = "product topilmadi"
    #     return Response ({"reultat":result})
