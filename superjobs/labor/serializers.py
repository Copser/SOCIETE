from rest_framework import serializers
from .models import ApplyForm, Reference, Experience


class ReferenceSerializer(serializers.Serializer):
    """TODO:
    returns: TODO
    """
    company_name = serializers.CharField(max_length=255)
    company_email = serializers.EmailField(max_length=100)
    company_phone = serializers.CharField(max_length=255)
    previous_job_title = serializers.CharField(max_length=255)

    class Meta:
        model = Reference
        fields = ('company_name', 'company_email', 'company_phone',
                  'previous_job_title')


class ExperienceSerializer(serializers.Serializer):
    """TODO:
    returns: TODO
    """
    work_experience = serializers.CharField(max_length=255)
    hospitality = serializers.CharField(max_length=255)

    class Meta:
        model = Experience
        fields = ('work_experience', 'working_hours')

