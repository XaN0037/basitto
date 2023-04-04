from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response
from apps.dashboard.models import *
from base.formats import *


class ProductView(ListCreateAPIView):

    def get(self, request, *args, **kwargs):
        global formatt
        formatt = karniz_format
        data = request.data
        product_type = data['type']
        product_id = data['product_id']

        nott = 'type' if 'type' not in data else None if 'product_id' not in data \
            else 'sub_category_id' if 'sub_category_id' not in data else None

        if nott:
            return Response({"Error": f"{nott} kiritilmagan"})

        if product_type == 'all' and product_id == 'all':
            l = []
            try:
                for i in Karniz.objects.filter(status=True):
                    l.append(karniz_format(i))
            except:
                l = l

            try:
                for i in Karona.objects.afilter(status=True):
                    l.append(karona_format(i))
            except:
                l = l
            try:
                for i in Kalso.objects.filter(status=True):
                    l.append(kalso_format(i))
            except:
                l = l
            try:
                for i in Noj.objects.filter(status=True):
                    l.append(noj_format(i))
            except:
                l = l
            try:
                for i in Baget.objects.filter(status=True):
                    l.append(baget_format(i))
            except:
                l = l
            try:
                for i in DoriAparat.objects.filter(status=True):
                    l.append(dori_format(i))
            except:
                l = l
            return Response({"data": l})

        if product_type == "karniz":
            formatt = karniz_format
            product = Karniz.objects.filter(pk=data['product_id'], category_id=data['sub_category_id'],
                                            status=True).first()

        elif product_type == "kalso":
            formatt = kalso_format
            if data['product_id'] == 'all':
                l = Kalso.objects.filter(category_id=data['sub_category_id'],
                                         status=True)
                product = []
                for i in l:
                    product.append(formatt(i))
                return Response(product)

            else:
                product = Kalso.objects.filter(pk=data['product_id'], category_id=data['sub_category_id'],
                                               status=True).first()




        elif product_type == "karona":
            formatt = karona_format

            if data['product_id'] == 'all':
                l = Karona.objects.filter(category_id=data['sub_category_id'],
                                          status=True)
                product = []
                for i in l:
                    product.append(formatt(i))
                return Response(product)

            else:
                product = Karona.objects.filter(pk=data['product_id'], category_id=data['sub_category_id'],
                                                status=True).first()

        elif product_type == "noj":
            formatt = noj_format

            if data['product_id'] == 'all':
                l = Noj.objects.filter(category_id=data['sub_category_id'],
                                       status=True)
                product = []
                for i in l:
                    product.append(formatt(i))
                return Response(product)

            else:
                product = Noj.objects.filter(pk=data['product_id'], category_id=data['sub_category_id'],
                                             status=True).first()


        elif product_type == "baget":
            formatt = baget_format
            if data['product_id'] == 'all':
                l = Baget.objects.filter(category_id=data['sub_category_id'],
                                         status=True)
                product = []
                for i in l:
                    product.append(formatt(i))
                return Response(product)

            else:
                product = Baget.objects.filter(pk=data['product_id'], category_id=data['sub_category_id'],
                                               status=True).first()

        elif product_type == "dori_aparat":
            formatt = dori_format
            if data['product_id'] == 'all':
                l = DoriAparat.objects.filter(category_id=data['sub_category_id'],
                                              status=True)
                product = []
                for i in l:
                    product.append(formatt(i))
                return Response(product)

            else:
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

        return Response(formatt(product))
