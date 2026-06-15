from rest_framework import serializers
from .models import FamilyMember


class FamilyMemberSerializer(serializers.ModelSerializer):
    relationship_display = serializers.CharField(source='get_relationship_display', read_only=True)
    history = serializers.SerializerMethodField()

    class Meta:
        model = FamilyMember
        exclude = ['deleted_at', 'updated_by']
        read_only_fields = ['id', 'profile', 'created_at', 'updated_at']

    def get_history(self, obj):
        from apps.timelines.serializers import HistoryEntrySerializer
        entries = obj.history_entries.filter().order_by('sort_order', 'from_year', 'from_month')
        return HistoryEntrySerializer(entries, many=True).data
