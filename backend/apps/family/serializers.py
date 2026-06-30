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
        # Use prefetched cache when available; sort in Python to avoid extra DB query.
        entries = sorted(
            obj.history_entries.all(),
            key=lambda e: (e.sort_order or 0, e.from_year or 0, e.from_month or 0),
        )
        return HistoryEntrySerializer(entries, many=True).data
