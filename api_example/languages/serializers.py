from rest_framework import serializers
from .models import Register

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Register
        fields = ('id', 'url', 'name', 'Password','Email')


# class LoginSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Register
#         fields = ('id', 'url', 'name', 'Password')
        		        