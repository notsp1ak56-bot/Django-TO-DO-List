from django.urls  import path
from . import views
urlpatterns =[
    path('main/', views.main  , name = "main"),
    path('main/add/', views.add_tusk, name = "add"),
    path('main/edit/<int:tusk_id>/', views.edit_tusk, name = "edit"),
    path('main/delete<int:tusk_id>/', views.delete_tusk , name = "delete")
]