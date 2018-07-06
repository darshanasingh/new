from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Log

class LogSerializer(serializers.ModelSerializer):
    class meta:
        model = Log
        fields = ('id','username','email_id','date_created')



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    def create(self, validated_data):
        user = get_user_model().objects.create(
            username = validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save
        return user
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')



