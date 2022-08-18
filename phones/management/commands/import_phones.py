import csv
import re

from django.core.management.base import BaseCommand

from phones.models import Phones


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        with open('phones.csv', encoding='utf-8') as file:
            zapis = csv.reader(file, delimiter="\n")
            zapis_list = list(zapis)
        for i in range(1,len(zapis_list)):
            z = str(zapis_list[i])[2:-2]
            z = z.split(';')
            print(z)
            phone = Phones(
                id=z[0],
                name=z[1],
                price=z[3],
                image=z[2],
                release_date=z[4],
                lte_exist=z[5],
                slug=re.sub(r" ", r"_", str(z[1]))
            )
            phone.save()
        import this