from rest_framework import serializers

class ImageUploadSeralizer(serializers.Serializer):
    image=serializers.ImageField()