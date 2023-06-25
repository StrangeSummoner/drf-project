from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, old_instance, validated_data):
        old_instance.name = validated_data.get('name', old_instance.name) 
        old_instance.description = validated_data.get('description', old_instance.description)
        old_instance.active = validated_data.get('active', old_instance.active)
        old_instance.save()
        return old_instance