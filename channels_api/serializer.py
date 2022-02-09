from rest_framework import serializers
from channels_api.models import Channel, Category, Subcription
from user_auth_api.serializers import UserSerializer


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = [
            "id",
            "channel_title",
            "channel_description",
            "channel_image",
            "subscription_price",
            "category_id",
        ]


class CategorySerializer(serializers.ModelSerializer):
    channels = ChannelSerializer(many=True)

    class Meta:
        model = Category
        fields = ["id", "name", "channels"]


class SubscriptionSerializer(serializers.ModelSerializer):
    startDate = serializers.DateField()
    endDate = serializers.DateField()
    days = serializers.CharField(max_length=40)
    total = serializers.CharField(max_length=100)

    class Meta:
        model = Subcription
        fields = '__all__'
