from django.urls import path
from . import views


from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [

    
   path('register', views.UserCreate.as_view()),
   path('login/', views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
   path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

   
]
