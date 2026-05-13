from rest_framework import serializers
from .models import StatsMonthly, ReportExport


class StatsMonthlySerializer(serializers.ModelSerializer):
    class Meta:
        model  = StatsMonthly
        fields = '__all__'
        read_only_fields = fields


class ReportExportSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.full_name', read_only=True)

    class Meta:
        model  = ReportExport
        fields = ['id', 'created_by', 'created_by_name', 'report_type', 'format',
                  'params', 'file_name', 'file_size', 'created_at']
        read_only_fields = ['id', 'created_by', 'created_by_name', 'file_name', 'file_size', 'created_at']
