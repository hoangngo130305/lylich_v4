from rest_framework import serializers
from .models import EthnicGroup, Religion, EducationLevel, PoliticalLevel, AdministrativeUnit


class EthnicGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = EthnicGroup
        fields = ['id', 'name']


class ReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religion
        fields = ['id', 'name']


class EducationLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationLevel
        fields = ['id', 'code', 'name', 'sort']


class PoliticalLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliticalLevel
        fields = ['id', 'code', 'name']


class AdministrativeUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministrativeUnit
        fields = ['id', 'parent_id', 'type', 'code', 'name']


class AdministrativeUnitTreeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = AdministrativeUnit
        fields = ['id', 'type', 'code', 'name', 'children']

    def get_children(self, obj):
        children = obj.children.all()
        return AdministrativeUnitTreeSerializer(children, many=True).data
