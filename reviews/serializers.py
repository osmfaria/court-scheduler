from rest_framework import serializers
from django.utils.timezone import now
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ["id", "court", "user"]