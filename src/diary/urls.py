from django.urls import path

from . import views

app_name = 'diary'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('detail/<int:pk>', views.detail, name='detail'),

    path('class_view/', views.IndexView.as_view(), name='class_view_index'),
    path('class_view/add/', views.AddView.as_view(), name='class_view_add'),
    path('class_view/update/<int:pk>', views.UpdateView.as_view(), name='class_view_update'),
    path('class_view/delete/<int:pk>', views.DeleteView.as_view(), name='class_view_delete'),
    path('class_view/detail/<int:pk>', views.DetailView.as_view(), name='class_view_detail'),
]
