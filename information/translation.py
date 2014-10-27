from modeltranslation.translator import translator, TranslationOptions
from information.models import News, UsefullInformation


class InformationTranslationOptions(TranslationOptions):
    fields = ('title', 'body',)

translator.register(News, InformationTranslationOptions)
translator.register(UsefullInformation, InformationTranslationOptions)