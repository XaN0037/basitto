from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.dashboard.v1.pages.pages import *


class PagesViews(GenericAPIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        method = data.get("method")
        params = data.get('params')

        if not method:
            return Response({"Error": 'methodda xatolik'})

        if not params or params is None:
            return Response({"Erorr": "paramsda xatolik"})

        if "lan" not in params or params["lan"] not in ["uz", "ru"]:
            return Response({"Error": "tilda xatolik"})

        methods = ['page1', 'page2', 'page3', 'page4']

        if method in methods:
            if method == "page1":
                result = page1(params["lan"])
            elif method == "page2":
                result = page2[params["lan"]]
            elif method == "page3":
                result = page3[params["lan"]]

            return Response({
                "page": method,
                "data": result
            })

        else:
            return Response({
                "Error": "method topilmadi"
            })
