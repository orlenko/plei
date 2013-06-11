# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Topic'
        db.create_table(u'pleiapp_topic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'pleiapp', ['Topic'])

        # Adding model 'Type'
        db.create_table(u'pleiapp_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'pleiapp', ['Type'])

        # Adding model 'Category'
        db.create_table(u'pleiapp_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'pleiapp', ['Category'])

        # Adding model 'ContentTypeResource'
        db.create_table(u'pleiapp_contenttyperesource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contenttyperesources', to=orm['auth.User'])),
        ))
        db.send_create_signal(u'pleiapp', ['ContentTypeResource'])

        # Adding M2M table for field types on 'ContentTypeResource'
        m2m_table_name = db.shorten_name(u'pleiapp_contenttyperesource_types')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contenttyperesource', models.ForeignKey(orm[u'pleiapp.contenttyperesource'], null=False)),
            ('type', models.ForeignKey(orm[u'pleiapp.type'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contenttyperesource_id', 'type_id'])

        # Adding M2M table for field topics on 'ContentTypeResource'
        m2m_table_name = db.shorten_name(u'pleiapp_contenttyperesource_topics')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contenttyperesource', models.ForeignKey(orm[u'pleiapp.contenttyperesource'], null=False)),
            ('topic', models.ForeignKey(orm[u'pleiapp.topic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contenttyperesource_id', 'topic_id'])

        # Adding M2M table for field categories on 'ContentTypeResource'
        m2m_table_name = db.shorten_name(u'pleiapp_contenttyperesource_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contenttyperesource', models.ForeignKey(orm[u'pleiapp.contenttyperesource'], null=False)),
            ('category', models.ForeignKey(orm[u'pleiapp.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contenttyperesource_id', 'category_id'])


    def backwards(self, orm):
        # Deleting model 'Topic'
        db.delete_table(u'pleiapp_topic')

        # Deleting model 'Type'
        db.delete_table(u'pleiapp_type')

        # Deleting model 'Category'
        db.delete_table(u'pleiapp_category')

        # Deleting model 'ContentTypeResource'
        db.delete_table(u'pleiapp_contenttyperesource')

        # Removing M2M table for field types on 'ContentTypeResource'
        db.delete_table(db.shorten_name(u'pleiapp_contenttyperesource_types'))

        # Removing M2M table for field topics on 'ContentTypeResource'
        db.delete_table(db.shorten_name(u'pleiapp_contenttyperesource_topics'))

        # Removing M2M table for field categories on 'ContentTypeResource'
        db.delete_table(db.shorten_name(u'pleiapp_contenttyperesource_categories'))


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'pleiapp.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'pleiapp.contenttyperesource': {
            'Meta': {'object_name': 'ContentTypeResource'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pleiapp.Category']", 'symmetrical': 'False'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'topics': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pleiapp.Topic']", 'symmetrical': 'False'}),
            'types': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pleiapp.Type']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contenttyperesources'", 'to': u"orm['auth.User']"})
        },
        u'pleiapp.topic': {
            'Meta': {'object_name': 'Topic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'pleiapp.type': {
            'Meta': {'object_name': 'Type'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['pleiapp']