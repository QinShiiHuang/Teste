from django.urls import path
from . import views
urlpatterns = [
    path('',views.cadastrados),
    path('<int:id>', views.consulta_att_delete)
]
