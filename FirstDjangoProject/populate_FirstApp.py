import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','FirstDjangoProject.settings')



import django
django.setup()



import random

from FirstApp.models import AccessRecord,Topic,Webpage
from faker import Faker

fakegen=Faker()
topics=['Search','Social','Marketplace','News','Games']


def add_topic():

    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):

    for entry in range(n):
        top = add_topic()

        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()


        webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]


        acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if  __name__ == '__main__' :
    print('populating script')
    populate(30)
    print("populating Complete")
