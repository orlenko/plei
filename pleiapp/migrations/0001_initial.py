# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Resource'
        db.create_table(u'pleiapp_resource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords_string', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('_meta_title', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gen_description', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('short_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('in_sitemap', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='resources', to=orm['auth.User'])),
            ('author', self.gf('django.db.models.fields.CharField')(default='', max_length=1024, blank=True)),
            ('featured_image', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('keywords', self.gf('mezzanine.generic.fields.KeywordsField')(object_id_field='object_pk', to=orm['generic.AssignedKeyword'], frozen_by_south=True)),
        ))
        db.send_create_signal(u'pleiapp', ['Resource'])

        # Adding M2M table for field categories on 'Resource'
        m2m_table_name = db.shorten_name(u'pleiapp_resource_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resource', models.ForeignKey(orm[u'pleiapp.resource'], null=False)),
            ('category', models.ForeignKey(orm[u'pleiapp.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['resource_id', 'category_id'])

        # Adding M2M table for field topics on 'Resource'
        m2m_table_name = db.shorten_name(u'pleiapp_resource_topics')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resource', models.ForeignKey(orm[u'pleiapp.resource'], null=False)),
            ('topic', models.ForeignKey(orm[u'pleiapp.topic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['resource_id', 'topic_id'])

        # Adding M2M table for field types on 'Resource'
        m2m_table_name = db.shorten_name(u'pleiapp_resource_types')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resource', models.ForeignKey(orm[u'pleiapp.resource'], null=False)),
            ('type', models.ForeignKey(orm[u'pleiapp.type'], null=False))
        ))
        db.create_unique(m2m_table_name, ['resource_id', 'type_id'])

        # Adding M2M table for field related_resources on 'Resource'
        m2m_table_name = db.shorten_name(u'pleiapp_resource_related_resources')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_resource', models.ForeignKey(orm[u'pleiapp.resource'], null=False)),
            ('to_resource', models.ForeignKey(orm[u'pleiapp.resource'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_resource_id', 'to_resource_id'])

        # Adding M2M table for field related_dictionary on 'Resource'
        m2m_table_name = db.shorten_name(u'pleiapp_resource_related_dictionary')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resource', models.ForeignKey(orm[u'pleiapp.resource'], null=False)),
            ('dictionary', models.ForeignKey(orm[u'pleiapp.dictionary'], null=False))
        ))
        db.create_unique(m2m_table_name, ['resource_id', 'dictionary_id'])

        # Adding M2M table for field related_faqs on 'Resource'
        m2m_table_name = db.shorten_name(u'pleiapp_resource_related_faqs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resource', models.ForeignKey(orm[u'pleiapp.resource'], null=False)),
            ('faq', models.ForeignKey(orm[u'pleiapp.faq'], null=False))
        ))
        db.create_unique(m2m_table_name, ['resource_id', 'faq_id'])

        # Adding model 'Faq'
        db.create_table(u'pleiapp_faq', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords_string', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('_meta_title', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gen_description', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('short_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('in_sitemap', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='faqs', to=orm['auth.User'])),
            ('author', self.gf('django.db.models.fields.CharField')(default='', max_length=1024, blank=True)),
            ('featured_image', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('keywords', self.gf('mezzanine.generic.fields.KeywordsField')(object_id_field='object_pk', to=orm['generic.AssignedKeyword'], frozen_by_south=True)),
        ))
        db.send_create_signal(u'pleiapp', ['Faq'])

        # Adding M2M table for field categories on 'Faq'
        m2m_table_name = db.shorten_name(u'pleiapp_faq_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('faq', models.ForeignKey(orm[u'pleiapp.faq'], null=False)),
            ('category', models.ForeignKey(orm[u'pleiapp.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['faq_id', 'category_id'])

        # Adding M2M table for field topics on 'Faq'
        m2m_table_name = db.shorten_name(u'pleiapp_faq_topics')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('faq', models.ForeignKey(orm[u'pleiapp.faq'], null=False)),
            ('topic', models.ForeignKey(orm[u'pleiapp.topic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['faq_id', 'topic_id'])

        # Adding M2M table for field types on 'Faq'
        m2m_table_name = db.shorten_name(u'pleiapp_faq_types')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('faq', models.ForeignKey(orm[u'pleiapp.faq'], null=False)),
            ('type', models.ForeignKey(orm[u'pleiapp.type'], null=False))
        ))
        db.create_unique(m2m_table_name, ['faq_id', 'type_id'])

        # Adding M2M table for field related_faqs on 'Faq'
        m2m_table_name = db.shorten_name(u'pleiapp_faq_related_faqs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_faq', models.ForeignKey(orm[u'pleiapp.faq'], null=False)),
            ('to_faq', models.ForeignKey(orm[u'pleiapp.faq'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_faq_id', 'to_faq_id'])

        # Adding M2M table for field related_dictionary on 'Faq'
        m2m_table_name = db.shorten_name(u'pleiapp_faq_related_dictionary')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('faq', models.ForeignKey(orm[u'pleiapp.faq'], null=False)),
            ('dictionary', models.ForeignKey(orm[u'pleiapp.dictionary'], null=False))
        ))
        db.create_unique(m2m_table_name, ['faq_id', 'dictionary_id'])

        # Adding model 'Dictionary'
        db.create_table(u'pleiapp_dictionary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords_string', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('_meta_title', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gen_description', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('short_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('in_sitemap', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='dictionarys', to=orm['auth.User'])),
            ('author', self.gf('django.db.models.fields.CharField')(default='', max_length=1024, blank=True)),
            ('featured_image', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('keywords', self.gf('mezzanine.generic.fields.KeywordsField')(object_id_field='object_pk', to=orm['generic.AssignedKeyword'], frozen_by_south=True)),
        ))
        db.send_create_signal(u'pleiapp', ['Dictionary'])

        # Adding M2M table for field categories on 'Dictionary'
        m2m_table_name = db.shorten_name(u'pleiapp_dictionary_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dictionary', models.ForeignKey(orm[u'pleiapp.dictionary'], null=False)),
            ('category', models.ForeignKey(orm[u'pleiapp.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dictionary_id', 'category_id'])

        # Adding M2M table for field topics on 'Dictionary'
        m2m_table_name = db.shorten_name(u'pleiapp_dictionary_topics')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dictionary', models.ForeignKey(orm[u'pleiapp.dictionary'], null=False)),
            ('topic', models.ForeignKey(orm[u'pleiapp.topic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dictionary_id', 'topic_id'])

        # Adding M2M table for field types on 'Dictionary'
        m2m_table_name = db.shorten_name(u'pleiapp_dictionary_types')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dictionary', models.ForeignKey(orm[u'pleiapp.dictionary'], null=False)),
            ('type', models.ForeignKey(orm[u'pleiapp.type'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dictionary_id', 'type_id'])

        # Adding M2M table for field related_dictionary on 'Dictionary'
        m2m_table_name = db.shorten_name(u'pleiapp_dictionary_related_dictionary')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_dictionary', models.ForeignKey(orm[u'pleiapp.dictionary'], null=False)),
            ('to_dictionary', models.ForeignKey(orm[u'pleiapp.dictionary'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_dictionary_id', 'to_dictionary_id'])

        # Adding model 'FrontPageItem'
        db.create_table(u'pleiapp_frontpageitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('featured_image', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'pleiapp', ['FrontPageItem'])

        # Adding model 'Category'
        db.create_table(u'pleiapp_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('visible', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
        ))
        db.send_create_signal(u'pleiapp', ['Category'])

        # Adding model 'Type'
        db.create_table(u'pleiapp_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('visible', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
        ))
        db.send_create_signal(u'pleiapp', ['Type'])

        # Adding model 'Topic'
        db.create_table(u'pleiapp_topic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('visible', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
        ))
        db.send_create_signal(u'pleiapp', ['Topic'])


    def backwards(self, orm):
        # Deleting model 'Resource'
        db.delete_table(u'pleiapp_resource')

        # Removing M2M table for field categories on 'Resource'
        db.delete_table(db.shorten_name(u'pleiapp_resource_categories'))

        # Removing M2M table for field topics on 'Resource'
        db.delete_table(db.shorten_name(u'pleiapp_resource_topics'))

        # Removing M2M table for field types on 'Resource'
        db.delete_table(db.shorten_name(u'pleiapp_resource_types'))

        # Removing M2M table for field related_resources on 'Resource'
        db.delete_table(db.shorten_name(u'pleiapp_resource_related_resources'))

        # Removing M2M table for field related_dictionary on 'Resource'
        db.delete_table(db.shorten_name(u'pleiapp_resource_related_dictionary'))

        # Removing M2M table for field related_faqs on 'Resource'
        db.delete_table(db.shorten_name(u'pleiapp_resource_related_faqs'))

        # Deleting model 'Faq'
        db.delete_table(u'pleiapp_faq')

        # Removing M2M table for field categories on 'Faq'
        db.delete_table(db.shorten_name(u'pleiapp_faq_categories'))

        # Removing M2M table for field topics on 'Faq'
        db.delete_table(db.shorten_name(u'pleiapp_faq_topics'))

        # Removing M2M table for field types on 'Faq'
        db.delete_table(db.shorten_name(u'pleiapp_faq_types'))

        # Removing M2M table for field related_faqs on 'Faq'
        db.delete_table(db.shorten_name(u'pleiapp_faq_related_faqs'))

        # Removing M2M table for field related_dictionary on 'Faq'
        db.delete_table(db.shorten_name(u'pleiapp_faq_related_dictionary'))

        # Deleting model 'Dictionary'
        db.delete_table(u'pleiapp_dictionary')

        # Removing M2M table for field categories on 'Dictionary'
        db.delete_table(db.shorten_name(u'pleiapp_dictionary_categories'))

        # Removing M2M table for field topics on 'Dictionary'
        db.delete_table(db.shorten_name(u'pleiapp_dictionary_topics'))

        # Removing M2M table for field types on 'Dictionary'
        db.delete_table(db.shorten_name(u'pleiapp_dictionary_types'))

        # Removing M2M table for field related_dictionary on 'Dictionary'
        db.delete_table(db.shorten_name(u'pleiapp_dictionary_related_dictionary'))

        # Deleting model 'FrontPageItem'
        db.delete_table(u'pleiapp_frontpageitem')

        # Deleting model 'Category'
        db.delete_table(u'pleiapp_category')

        # Deleting model 'Type'
        db.delete_table(u'pleiapp_type')

        # Deleting model 'Topic'
        db.delete_table(u'pleiapp_topic')


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
        u'generic.assignedkeyword': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'AssignedKeyword'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assignments'", 'to': u"orm['generic.Keyword']"}),
            'object_pk': ('django.db.models.fields.IntegerField', [], {})
        },
        u'generic.keyword': {
            'Meta': {'object_name': 'Keyword'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'pleiapp.category': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'visible': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'})
        },
        u'pleiapp.dictionary': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Dictionary'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'dicts'", 'blank': 'True', 'to': u"orm['pleiapp.Category']"}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'featured_image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'keywords': ('mezzanine.generic.fields.KeywordsField', [], {'object_id_field': "'object_pk'", 'to': u"orm['generic.AssignedKeyword']", 'frozen_by_south': 'True'}),
            'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'related_dictionary': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_dictionary_rel_+'", 'blank': 'True', 'to': u"orm['pleiapp.Dictionary']"}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'topics': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'dicts'", 'blank': 'True', 'to': u"orm['pleiapp.Topic']"}),
            'types': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'dicts'", 'blank': 'True', 'to': u"orm['pleiapp.Type']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dictionarys'", 'to': u"orm['auth.User']"})
        },
        u'pleiapp.faq': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Faq'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'faqs'", 'blank': 'True', 'to': u"orm['pleiapp.Category']"}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'featured_image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'keywords': ('mezzanine.generic.fields.KeywordsField', [], {'object_id_field': "'object_pk'", 'to': u"orm['generic.AssignedKeyword']", 'frozen_by_south': 'True'}),
            'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'related_dictionary': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'related_faqs'", 'blank': 'True', 'to': u"orm['pleiapp.Dictionary']"}),
            'related_faqs': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_faqs_rel_+'", 'blank': 'True', 'to': u"orm['pleiapp.Faq']"}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'topics': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'faqs'", 'blank': 'True', 'to': u"orm['pleiapp.Topic']"}),
            'types': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'faqs'", 'blank': 'True', 'to': u"orm['pleiapp.Type']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'faqs'", 'to': u"orm['auth.User']"})
        },
        u'pleiapp.frontpageitem': {
            'Meta': {'object_name': 'FrontPageItem'},
            'featured_image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'pleiapp.resource': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Resource'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'resources'", 'blank': 'True', 'to': u"orm['pleiapp.Category']"}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'featured_image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'keywords': ('mezzanine.generic.fields.KeywordsField', [], {'object_id_field': "'object_pk'", 'to': u"orm['generic.AssignedKeyword']", 'frozen_by_south': 'True'}),
            'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'related_dictionary': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'related_resources'", 'blank': 'True', 'to': u"orm['pleiapp.Dictionary']"}),
            'related_faqs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'related_resources'", 'blank': 'True', 'to': u"orm['pleiapp.Faq']"}),
            'related_resources': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_resources_rel_+'", 'blank': 'True', 'to': u"orm['pleiapp.Resource']"}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'topics': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'resources'", 'blank': 'True', 'to': u"orm['pleiapp.Topic']"}),
            'types': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'resources'", 'blank': 'True', 'to': u"orm['pleiapp.Type']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'resources'", 'to': u"orm['auth.User']"})
        },
        u'pleiapp.topic': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Topic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'visible': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'})
        },
        u'pleiapp.type': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Type'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'visible': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['pleiapp']