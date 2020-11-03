from rest_framework import serializers

from .models import Developer


class DeveloperListSerializer(serializers.ModelSerializer):
    """Developer list"""

    class Meta:
        model = Developer
        fields = ("surname", "name", "age")