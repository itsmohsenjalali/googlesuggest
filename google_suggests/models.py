from django.db import models

# Create your models here.


class Word(models.Model):
    key = models.AutoField(auto_created=True, primary_key=True)
    word = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.word


class Suggestion(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE, to_field='word')
    sugg = models.CharField(max_length=150)
