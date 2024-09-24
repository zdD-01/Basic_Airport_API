from rest_framework import serializers
from .models import Airline, Aircraft

class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ['manufacturer_serial_number', 'type', 'operator_airline', 'number_of_engines']

class AirlineSerializer(serializers.ModelSerializer):
    aircraft_set = AircraftSerializer(many=True, read_only=True)

    class Meta:
        model = Airline
        fields = ['name', 'callsign', 'founded_year', 'base_airport', 'aircraft_set']