from django.test import TestCase
from jsonfieldexample.demo.models import Language
from jsonfieldexample import settings

print(settings.LANGUAGES)
defualtdict={}

for i in settings.LANGUAGES:
    defualtdict[i[0]] = i[1]
print(defualtdict)

class ModelsTestCase(TestCase):
        def test_languages(self):
            """test for creating record in model"""
            language = Language.objects.create(title=defualtdict)
            language.save()
            self.assertEqual(language, language.title)