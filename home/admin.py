from django.contrib import admin
from .models import Contact,Subscribe,Vote
# Register your models here.
admin.site.register(Contact)
admin.site.register(Subscribe)
admin.site.register(Vote)