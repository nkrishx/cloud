import csv
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','cloud_app.settings')

import django
django.setup()

from cloud_application.models import AirPollution

def populate():
    csv_file='AirQuality.csv'
    with open (csv_file,'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            d, created = AirPollution.objects.get_or_create(country=row[0], state=row[1], city=row[2], place=row[3], pollutants=row[4])
            d.save()

if __name__ == "__main__":
    populate()