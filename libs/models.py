from django.db import models

class Degree(models.Model):
    name = models.CharField(max_length=255)
    lv = models.CharField(max_length=2)
    def __str__(self):
        return self.name

class Word(models.Model):
    level = models.IntegerField()
    word_en = models.CharField(max_length=100)
    word_uz = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.word_en} - {self.word_uz}"


class About(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)