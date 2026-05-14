from rest_framework import serializers
from .models import Profile, ProfileReview, CommitteeComment, ProfileOfficerAssignment
from apps.accounts.serializers import UserPublicSerializer
from apps.common.serializers import (
    EthnicGroupSerializer, ReligionSerializer, EducationLevelSerializer,
    PoliticalLevelSerializer, AdministrativeUnitSerializer,
)
from apps.uploads.serializers import UploadedFileSerializer


class ProfileListSerializer(serializers.ModelSerializer):
    """Lightweight — for list views / dashboard."""
    officer_in_charge_name = serializers.CharField(
        source='officer_in_charge.full_name', read_only=True, default=None
    )
    current_ward_name = serializers.CharField(
        source='current_ward.name', read_only=True, default=None
    )
    user_phone = serializers.CharField(source='user.phone', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id', 'profile_number', 'full_name', 'gender', 'dob',
            'status', 'status_display', 'ai_score', 'submitted_at',
            'officer_in_charge_id', 'officer_in_charge_name', 'current_ward_name', 'user_phone',
            'created_at', 'updated_at',
        ]


class ProfileDetailSerializer(serializers.ModelSerializer):
    """Full profile — all sections A–K."""
    user = UserPublicSerializer(read_only=True)
    # CCCD is sourced from the user account, not profile. Read-only here.
    cccd = serializers.CharField(source='user.cccd', read_only=True, default=None)
    ethnic_group_detail    = EthnicGroupSerializer(source='ethnic_group', read_only=True)
    ethnic_group_name      = serializers.CharField(source='ethnic_group.name', read_only=True, default=None)
    religion_detail        = ReligionSerializer(source='religion', read_only=True)
    religion_name          = serializers.CharField(source='religion.name', read_only=True, default=None)
    edu_level_detail       = EducationLevelSerializer(source='edu_level', read_only=True)
    political_level_detail_obj = PoliticalLevelSerializer(source='political_level', read_only=True)
    current_ward_detail    = AdministrativeUnitSerializer(source='current_ward', read_only=True)
    hometown_ward_detail   = AdministrativeUnitSerializer(source='hometown_ward', read_only=True)
    birth_ward_detail      = AdministrativeUnitSerializer(source='birth_place_ward', read_only=True)
    photo_file_detail      = UploadedFileSerializer(source='photo_file', read_only=True)
    status_display         = serializers.CharField(source='get_status_display', read_only=True)
    officer_name           = serializers.CharField(source='officer_in_charge.full_name', read_only=True, default=None)

    # Write-only FK IDs
    ethnic_group_id    = serializers.PrimaryKeyRelatedField(
        source='ethnic_group', queryset=__import__('apps.common.models', fromlist=['EthnicGroup']).EthnicGroup.objects.all(),
        write_only=True, required=False, allow_null=True
    )
    religion_id        = serializers.PrimaryKeyRelatedField(
        source='religion', queryset=__import__('apps.common.models', fromlist=['Religion']).Religion.objects.all(),
        write_only=True, required=False, allow_null=True
    )
    edu_level_id       = serializers.PrimaryKeyRelatedField(
        source='edu_level', queryset=__import__('apps.common.models', fromlist=['EducationLevel']).EducationLevel.objects.all(),
        write_only=True, required=False, allow_null=True
    )
    political_level_id = serializers.PrimaryKeyRelatedField(
        source='political_level', queryset=__import__('apps.common.models', fromlist=['PoliticalLevel']).PoliticalLevel.objects.all(),
        write_only=True, required=False, allow_null=True
    )
    current_ward_id    = serializers.PrimaryKeyRelatedField(
        source='current_ward', queryset=__import__('apps.common.models', fromlist=['AdministrativeUnit']).AdministrativeUnit.objects.all(),
        write_only=True, required=False, allow_null=True
    )
    hometown_ward_id   = serializers.PrimaryKeyRelatedField(
        source='hometown_ward', queryset=__import__('apps.common.models', fromlist=['AdministrativeUnit']).AdministrativeUnit.objects.all(),
        write_only=True, required=False, allow_null=True
    )
    birth_place_ward_id = serializers.PrimaryKeyRelatedField(
        source='birth_place_ward', queryset=__import__('apps.common.models', fromlist=['AdministrativeUnit']).AdministrativeUnit.objects.all(),
        write_only=True, required=False, allow_null=True
    )
    temporary_ward_id  = serializers.PrimaryKeyRelatedField(
        source='temporary_ward', queryset=__import__('apps.common.models', fromlist=['AdministrativeUnit']).AdministrativeUnit.objects.all(),
        write_only=True, required=False, allow_null=True
    )
    photo_file_id      = serializers.PrimaryKeyRelatedField(
        source='photo_file', queryset=__import__('apps.uploads.models', fromlist=['UploadedFile']).UploadedFile.objects.all(),
        write_only=True, required=False, allow_null=True
    )

    class Meta:
        model = Profile
        exclude = ['deleted_at']
        read_only_fields = [
            'id', 'user', 'cccd', 'profile_number', 'ai_score', 'ai_last_scanned_at',
            'ai_issues_json', 'submitted_at', 'approved_at', 'approved_by',
            'completed_at', 'last_returned_at', 'return_reason',
            'rejected_at', 'rejected_reason', 'created_at', 'updated_at',
        ]

    def get_fields(self):
        """Allow applicants to have partial profiles - relax required constraint."""
        fields = super().get_fields()
        # When reading/writing, don't require fields that would cause 400 errors
        # for incomplete profiles being edited by applicants
        for field_name in ['full_name', 'gender']:
            if field_name in fields:
                fields[field_name].required = False
                fields[field_name].allow_blank = True
        
        # DateField: not required, but if provided must be valid
        if 'dob' in fields:
            fields['dob'].required = False
        
        return fields

    def update(self, instance, validated_data):
        # Auto word count
        self_text = validated_data.get('self_assessment_text', instance.self_assessment_text)
        if self_text:
            validated_data['self_assessment_word_count'] = len(self_text.split())
        return super().update(instance, validated_data)


class ProfileReviewSerializer(serializers.ModelSerializer):
    reviewer_name = serializers.CharField(source='reviewer.full_name', read_only=True)

    class Meta:
        model = ProfileReview
        fields = ['id', 'action', 'from_status', 'to_status', 'comment',
                  'reviewer_id', 'reviewer_name', 'created_at']
        read_only_fields = ['id', 'from_status', 'to_status', 'reviewer_id', 'created_at']


class CommitteeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommitteeComment
        fields = ['id', 'type', 'content', 'signed_by', 'signed_date', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class ProfileWorkflowSerializer(serializers.Serializer):
    """Generic workflow action: submit / approve / return / reject / complete / withdraw."""
    action  = serializers.ChoiceField(choices=ProfileReview.Action.choices)
    comment = serializers.CharField(required=False, allow_blank=True)
    return_reason   = serializers.CharField(required=False, allow_blank=True)
    rejected_reason = serializers.CharField(required=False, allow_blank=True)
