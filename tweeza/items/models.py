from extensions import db
from users.models import User
import datetime


class Meta(db.EmbeddedDocument):

    title = db.StringField()
    short_description = db.StringField()
    lang = db.StringField(max_length=3)


class Category(db.Document):

    created_at = db.DateTimeField(default=datetime.datetime.now,
                                  required=True)
    name_ar = db.StringField(max_length=50)
    name_fr = db.StringField(max_length=50)
    name_en = db.StringField(max_length=50)
    description = db.StringField()
   

class Item(db.Document):

    item_id = db.SequenceField(primary_key=True)

    submitted_at = db.DateTimeField(default=datetime.datetime.now,
                                    required=True)

    meta_info = db.ListField(db.EmbeddedDocumentField(Meta),
                             required=True)

    submitter = db.ReferenceField(User)

    category = db.ReferenceField(Category)

    item_data = db.ListField(db.StringField())

    vcs_url = db.URLField()

    tags = db.ListField(db.StringField(max_length=30))

    description = db.StringField()

    thumbnail_path = db.StringField()

    license_name = db.StringField(max_length=50)
