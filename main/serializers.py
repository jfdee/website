from rest_framework import serializers

from .models import Developer


class DeveloperSerializer(serializers.ModelSerializer):
    """Developer list"""

    class Meta:
        model = Developer
        fields = '__all__'
