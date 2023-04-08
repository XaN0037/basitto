from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from apps.dashboard.models import Contacts
from base.formats import contact_format


class ContactViews(GenericAPIView):
    def get(self, requests, *args, **kwargs):
        contacts = Contacts.objects.all()
        print(contacts)
        if not contacts:
            return Response({"error": "contacts qo'shilmagan"})

        contact = [contact_format(i) for i in contacts]
        return Response({"data": contact})
