from dataclasses import fields
from rest_framework import serializers
from api.models import InfoFood
class infoFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoFood
        fields =  ('week_day','total_food_value','people_percentage')