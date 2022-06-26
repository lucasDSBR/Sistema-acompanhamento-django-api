#IMPORTS
import os
from django.core.files.storage import default_storage
from django.http import HttpResponse
from nltk.tokenize import sent_tokenize, word_tokenize
import translators as ts
from ..models import FullParagraphs, Words
#METHODS


def handle_file_upload(file):
    file_name = default_storage.save('./storage/files/'+file.name, file)
    file = default_storage.open(file_name)
    return read_file(file_name)
    
def read_file(file_name):
    dataFile = []
    file = default_storage.open(file_name)
    try:
        dataFile.append(file.read().decode('utf8'))
        return tokenizeData(dataFile)
    except:
        return "Erro ao ler e adicionar dados do arquivo em Array. Erro: "
    
def tokenizeData(dataFile):
    allText = dataFile[0]
    textTokenized = sent_tokenize(allText)
    #data = translateSaveParagraphs(textTokenized)
    data = translateSaveWords(textTokenized)
    return data
    
    
def translateSaveParagraphs(textTokenized):
    #translate Full Paragraph:
    fullParagraphsTranslated = []
    i = 0
    for fullParagraphs in textTokenized:
        fullParagraphsTranslated.append(ts.google(fullParagraphs, from_language='pt', to_language='en'))
        fullParag = FullParagraphs(
            ptBR = fullParagraphs,
            enUS = fullParagraphsTranslated[i]
        )
        fullParag.save()
        i = i + 1
    return fullParagraphsTranslated
    
    
def translateSaveWords(textTokenized):
    #translate Words:
    paragraphTokenized = []
    for fullParagraphs in textTokenized:
        paragraphTokenized = word_tokenize(fullParagraphs)
        for word in paragraphTokenized:
            if Words.objects.filter(ptBR=word):
                continue
            else:
                w = ts.google(word, from_language='pt', to_language='en')
                s = Words(
                    ptBR = word,
                    enUS = w
                )
                s.save()