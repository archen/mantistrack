# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Breed'
        db.create_table('mantises_breed', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('long_name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('life_expectancy', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=4)),
            ('low_temperature', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('high_temperature', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('low_humidity', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('high_humidity', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal('mantises', ['Breed'])

        # Adding model 'Prey'
        db.create_table('mantises_prey', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('long_name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mantises', ['Prey'])

        # Adding model 'Mantis'
        db.create_table('mantises_mantis', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('instar', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('breed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mantises.Breed'])),
            ('born', self.gf('django.db.models.fields.DateTimeField')()),
            ('died', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('mantises', ['Mantis'])

        # Adding model 'Feeding'
        db.create_table('mantises_feeding', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('prey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mantises.Prey'])),
            ('accepted', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('total_fed', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('feeding_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('mantises', ['Feeding'])

        # Adding model 'Molt'
        db.create_table('mantises_molt', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('mantis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mantises.Mantis'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('from_instar', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('to_instar', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('mantises', ['Molt'])


    def backwards(self, orm):
        # Deleting model 'Breed'
        db.delete_table('mantises_breed')

        # Deleting model 'Prey'
        db.delete_table('mantises_prey')

        # Deleting model 'Mantis'
        db.delete_table('mantises_mantis')

        # Deleting model 'Feeding'
        db.delete_table('mantises_feeding')

        # Deleting model 'Molt'
        db.delete_table('mantises_molt')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mantises.breed': {
            'Meta': {'object_name': 'Breed'},
            'high_humidity': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'high_temperature': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'life_expectancy': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '4'}),
            'long_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'low_humidity': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'low_temperature': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mantises.feeding': {
            'Meta': {'object_name': 'Feeding'},
            'accepted': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'feeding_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mantises.Prey']"}),
            'total_fed': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mantises.mantis': {
            'Meta': {'object_name': 'Mantis'},
            'born': ('django.db.models.fields.DateTimeField', [], {}),
            'breed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mantises.Breed']"}),
            'died': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instar': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mantises.molt': {
            'Meta': {'object_name': 'Molt'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'from_instar': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mantis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mantises.Mantis']"}),
            'to_instar': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mantises.prey': {
            'Meta': {'object_name': 'Prey'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['mantises']