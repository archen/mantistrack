# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Ooth.name'
        db.add_column('mantises_ooth', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=200, blank=True, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Ooth.name'
        db.delete_column('mantises_ooth', 'name')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Group']", 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']", 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'containers.container': {
            'Meta': {'object_name': 'Container'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['containers.ContainerType']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'containers.containertype': {
            'Meta': {'unique_together': "(('height', 'length', 'width', 'type'),)", 'object_name': 'ContainerType'},
            'height': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'width': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '5'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mantises.breed': {
            'Meta': {'object_name': 'Breed'},
            'adult_instar_female': ('django.db.models.fields.SmallIntegerField', [], {}),
            'adult_instar_male': ('django.db.models.fields.SmallIntegerField', [], {}),
            'high_humidity': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '5'}),
            'high_temperature': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'life_expectancy': ('django.db.models.fields.DecimalField', [], {'decimal_places': '4', 'max_digits': '5'}),
            'long_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '300'}),
            'low_humidity': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '5'}),
            'low_temperature': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '5'}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['photologue.Photo']"}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mantises.mantis': {
            'Meta': {'object_name': 'Mantis'},
            'born': ('django.db.models.fields.DateTimeField', [], {}),
            'breed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mantises.Breed']"}),
            'container': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['containers.Container']"}),
            'died': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'from_colony': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['mantises.NymphColony']"}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['photologue.Gallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mantises.molt': {
            'Meta': {'unique_together': "(('to_instar', 'from_instar', 'mantis'),)", 'object_name': 'Molt'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'from_instar': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mantis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mantises.Mantis']"}),
            'to_instar': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mantises.nymphcolony': {
            'Meta': {'object_name': 'NymphColony'},
            'container': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['containers.Container']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'num_died': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'num_hatched': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mantises.ooth': {
            'Meta': {'object_name': 'Ooth'},
            'container': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['containers.Container']"}),
            'date_hatched': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'date_laid': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'laid_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['mantises.Mantis']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'nymphs': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['mantises.NymphColony']"}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['photologue.Photo']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'photologue.gallery': {
            'Meta': {'object_name': 'Gallery', 'ordering': "['-date_added']"},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['photologue.Photo']", 'null': 'True', 'related_name': "'galleries'"}),
            'tags': ('photologue.models.TagField', [], {'blank': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'photologue.photo': {
            'Meta': {'object_name': 'Photo', 'ordering': "['-date_added']"},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'blank': 'True', 'max_length': '10'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['photologue.PhotoEffect']", 'null': 'True', 'related_name': "'photo_related'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tags': ('photologue.models.TagField', [], {'blank': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'photologue.photoeffect': {
            'Meta': {'object_name': 'PhotoEffect'},
            'background_color': ('django.db.models.fields.CharField', [], {'default': "'#FFFFFF'", 'max_length': '7'}),
            'brightness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'color': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'contrast': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'filters': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'reflection_size': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reflection_strength': ('django.db.models.fields.FloatField', [], {'default': '0.6'}),
            'sharpness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'transpose_method': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15'})
        }
    }

    complete_apps = ['mantises']