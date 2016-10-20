from rest_framework import serializers
from labor_apply_app.models import PersonalInfo


class PersonalInfoSerializer(serializers.Serializer):
    """TODO: Exteding are PersonalInfo model
    return: TODO
    """
    class Meta:
        model = PersonalInfo
        fields = ('id', 'full_name', 'email', 'mobile', 'birthdate',
                  'previous_company_name', 'previous_company_email', 'previous_company_phone', 'previous_job_title',
                  'relevante_experience', 'hospitality_experience',
                  'future_working_hours', 'hourly_wage', 'driver_license', 'created')
