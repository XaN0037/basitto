from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.dashboard.models import SubCategory
from base.formats import *


class SubCategoryView(GenericAPIView):
    def get(self, requests, pk=None, *args, **kwargs):
        if pk:

            try:
                discount = SubCategory.objects.get(pk=pk)
                resul = subcategory_format(discount)
            except:
                resul = "SubCategory topilmadi"
            return Response({"data": resul})

        result = [subcategory_format(i) for i in SubCategory.objects.all()]
        if not result:
            result = "SubCategory umuman yo'q"
        return Response({
            "data": result
        })