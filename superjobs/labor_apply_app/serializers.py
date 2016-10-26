from django.contrib.auth.models import User
from rest_framework import serializers
from labor_apply_app.models import PersonalInfo, DRIVERS_CATEGORY_CHOICES


class PersonalInfoSerializer(serializers.Serializer):
    """TODO: Exteding are PersonalInfo model
    return: TODO
    """
    id = serializers.IntegerField(read_only=True)
    owner = serializers.PrimaryKeyRelatedField(many=True, queryset=PersonalInfo.objects.all())
    class Meta:
        model = PersonalInfo
        fields = ('owner', 'full_name', 'email', 'mobile', 'birthdate', 'previous_company_name',
                  'previous_company_email', 'previous_company_phone', 'previous_job_title',
                  'relevante_experience', 'hospitality_experience', 'future_working_hours',
                  'hourly_wage', 'driver_license', 'curriculum_vitae')


class UserSerializer(serializers.ModelSerializer):
    """TODO: Add UserSerializer to handle user permission and authentication
    return: TODO
    """
    owner = serializers.PrimaryKeyRelatedField(many=True, queryset=PersonalInfo.objects.all())
    class Meta:
        model = User
        fields = ('id', 'owner', 'username')
