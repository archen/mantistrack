# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContainerType'
        db.create_table('containers_containertype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('height', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=5)),
            ('length', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=5)),
            ('width', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=5)),
            ('url', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('containers', ['ContainerType'])

        # Adding unique constraint on 'ContainerType', fields ['height', 'length', 'width', 'type']
        db.create_unique('containers_containertype', ['height', 'length', 'width', 'type'])

        # Adding model 'Container'
        db.create_table('containers_container', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['containers.ContainerType'])),
        ))
        db.send_create_signal('containers', ['Container'])

        # Adding model 'EnvironmentReading'
        db.create_table('containers_environmentreading', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('temperature', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=5)),
            ('humidity', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=5)),
            ('container', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['containers.Container'])),
        ))
        db.send_create_signal('containers', ['EnvironmentReading'])

        # Adding unique constraint on 'EnvironmentReading', fields ['date', 'container']
        db.create_unique('containers_environmentreading', ['date', 'container_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'EnvironmentReading', fields ['date', 'container']
        db.delete_unique('containers_environmentreading', ['date', 'container_id'])

        # Removing unique constraint on 'ContainerType', fields ['height', 'length', 'width', 'type']
        db.delete_unique('containers_containertype', ['height', 'length', 'width', 'type'])

        # Deleting model 'ContainerType'
        db.delete_table('containers_containertype')

        # Deleting model 'Container'
        db.delete_table('containers_container')

        # Deleting model 'EnvironmentReading'
        db.delete_table('containers_environmentreading')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'to': "orm['auth.Group']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'containers.container': {
            'Meta': {'object_name': 'Container'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['containers.ContainerType']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'containers.containertype': {
            'Meta': {'object_name': 'ContainerType', 'unique_together': "(('height', 'length', 'width', 'type'),)"},
            'height': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'width': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '5'})
        },
        'containers.environmentreading': {
            'Meta': {'object_name': 'EnvironmentReading', 'unique_together': "(('date', 'container'),)"},
            'container': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['containers.Container']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'humidity': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'temperature': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '5'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['containers']