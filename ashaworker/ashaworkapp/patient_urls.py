from django.urls import path
from django.contrib.auth import views as auth_views
from ashaworkapp.patient_views import Patient_Index, Feedback_from_Patient, Ask_to_Doctor, Add_Details, Newly_Married, \
    Pregnant, Mother, Newlymarried, Patient_Profile

urlpatterns = [
    path('', Patient_Index.as_view()),
    path('feedback_from_patient', Feedback_from_Patient.as_view()),
    path('ask_to_doctor', Ask_to_Doctor.as_view()),
    path('add_details', Add_Details.as_view()),
    path('newly_married', Newlymarried.as_view()),
    path('pregnant', Pregnant.as_view()),
    path('mother', Mother.as_view()),
    path('profile', Patient_Profile.as_view()),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='/'
        ),
        name='logout'
    ),
]


def urls():
    return urlpatterns,'patient','patient'