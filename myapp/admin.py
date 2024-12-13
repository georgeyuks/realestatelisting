from email.message import Message

from django.contrib import admin
from myapp.models import User, Message, Book

# Register your models here.
admin.site.register(User)
admin.site.register(Message)
admin.site.register(Book)


