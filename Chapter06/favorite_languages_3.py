#!/usr/bin/python

favorite_languages = {
    'jen':['python','Ruby'],
    'sarah':['c'],
    'edward':['ruby','Go'],
    'phil':['python','Haskell'],
    }

for name,languages in favorite_languages.items():
    if len(languages)>1:
        print(name.title()+"'s favorite language is:") 
        for language in languages:
            print("\t"+language.title())
    else:
        print(name.title()+"'s favorite language is: "+ languages[0].title())
         