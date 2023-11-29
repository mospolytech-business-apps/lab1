#!/bin/bash

python manage.py loaddata ./tickets/fixtures/tickets.json
python manage.py loaddata ./amenities/fixtures/amenitiesTickets.json
python manage.py loaddata ./amenities/fixtures/amenities.json
python manage.py loaddata ./amenities/fixtures/amenitiesCabinType.json
python manage.py loaddata ./aircrafts/fixtures/aircrafts.json
python manage.py loaddata ./office/fixtures/office.json
python manage.py loaddata ./airoutes/fixtures/airoutes.json
python manage.py loaddata ./schedules/fixtures/schedules.json
python manage.py loaddata ./survey/fixtures/survey.json
python manage.py loaddata ./authentication/fixtures/users.json
python manage.py loaddata ./country/fixtures/country.json
python manage.py loaddata ./airports/fixtures/airports.json
python manage.py loaddata ./cabintypes/fixtures/cabintypes.json
