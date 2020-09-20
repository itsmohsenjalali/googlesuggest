from rest_framework import serializers
from .models import Suggestion, Word


class SuggestionSerialize(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = ('sugg',)
