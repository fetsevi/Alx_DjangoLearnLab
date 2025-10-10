from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()  # shows username instead of ID
    recipient = serializers.StringRelatedField()
    target = serializers.StringRelatedField()

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target', 'timestamp', 'is_read']
