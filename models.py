# from datetime import datetime

# from scrapy.item import Item, Field
# from mongoengine import EmbeddedDocument, CASCADE
# from mongoengine.fields import (BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField,
#                                 IntField, ReferenceField)

# import connect

# class QuoteItem(Item):
#     quote = Field()
#     author = Field()
#     tags = Field()


# class AuthorItem(Item):
#     fullname = Field()
#     born_date = Field()
#     born_location = Field()
#     description = Field()

from datetime import datetime

from mongoengine import EmbeddedDocument, Document, CASCADE
from mongoengine.fields import (BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField,
                                IntField, ReferenceField)

import connect

class Author(Document):
    fullname = StringField(unique=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField()
