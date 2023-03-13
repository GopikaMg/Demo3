
from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:task_id>/', views.delete,name='delete'),
    path('update/<int:id>/', views.update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.Detailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.updateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.deleteview.as_view(),name='cbvdelete'),

    #path('details/',views.details,name='details')
]
