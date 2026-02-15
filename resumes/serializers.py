from rest_framework import serializers
import re


class ResumeSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=15)
    skills = serializers.ListField(
        child=serializers.CharField(max_length=50),
        allow_empty=False
    )
    experience = serializers.IntegerField(min_value=0)

    def validate_phone(self, value):
        if not re.match(r'^\+?\d{10,15}$', value):
            raise serializers.ValidationError(
                "Phone number must contain 10-15 digits and may start with +."
            )
        return value
