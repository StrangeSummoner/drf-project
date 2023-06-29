from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ['id', 'name', 'description']
        # exclude = ['active']

    def get_len_name(self, object):
        length = len(object.name)
        return length

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and description should not be the same")
        else:
            return data
        
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        else:
            return value
        


# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short")
#     else:
#         value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, old_instance, validated_data):
#         old_instance.name = validated_data.get('name', old_instance.name) 
#         old_instance.description = validated_data.get('description', old_instance.description)
#         old_instance.active = validated_data.get('active', old_instance.active)
#         old_instance.save()
#         return old_instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and description should not be the same")
#         else:
#             return data

#     # def validate_name(self, value):

#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name is too short")
#     #     else:
#     #         return value