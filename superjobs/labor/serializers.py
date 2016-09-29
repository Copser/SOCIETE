from rest_framework import serializers
from .models import ApplyForm, Reference, Experience


class ReferenceSerializer(serializers.Serializer):
    """TODO: serialize Rreference Model
    returns: TODO
    """
    company_name = serializers.CharField(max_length=255)
    company_email = serializers.EmailField(max_length=100)
    company_phone = serializers.CharField(max_length=255)
    job_title = serializers.CharField(max_length=255)

    class Meta:
        model = Reference
        fields = ('company_name', 'company_email', 'company_phone',
                  'previous_job_title')


class ExperienceSerializer(serializers.Serializer):
    """TODO: Serialize Experience Model
    returns: TODO
    """
    work_experience = serializers.CharField(max_length=255)
    hospitality = serializers.CharField(max_length=255)

    class Meta:
        model = Experience
        fields = ('work_experience', 'working_hours')


class ApplyFormSerializer(serializers.ModelSerializer):
    """TODO: Serialize ApplyForm Model, and we are adding ExperienceSerializer and ReferenceSerializer
    to ApplyFormSerializer, because we want to nest them into ApplyForm
    returns: TODO
    """
    class Meta:
        model = ApplyForm
        fields = '__all__'
