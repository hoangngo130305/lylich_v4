from rest_framework import serializers
from .models import ProfileEditHistory, ProfileCorrectionRequest, ProfileCorrectionItem, WordExportLog


class ProfileEditHistorySerializer(serializers.ModelSerializer):
    edited_by_name = serializers.CharField(source='edited_by.full_name', read_only=True)

    class Meta:
        model  = ProfileEditHistory
        fields = ['id', 'profile', 'edited_by', 'edited_by_name', 'section', 'field_name',
                  'old_value', 'new_value', 'edit_reason', 'created_at']
        read_only_fields = fields


class ProfileCorrectionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ProfileCorrectionItem
        fields = ['id', 'section', 'field_name', 'description', 'status',
                  'corrected_at', 'corrected_note', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class ProfileCorrectionRequestSerializer(serializers.ModelSerializer):
    items           = ProfileCorrectionItemSerializer(many=True, read_only=True)
    created_by_name = serializers.CharField(source='created_by.full_name', read_only=True)
    resolved_by_name= serializers.CharField(source='resolved_by.full_name', read_only=True, default=None)

    class Meta:
        model  = ProfileCorrectionRequest
        fields = ['id', 'profile', 'created_by', 'created_by_name', 'status', 'overall_note',
                  'resolved_by', 'resolved_by_name', 'resolved_at', 'created_at', 'updated_at', 'items']
        read_only_fields = ['id', 'created_by', 'created_by_name', 'resolved_by_name',
                            'resolved_at', 'created_at', 'updated_at']


class CorrectionRequestCreateSerializer(serializers.ModelSerializer):
    items = ProfileCorrectionItemSerializer(many=True)

    class Meta:
        model  = ProfileCorrectionRequest
        fields = ['profile', 'overall_note', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        request_obj = ProfileCorrectionRequest.objects.create(**validated_data)
        for item_data in items_data:
            ProfileCorrectionItem.objects.create(request=request_obj, **item_data)
        return request_obj


class WordExportLogSerializer(serializers.ModelSerializer):
    exported_by_name = serializers.CharField(source='exported_by.full_name', read_only=True)

    class Meta:
        model  = WordExportLog
        fields = ['id', 'profile', 'exported_by', 'exported_by_name', 'template_name',
                  'file', 'file_name', 'file_size', 'sections_json', 'created_at']
        read_only_fields = fields
