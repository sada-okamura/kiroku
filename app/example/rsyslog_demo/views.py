import logging
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import authentication_classes, permission_classes
from example.rsyslog_demo.serializers import UserSerializer, GroupSerializer
from . import remote_logger

logger = logging.getLogger('django')


@authentication_classes([])
@permission_classes([])
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, *args, **kwargs):
        logger.info('this is local logger')
        remote_logger.info(tag='login', message='this is remote logger')
        return super().list(*args, **kwargs)
