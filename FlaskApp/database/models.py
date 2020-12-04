from mongoengine import *
class Posting(Document):
    post_id = StringField(required=True)
    # display_url = StringField(required=True, unique=True)
    likes = IntField(required=True)
    main_tag = StringField(required=True)
    # location = db.StringField(required=False, unique=False)
    # tags = db.ListField(db.StringField(), required=False)
    # caption = db.StringField(required=False, unique=False)
    # accessibility_caption = db.ListField(db.StringField(), required=False)
    # timestamp = db.StringField(required=True, unique=False)
    # username = db.StringField(required=True, unique=False)
    @queryset_manager
    def take_nyc(doc_cls, queryset):
        return queryset.filter(main_tag = 'nyc')