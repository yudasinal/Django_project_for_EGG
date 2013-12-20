# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
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
            ('name_of_the_game', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'logins', ['Game'])

        # Adding model 'Info'
        db.create_table(u'logins_info', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organization_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(max_length=500, blank=True)),
        ))
        db.send_create_signal(u'logins', ['Info'])

        # Adding M2M table for field game on 'Info'
        m2m_table_name = db.shorten_name(u'logins_info_game')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('info', models.ForeignKey(orm[u'logins.info'], null=False)),
            ('game', models.ForeignKey(orm[u'logins.game'], null=False))
        ))
        db.create_unique(m2m_table_name, ['info_id', 'game_id'])

        # Adding M2M table for field department on 'Info'
        m2m_table_name = db.shorten_name(u'logins_info_department')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('info', models.ForeignKey(orm[u'logins.info'], null=False)),
            ('department', models.ForeignKey(orm[u'logins.department'], null=False))
        ))
        db.create_unique(m2m_table_name, ['info_id', 'department_id'])

        # Adding model 'CustomUser'
        db.create_table(u'logins_customuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'logins', ['CustomUser'])

        # Adding M2M table for field department on 'CustomUser'
        m2m_table_name = db.shorten_name(u'logins_customuser_department')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customuser', models.ForeignKey(orm[u'logins.customuser'], null=False)),
            ('department', models.ForeignKey(orm[u'logins.department'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customuser_id', 'department_id'])

        # Adding M2M table for field game on 'CustomUser'
        m2m_table_name = db.shorten_name(u'logins_customuser_game')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customuser', models.ForeignKey(orm[u'logins.customuser'], null=False)),
            ('game', models.ForeignKey(orm[u'logins.game'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customuser_id', 'game_id'])


    def backwards(self, orm):
        # Deleting model 'Department'
        db.delete_table(u'logins_department')

        # Deleting model 'Game'
        db.delete_table(u'logins_game')

        # Deleting model 'Info'
        db.delete_table(u'logins_info')

        # Removing M2M table for field game on 'Info'
        db.delete_table(db.shorten_name(u'logins_info_game'))

        # Removing M2M table for field department on 'Info'
        db.delete_table(db.shorten_name(u'logins_info_department'))

        # Deleting model 'CustomUser'
        db.delete_table(u'logins_customuser')

        # Removing M2M table for field department on 'CustomUser'
        db.delete_table(db.shorten_name(u'logins_customuser_department'))

        # Removing M2M table for field game on 'CustomUser'
        db.delete_table(db.shorten_name(u'logins_customuser_game'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'logins.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'department': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['logins.Department']", 'symmetrical': 'False'}),
            'game': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['logins.Game']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'logins.department': {
            'Meta': {'object_name': 'Department'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'logins.game': {
            'Meta': {'object_name': 'Game'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_of_the_game': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'logins.info': {
            'Meta': {'object_name': 'Info'},
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'}),
            'department': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['logins.Department']", 'symmetrical': 'False', 'blank': 'True'}),
            'game': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['logins.Game']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['logins']