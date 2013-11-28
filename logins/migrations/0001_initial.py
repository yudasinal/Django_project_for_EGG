# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Department'
        db.create_table(u'logins_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'logins', ['Department'])

        # Adding model 'Game'
        db.create_table(u'logins_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['logins.Department'])),
            ('name_of_the_game', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'logins', ['Game'])


    def backwards(self, orm):
        # Deleting model 'Department'
        db.delete_table(u'logins_department')

        # Deleting model 'Game'
        db.delete_table(u'logins_game')


    models = {
        u'logins.department': {
            'Meta': {'object_name': 'Department'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'logins.game': {
            'Meta': {'object_name': 'Game'},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['logins.Department']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_of_the_game': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['logins']