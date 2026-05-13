import os
import uuid
from django.conf import settings
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import UploadedFile
from .serializers import UploadedFileSerializer, FileUploadSerializer


class FileUploadView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file     = serializer.validated_data['file']
        category = serializer.validated_data['category']
        profile_id = serializer.validated_data.get('profile_id')

        ext         = os.path.splitext(file.name)[1].lower()
        stored_name = f'{uuid.uuid4().hex}{ext}'
        rel_path    = f'uploads/{category}/{stored_name}'
        abs_path    = os.path.join(settings.MEDIA_ROOT, rel_path)

        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        with open(abs_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        import mimetypes
        mime, _ = mimetypes.guess_type(file.name)

        uploaded = UploadedFile.objects.create(
            uploader=request.user,
            profile_id=profile_id,
            category=category,
            original_name=file.name,
            stored_path=rel_path,
            mime_type=mime,
            file_size=file.size,
        )

        return Response(
            {'success': True, 'data': UploadedFileSerializer(uploaded, context={'request': request}).data},
            status=status.HTTP_201_CREATED
        )


class FileListView(generics.ListAPIView):
    serializer_class = UploadedFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = UploadedFile.objects.filter(uploader=self.request.user)
        category = self.request.query_params.get('category')
        profile_id = self.request.query_params.get('profile_id')
        if category:
            qs = qs.filter(category=category)
        if profile_id:
            qs = qs.filter(profile_id=profile_id)
        return qs.order_by('-created_at')
