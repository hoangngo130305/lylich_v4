from rest_framework import generics, permissions
from .models import EthnicGroup, Religion, EducationLevel, PoliticalLevel, AdministrativeUnit
from .serializers import (
    EthnicGroupSerializer, ReligionSerializer, EducationLevelSerializer,
    PoliticalLevelSerializer, AdministrativeUnitSerializer
)


class EthnicGroupListView(generics.ListAPIView):
    queryset = EthnicGroup.objects.all()
    serializer_class = EthnicGroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReligionListView(generics.ListAPIView):
    queryset = Religion.objects.all()
    serializer_class = ReligionSerializer
    permission_classes = [permissions.IsAuthenticated]


class EducationLevelListView(generics.ListAPIView):
    queryset = EducationLevel.objects.all().order_by('sort')
    serializer_class = EducationLevelSerializer
    permission_classes = [permissions.IsAuthenticated]


class PoliticalLevelListView(generics.ListAPIView):
    queryset = PoliticalLevel.objects.all()
    serializer_class = PoliticalLevelSerializer
    permission_classes = [permissions.IsAuthenticated]


class AdministrativeUnitListView(generics.ListAPIView):
    serializer_class = AdministrativeUnitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = AdministrativeUnit.objects.all()
        unit_type = self.request.query_params.get('type')
        parent_id = self.request.query_params.get('parent_id')
        if unit_type:
            qs = qs.filter(type=unit_type)
        if parent_id:
            qs = qs.filter(parent_id=parent_id)
        return qs.order_by('name')
