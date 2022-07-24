from django.urls import path
from api.views import make_prediction

urlpatterns = [
    path('prediction/<int:actual_food_value>', make_prediction),
]