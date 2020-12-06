from mongoengine import *

class Posting(Document):
    post_id = StringField(required=True)
    im_640 = StringField(required=True, unique=True)
    likes = IntField(required=True)
    main_tag = StringField(required=True)
    locations = StringField(required=False, unique=False)
    #tags = ListField(StringField(), required=False)
    # caption = StringField(required=False, unique=False)
    contains = ListField(StringField(), required=False)
    timestamp = StringField(required=True, unique=False)
    username = StringField(required=True, unique=False)
    @queryset_manager
    def take_nyc(doc_cls, queryset):
        return queryset.filter(main_tag = 'nyc')