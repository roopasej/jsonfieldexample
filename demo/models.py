from django.db import models
from jsonfieldexample import settings
from django.contrib.postgres.fields import JSONField

print(settings.LANGUAGES)
defualtdict={}

for i in settings.LANGUAGES:
    defualtdict[i[0]] = i[1]
print(defualtdict)


class Language(models.Model):

    title = models. JSONField('Article title', default=defualtdict)
