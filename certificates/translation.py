from modeltranslation.translator import translator, TranslationOptions
from models import Certificate


class CertificateTranslationOptions(TranslationOptions):
    fields = ('description',)

translator.register(Certificate, CertificateTranslationOptions)
