from rest_framework.permissions import AllowAny
from .models import Log
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets
from .serializers import LogSerializer, UserSerializer
from django.contrib.auth import get_user_model


class LogView(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer




class CreateUserview(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny)
    serializer_class = UserSerializer
