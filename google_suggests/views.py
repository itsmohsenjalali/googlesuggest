from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Word, Suggestion
from .serializers import SuggestionSerialize
from .google_suggest import get_google_suggest
# Create your views here.


@api_view(['GET'])
def GetGoogleSuggests(request, word):
    """
    Get Google Suggestion for a word

    Parameters:
    word (str): the word we want Google suggestion for it

    Returns:
    json: Google Suggestion  
    """
    # return Suggestion if in the database
    if Word.objects.filter(word__exact=word).exists():
        SuggestionWord = Suggestion.objects.filter(word__exact=word)
        SuggestionWordSerializes = SuggestionSerialize(
            SuggestionWord, many=True)
        return Response(SuggestionWordSerializes.data, status=status.HTTP_200_OK)
    # Get data from Google and store in database
    wordobject = Word.objects.create(word=word)
    Suggestlist = get_google_suggest(word=word)
    SuggestionWord = Suggestion.objects.bulk_create(
        [Suggestion(word=wordobject, sugg=i) for i in Suggestlist])
    SuggestionWordSerializes = SuggestionSerialize(
        SuggestionWord, many=True)
    return Response(SuggestionWordSerializes.data, status=status.HTTP_200_OK)
