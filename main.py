import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(instance=car)
    json = JSONRenderer().render(serializer.data)
    return json


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    serializer_data = JSONParser().parse(stream)
    serializer = CarSerializer(data=serializer_data)

    if serializer.is_valid():
        serializer.save()
        return serializer.instance
    else:
        return serializer.errors
