class MovieSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = ('movie_name')