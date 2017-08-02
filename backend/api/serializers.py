from rest_framework import serializers
from .models import Question, Choice

class QuestionSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    choices = serializers.StringRelatedField(many=True)
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Question
        fields = ('id', 'question_text', 'date_created', 'date_modified', 'choices')
        read_only_fields = ('date_created',)

class ChoiceSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Choice
        fields = ('id', 'question', 'choice_text', 'votes')
    