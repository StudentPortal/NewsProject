from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="indexfile"),
    path('aboutus',views.about,name="aboutusfile"),
    path('sports.html',views.sports,name="sports"),
    path('business.html',views.business,name="business"),
    path('national.html',views.national,name="national"),
    path('world.html',views.world,name="world"),
    path('politics.html',views.politics,name="politics"),
    path('technology.html',views.technology,name="technology"),
    path('startup.html',views.startup,name="startup"),
    path('entertainment.html',views.entertainment,name="entertainment"),
    path('miscellaneous.html',views.miscellaneous,name="miscellaneous"),
    path('hatke.html',views.hatke,name="hatke"),
    path('science.html',views.science,name="science"),
    path('automobile.html',views.automobile,name="automobile")
]