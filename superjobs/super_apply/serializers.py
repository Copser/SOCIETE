from rest_framework import serializers
from .models import SuperApplyForm, SuperExperience, SuperReference


class SuperSerializer(serializers.Serializer):
    """TODO: extending models,
        return: Serializer
    """
    first_name = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=100)
    mobile = serializers.CharField(max_length=100)
    hourly_rate = serializers.IntegerField()
    working_hours = serializers.IntegerField()
    drivers_license = serializers.CharField(max_length=100)
    pk = serializers.IntegerField(read_only=True)

