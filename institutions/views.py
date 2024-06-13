from rest_framework.views import APIView
from rest_framework.response import Response
from institutions.models import Institution
from institutions.serializer import InstitutionSerializer


class ListInstitution(APIView):
    def get(self, request):
        institutions = Institution.objects.all()
        serializer = InstitutionSerializer(institutions, many=True)
        return Response(serializer.data)
