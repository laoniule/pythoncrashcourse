#！/usr/bin/pyhton

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'Python'
favorite_languages['sarah'] = 'C'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'Python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ",")
