from django.urls import path
from employee import views

app_name='employee'
urlpatterns=[

    path('',views.index,name='index'),
    path('emp/',views.emp,name='emp'),
    path('show/',views.show,name='show'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
]