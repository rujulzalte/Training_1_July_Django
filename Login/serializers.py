from rest_framework import serializers
from . models import User

# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     email = serializers.EmailField()
#     date = serializers.DateField()
#     zipcode = serializers.IntegerField()
#     phone = serializers.IntegerField()   

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','date','zipcode','phone']