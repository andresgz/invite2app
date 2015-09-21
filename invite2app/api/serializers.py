from invite2app.users.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'name', 'username', 'date_joined')
