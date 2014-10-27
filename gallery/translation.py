from modeltranslation.translator import translator, TranslationOptions
from models import PhotoGallery, VideoGallery


class MediaTranslationOptions(TranslationOptions):
    fields = ('description',)

translator.register(PhotoGallery, MediaTranslationOptions)
translator.register(VideoGallery, MediaTranslationOptions)