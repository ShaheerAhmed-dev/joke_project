from django.urls import path, include
from .views import SignUpView, UserLoginView, logout_user, HomeView, NewJokeView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('home/', HomeView.as_view(), name='home'),
    path('new_joke/', NewJokeView.as_view(), name='new_joke'),
]
