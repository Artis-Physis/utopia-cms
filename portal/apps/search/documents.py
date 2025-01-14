from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from core.models import Article


@registry.register_document
class ArticleDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'articles'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    get_absolute_url = fields.TextField(attr="get_absolute_url")
    get_type_display = fields.TextField(attr="get_type_display")
    get_lead = fields.TextField(attr="get_lead")
    section = fields.TextField()

    def prepare_section(self, instance):
        return instance.section.__unicode__() if instance.section else u''

    class Django:
        model = Article  # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'headline',
            'deck',
            'lead',
            'body',
            'home_lead',
            'is_published',
            'date_published',
            'type',
        ]

        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True

        # Don't perform an index refresh after every update (overrides global setting):
        # auto_refresh = False

        # Paginate the django queryset used to populate the index with the specified size
        # (by default it uses the database driver's default setting)
        # queryset_pagination = 5000
