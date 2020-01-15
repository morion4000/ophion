# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Movie.year'
        db.delete_column(u'movies_movie', 'year')

        # Adding field 'Movie.release_date'
        db.add_column(u'movies_movie', 'release_date',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Movie.year'
        db.add_column(u'movies_movie', 'year',
                      self.gf('django.db.models.fields.IntegerField')(default='', max_length=4),
                      keep_default=False)

        # Deleting field 'Movie.release_date'
        db.delete_column(u'movies_movie', 'release_date')


    models = {
        u'movies.movie': {
            'Meta': {'object_name': 'Movie'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imdb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'release_date': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'synopsis': ('django.db.models.fields.TextField', [], {}),
            'thumbnail': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'tmdb': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['movies']