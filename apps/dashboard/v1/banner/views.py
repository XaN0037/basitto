from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.dashboard.models import Banner
from base.formats import banner_format



class BannerViews(GenericAPIView):
    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            banner = Banner.objects.filter(pk=pk).first()

            if not banner:
                return Response({
                    "error": "bu pk da mahsulot topilmadi"
                })
            return Response({
                "result": banner_format(banner)
            })

        banners = [banner_format(x) for x in Banner.objects.all()]
        return Response({
            "data": banners
        })
