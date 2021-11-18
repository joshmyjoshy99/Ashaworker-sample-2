from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from ashaworkapp.ashaworker_views import Ashaworker_Index, Patient_Approve, Patient_View, \
    Patient_Details, Patient_RejectView, Patient_ApproveView, Feedback_to_Admin, Ashaworker_Profile, Child_Approve, \
    Child_RejectView, Child_ApproveView, Child_View, Child_Details

urlpatterns = [
    path('', Ashaworker_Index.as_view()),
    path('patient_app', Patient_Approve.as_view()),
    path('reject', Patient_RejectView.as_view()),
    path('approve', Patient_ApproveView.as_view()),
    path('patient_view', Patient_View.as_view()),
    path('patient_details', Patient_Details.as_view()),
    path('child_app', Child_Approve.as_view()),
    path('child_reject', Child_RejectView.as_view()),
    path('child_approve', Child_ApproveView.as_view()),
    path('child_view', Child_View.as_view()),
    path('child_details', Child_Details.as_view()),
    path('feedback_to_admin', Feedback_to_Admin.as_view()),
    path('profile', Ashaworker_Profile.as_view()),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='/'
    ),
         name='logout'
         ),

]



def urls():
    return urlpatterns,'ashaworker','ashaworker'