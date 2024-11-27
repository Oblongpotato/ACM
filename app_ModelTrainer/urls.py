from django.urls import path
from . import views


urlpatterns = [
    path('', views.TrainerInterface, name='trainer_interface'),
    path("rate-image/", views.rate_image, name="rate_image"),

]

