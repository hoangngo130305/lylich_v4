from rest_framework import serializers
from .models import HistoryEntry, WorkHistory, EducationHistory, OrgParticipation, Award, OverseasTravel, OverseasRelative


class HistoryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryEntry
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class WorkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkHistory
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class EducationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationHistory
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class OrgParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgParticipation
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class AwardSerializer(serializers.ModelSerializer):
    type_display = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = Award
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class OverseasTravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverseasTravel
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class OverseasRelativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverseasRelative
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class ProfileSectionsSerializer(serializers.Serializer):
    """All supplementary sections in a single payload."""
    history      = HistoryEntrySerializer(many=True, read_only=True)
    work_history = WorkHistorySerializer(many=True, read_only=True)
    education    = EducationHistorySerializer(many=True, read_only=True)
    awards       = AwardSerializer(many=True, read_only=True)
    overseas_travels   = OverseasTravelSerializer(many=True, read_only=True)
    overseas_relatives = OverseasRelativeSerializer(many=True, read_only=True)
