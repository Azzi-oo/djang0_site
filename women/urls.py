from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('cats/<int:cat_id>/', views.categories, name="cats_id"),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name="cats"),
    re_path(r"^archieve/(?P<year>[0-9]{4})/", views.archieve, name="arcieve"),
]
