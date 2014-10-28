from modeltranslation.translator import translator, TranslationOptions
from models import GeograohyTransporation


class GeograohyTransporationTranslationOptions(TranslationOptions):
    fields = ('description', 'title')

translator.register(GeograohyTransporation, GeograohyTransporationTranslationOptions)
