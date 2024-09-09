from rest_framework import serializers
from django.contrib.auth.models import User




class UserSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField()
    class Meta:
        model = User
        fields = ['username','password','password2']

    def validate(self, data):
        if not data['password2'] or not data['password'] or data['password2'] != data['password']:
            raise serializers.ValidationError("password2 =! password")
        return data



