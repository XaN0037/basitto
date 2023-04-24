from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response
from apps.dashboard.models import *
from base.formats import *


class ProductView(ListCreateAPIView):

    def get(self, request, *args, **kwargs):
        global formatt
        data = request.query_params
        product_type = data.get('type')
        product_id = data.get('product_id')
        sub_category_id = data.get('sub_category_id')

        if product_type is None:
            nott = 'type'
        elif product_id is None:
            nott = 'product_id'
        else:
            nott = None

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
                for i in Karona.objects.filter(status=True):
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
            if product_id == "all":
                product = Karniz.objects.all()
                mylist = [formatt(i) for i in product]
                return Response(mylist)

            product = Karniz.objects.filter(pk=product_id, category_id=sub_category_id, status=True).first()

        elif product_type == "kalso":
            formatt = kalso_format
            if product_id == "all":
                product = Kalso.objects.all()
                mylist = [formatt(i) for i in product]
                return Response(mylist)

            product = Kalso.objects.filter(pk=product_id, category_id=sub_category_id, status=True).first()

        elif product_type == "karona":
            formatt = karona_format
            if product_id == "all":
                product = Karona.objects.all()
                mylist = [formatt(i) for i in product]
                return Response(mylist)

            product = Karona.objects.filter(pk=product_id, category_id=sub_category_id, status=True).first()

        elif product_type == "noj":
            formatt = noj_format
            if product_id == "all":
                product = Noj.objects.all()
                mylist = [formatt(i) for i in product]
                return Response(mylist)

            product = Noj.objects.filter(pk=product_id, category_id=sub_category_id, status=True).first()

        elif product_type == "baget":
            formatt = baget_format
            if product_id == "all":
                product = Baget.objects.all()
                mylist = [formatt(i) for i in product]
                return Response(mylist)

            product = Baget.objects.filter(pk=product_id, category_id=sub_category_id, status=True).first()

        elif product_type == "dori_aparat":
            formatt = dori_format
            if product_id == "all":
                product = DoriAparat.objects.all()
                mylist = [formatt(i) for i in product]
                return Response(mylist)

            product = DoriAparat.objects.filter(pk=product_id, category_id=sub_category_id, status=True).first()
        else:
            return Response({"Error": "bunaqa type mavjud emas"})

        if not product:
            return Response({"Error": " bu sub categoryda bunaqa product mavjud emas"})

        return Response(formatt(product))

