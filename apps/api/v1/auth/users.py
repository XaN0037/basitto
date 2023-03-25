import re

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.api.v1.auth.serializer import Userserializer
from apps.api.v1.auth.servise import BearerAuth
from base.formats import format


class UserView(GenericAPIView):
    serializer_class = Userserializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerAuth,)

    def get(self, request, *args, **kwargs):
        return Response(format(request.user))

    def put(self, requests, *args, **kwargs):

        data = requests.data
        serializer = self.get_serializer(data=data, instance=requests.user, partial=True)
        serializer.is_valid(raise_exception=True)
        root = serializer.save()
        return Response(format(root))

    def post(self, requests, *args, **kwargs):
        data = requests.data

        nott = "old" if "old" not in data else "new" if 'new' not in data else None
        if nott:
            return Response({
                "Error": f"{nott} section is not filled"
            })
        if len(data['new']) < 7 or data['new'].islower() or data['new'].isalpha():
            return Response({
                "status": "Parolda 8 ta simvol yoki katta xarf qatnashishi shart"})

        if not requests.user.check_password(data['old']):
            return Response({
                "status": "old password is not correct",

            })
        requests.user.set_password(data['new'])
        requests.user.save()

        return Response({
            "status": "password changed",
            "user": format(requests.user)})
