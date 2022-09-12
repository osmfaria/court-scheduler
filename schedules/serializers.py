from rest_framework import serializers
from schedules.models import Schedule

import ipdb

from users.serializers import UserBaseInfoSerializer

class ScheduleSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Schedule
        fields = ["id", "datetime", "user", "court"]
        read_only_fields = ["user", "court"]

class ScheduleDetail(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ["datetime", "court"]
