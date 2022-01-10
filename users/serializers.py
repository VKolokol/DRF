from rest_framework import serializers

from users.models import Users, UserProfiles


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfiles
        fields = ['gender', 'region', 'phone']


class UserSerializer(serializers.ModelSerializer):
    userprofiles = UserProfileSerializers(read_only=True)

    class Meta:
        model = Users
        fields = ['email', 'first_name', 'last_name', 'birthday', 'userprofiles']
