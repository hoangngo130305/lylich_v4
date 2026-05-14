from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import HistoryEntry, WorkHistory, EducationHistory, OrgParticipation, Award, OverseasTravel, OverseasRelative
from .serializers import (
    HistoryEntrySerializer, WorkHistorySerializer, EducationHistorySerializer,
    OrgParticipationSerializer, AwardSerializer, OverseasTravelSerializer, OverseasRelativeSerializer,
)
from apps.accounts.permissions import IsOfficerOrApplicant


def make_list_create_view(model, serializer_class, profile_fk='profile_id'):
    class View(generics.ListCreateAPIView):
        permission_classes = [IsOfficerOrApplicant]

        def get_serializer_class(self):
            return serializer_class

        def get_queryset(self):
            pid = self.kwargs['profile_id']
            if self.request.user.role_code == 'quan_chung':
                return model.objects.filter(**{profile_fk: pid, 'profile__user': self.request.user})
            return model.objects.filter(**{profile_fk: pid})

        def perform_create(self, s):
            s.save(**{profile_fk: self.kwargs['profile_id']})
    return View


def make_detail_view(model, serializer_class):
    class View(generics.RetrieveUpdateDestroyAPIView):
        permission_classes = [IsOfficerOrApplicant]
        queryset = model.objects.all()

        def get_serializer_class(self):
            return serializer_class
    return View


HistoryListCreate   = make_list_create_view(HistoryEntry, HistoryEntrySerializer)
HistoryDetail       = make_detail_view(HistoryEntry, HistoryEntrySerializer)
WorkListCreate      = make_list_create_view(WorkHistory, WorkHistorySerializer)
WorkDetail          = make_detail_view(WorkHistory, WorkHistorySerializer)
EducationListCreate = make_list_create_view(EducationHistory, EducationHistorySerializer)
EducationDetail     = make_detail_view(EducationHistory, EducationHistorySerializer)
OrgListCreate       = make_list_create_view(OrgParticipation, OrgParticipationSerializer)
OrgDetail           = make_detail_view(OrgParticipation, OrgParticipationSerializer)
AwardListCreate     = make_list_create_view(Award, AwardSerializer)
AwardDetail         = make_detail_view(Award, AwardSerializer)
TravelListCreate    = make_list_create_view(OverseasTravel, OverseasTravelSerializer)
TravelDetail        = make_detail_view(OverseasTravel, OverseasTravelSerializer)
RelativeListCreate  = make_list_create_view(OverseasRelative, OverseasRelativeSerializer)
RelativeDetail      = make_detail_view(OverseasRelative, OverseasRelativeSerializer)


@api_view(['GET'])
@permission_classes([IsOfficerOrApplicant])
def all_sections(request, profile_id):
    """Return all supplementary sections for a profile in one call."""
    def check_access():
        if request.user.role_code == 'quan_chung':
            from apps.profiles.models import Profile
            try:
                Profile.objects.get(id=profile_id, user=request.user)
            except Profile.DoesNotExist:
                return False
        return True

    if not check_access():
        return Response({'success': False, 'error': 'Không có quyền truy cập.'}, status=403)

    return Response({
        'success': True,
        'data': {
            'history':           HistoryEntrySerializer(HistoryEntry.objects.filter(profile_id=profile_id, entry_type='self').order_by('from_year','from_month'), many=True).data,
            'work_history':      WorkHistorySerializer(WorkHistory.objects.filter(profile_id=profile_id).order_by('from_year'), many=True).data,
            'education_history': EducationHistorySerializer(EducationHistory.objects.filter(profile_id=profile_id).order_by('from_year'), many=True).data,
            'org_participations':OrgParticipationSerializer(OrgParticipation.objects.filter(profile_id=profile_id), many=True).data,
            'awards':            AwardSerializer(Award.objects.filter(profile_id=profile_id, type='award'), many=True).data,
            'disciplines':       AwardSerializer(Award.objects.filter(profile_id=profile_id, type='discipline'), many=True).data,
            'overseas_travels':  OverseasTravelSerializer(OverseasTravel.objects.filter(profile_id=profile_id), many=True).data,
            'overseas_relatives':OverseasRelativeSerializer(OverseasRelative.objects.filter(profile_id=profile_id), many=True).data,
            'family_history':    HistoryEntrySerializer(HistoryEntry.objects.filter(profile_id=profile_id, entry_type='family').order_by('family_member_id', 'from_year', 'from_month', 'sort_order'), many=True).data,
        }
    })
