from rest_framework import serializers
from .models import Actor, Movie

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name']

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    average_grade = serializers.FloatField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'actors', 'average_grade']

    def create(self, validated_data):
        actors_data = validated_data.pop('actors')
        movie = Movie.objects.create(**validated_data)
        for actor in actors_data:
            actor_obj, _ = Actor.objects.get_or_create(**actor)
            movie.actors.add(actor_obj)
        return movie

    def update(self, instance, validated_data):
        actors_data = validated_data.pop('actors', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if actors_data:
            instance.actors.clear()
            for actor in actors_data:
                actor_obj, _ = Actor.objects.get_or_create(**actor)
                instance.actors.add(actor_obj)
        instance.save()
        return instance
