from rest_framework import serializers
from User_Login.models import UserProfile, Survey, Friend


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'password', 'first_name',
                  'last_name', 'username', 'phone', 'gender', 'dob', 'access_code')
        extra_kwargs = {
            "password": {"write_only": True, "style": {
                "input_type": "password"
            }}
        }


class ChangePasswordSerializer(serializers.Serializer):
    model = UserProfile
    old_password = serializers.CharField(required=True,
                                         style={'input_type': 'password', 'placeholder': 'old password'})
    new_password = serializers.CharField(required=True,
                                         style={'input_type': 'password', 'placeholder': 'new password'})


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'answer1', 'answer2', 'answer3', 'answer4', 'answer5')

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('id', 'user', 'friend', 'status')
