# from rest_framework.generics import GenericAPIView
# from rest_framework.response import Response
# from base.formats import discount_format
#
#
#
# class DiscountView(GenericAPIView):
#
#     def get(self, requests, pk=None, *args, **kwargs):
#         if pk:
#             #     discount = Discount.objects.filter(pk=pk).first()
#             #     if discount:
#             #         return Response({
#             #             "data": discount_format(discount)
#             #         })
#             #
#             #     return Response({
#             #         "Maxsulot topilmadi"
#             #     })
#             #
#             # result = [discount_format(i) for i in Discount.objects.all()]
#             # return Response({
#             #     "data": result
#             #     })
#             try:
#                 discount = Discount.objects.get(pk=pk)
#                 resul = discount_format(discount)
#             except:
#                 resul = "Maxsulot topilmadi"
#             return Response({"data": resul})
#
#         result = [discount_format(i) for i in Discount.objects.all()]
#         if not result:
#             result = "Discountda Maxsulot umuman yo'q"
#         return Response({
#             "data": result
#         })