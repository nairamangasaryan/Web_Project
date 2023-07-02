from django.urls import path
from .views import newCV


urlpatterns = [
 
    path("", newCV),

]