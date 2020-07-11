from rest_framework import serializers
from website.models import login1

class login1Serializer(serializers.ModelSerializer):

    class Meta:
        model=login1
        fields = '__all__'