from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    data = JSONRenderer().render(serializer.data)
    return data


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data)
    if serializer.is_valid():
        return Car(**serializer.validated_data)
    return serializer.errors
