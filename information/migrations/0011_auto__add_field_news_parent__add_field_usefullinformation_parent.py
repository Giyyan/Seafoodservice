# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'News.parent'
        db.add_column(u'information_news', 'parent',
                      self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='related', null=True, to=orm['information.News']),
                      keep_default=False)

        # Adding field 'UsefullInformation.parent'
        db.add_column(u'information_usefullinformation', 'parent',
                      self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='related', null=True, to=orm['information.UsefullInformation']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'News.parent'
        db.delete_column(u'information_news', 'parent_id')

        # Deleting field 'UsefullInformation.parent'
        db.delete_column(u'information_usefullinformation', 'parent_id')


    models = {
        u'information.news': {
            'Meta': {'object_name': 'News'},
            'body': ('tinymce.models.HTMLField', [], {}),
            'body_en': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'body_ru': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'related'", 'null': 'True', 'to': u"orm['information.News']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'information.usefullinformation': {
            'Meta': {'object_name': 'UsefullInformation'},
            'body': ('tinymce.models.HTMLField', [], {}),
            'body_en': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'body_ru': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'related'", 'null': 'True', 'to': u"orm['information.UsefullInformation']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['information']