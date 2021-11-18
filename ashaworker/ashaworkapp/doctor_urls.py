from django.urls import path
from django.contrib.auth import views as auth_views
from ashaworkapp.doctor_views import Doctor_Index, Profile, Answer, Tips_to_user

urlpatterns = [
    path('', Doctor_Index.as_view()),
    path('tips', Tips_to_user.as_view()),
    path('profile', Profile.as_view()),
    path('answer', Answer.as_view()),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='/'
        ),
        name='logout'
    ),

]


def urls():
    return urlpatterns,'doctor','doctor'