from rest_framework import serializers
from django.contrib.auth.models import User

from app.models import (
    Books,
    Reads,
    Reviews,
    Authors,
    WrittenBy,
    Collections,
    Contains,
    Profiles,
    ReadingGoals,
    Upvotes
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 'password'
        )
        extra_kwargs = {'password' : {'write_only' : True}}

class BookSerializer(serializers.ModelSerializer):

    publication_date = serializers.DateField(
        format="%b %d, %Y", 
        input_formats=["%b %d, %Y", 'iso-8601'], 
        allow_null=True
    )

    class Meta:
        model = Books
        fields = (
            'id', 'book_title', 'book_synopsis', 'book_publisher',
            'publication_date', 'genre', 'average_rating', 'book_thumbnail', 'read_count'
        )

class ReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reads
        fields = (
            'id', 'user', 'book', 'month_added',
        )

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = (
            'id', 'user', 'book', 'review', 'rating', 'date',
        )

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Authors
        fields = (
            'id', 'author_name',
        )

class WrittenBySerializer(serializers.ModelSerializer):

    class Meta:
        model = WrittenBy
        fields = (
            'id', 'book', 'author',
        )

class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collections
        fields = (
            'id', 'collection_type', 'is_private', 
            'description', 'collection_name', 'count', 'date_created', 'owner',
        )

class ContainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contains
        fields = (
            'id', 'collection', 'book', 'time_added',
        )

class ReadingGoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReadingGoals
        fields = (
            'id', 'user', 'current_month', 'reading_goal'
        )

class UpvoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Upvotes
        fields = (
            'id', 'user', 'review'
        )
