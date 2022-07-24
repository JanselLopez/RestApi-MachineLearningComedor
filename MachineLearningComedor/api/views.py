#Django

from django.http import JsonResponse
from api.models import  InfoFood
from django.views.decorators.csrf import csrf_exempt

#ML
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import psycopg2 as psy
 
#dia de la semana actual
from datetime import datetime

# Create your views here.
@csrf_exempt
def make_prediction(request,actual_food_value):
    '''
    getting the values
    '''
    item = InfoFood.objects.all().values()
    con_string = "host = '127.0.0.1' port = '5433' dbname = 'comedor_ml' user = 'postgres' password = 'FzZ3v8vZLpu3kQG'"
    con_pos = psy.connect(con_string)
    DATASET = pd.read_sql("SELECT * FROM api_infofood",con_pos)
    x1, x2, y = DATASET['week_day'], DATASET['total_food_value'], DATASET['people_percentage']
    df = pd.DataFrame(item)
    '''
    model creation
    '''
    lin_reg = LinearRegression()
    lin_reg.fit(df[['week_day', 'total_food_value']], df['people_percentage'])
    '''
    for represent the plane
    '''
    X, Y = np.meshgrid(np.linspace(min(x1), max(x1), 10), np.linspace(min(x1), max(x2), 10))
    z = lin_reg.intercept_ + lin_reg.coef_[0] * X + lin_reg.coef_[1] * Y
    '''
    macking the prediction
    '''
    x_new = np.array([[datetime.today().weekday(), actual_food_value]])
    people = lin_reg.predict(x_new)

    '''
    representing the function in 3d
    '''
    ax = plt.axes(projection='3d')
    ax.scatter3D(x1, x2, y, color='red')
    ax.plot_surface(X, Y, z, alpha=0.75)
    ax.scatter(datetime.today().weekday(),actual_food_value,people[0],c='g',marker='o')
    plt.xlabel('week_day')
    plt.ylabel('food_value')
    plt.show()

    return JsonResponse(float(people[0]),safe=False)
  