from rest_framework import serializers
from .models import Meeting

class MeetingSerializer(serializers.ModelSerializer):

    class Meta:
            model = Meeting
            fields = ('pk','name', 'description', 'date')
