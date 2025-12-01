from rest_framework.serializers import ModelSerializer
from .models import *
     

class Pin_Num_Serializer(ModelSerializer):
    class Meta:
        model=Pin_Num
        fields='__all__'

class Profile_Serializer(ModelSerializer):
    class Meta:
        model=profile
        fields='__all__'
class Account_Serializer(ModelSerializer):
    class Meta:
        model=account
        fields='__all__'