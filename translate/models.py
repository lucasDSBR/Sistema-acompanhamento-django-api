from django.db import models

# Create your models here.

class FullParagraphs(models.Model):
    ptBR = models.TextField(default="")
    enUS = models.TextField(default="")
    correctionPtBR = models.TextField(default="")
    correctionEnUS = models.TextField(default="")
    def __str__(self):
        return self.fullParagraphs_Cod

class Phrases(models.Model):
    ptBR = models.TextField(default="")
    enUS = models.TextField(default="")
    correctionPtBR = models.TextField(default="")
    correctionEnUS = models.TextField(default="")
    def __str__(self):
        return self.phrases_Cod
    
class Words(models.Model):
    ptBR = models.TextField(default="")
    enUS = models.TextField(default="")
    correctionPtBR = models.TextField(default="")
    correctionEnUS = models.TextField(default="")
    def __str__(self):
        return self.words_Cod   