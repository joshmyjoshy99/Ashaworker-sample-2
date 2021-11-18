from django.urls import path
from django.contrib.auth import views as auth_views
from ashaworkapp.admin_views import Admin_Index, Doctor_Approve, Ashaworker_Approve, RejectView, ApproveView, \
    Doctor_View, Ashaworker_View, Doctor_Details, Ashaworker_Details, Feedback_View, Feedback_Patients, \
    Feedback_Ashaworker

urlpatterns = [
    path('', Admin_Index.as_view()),
    path('doctor_app', Doctor_Approve.as_view()),
    path('ashaworker_app', Ashaworker_Approve.as_view()),
    path('reject', RejectView.as_view()),
    path('approve', ApproveView.as_view()),
    path('doctor_view', Doctor_View.as_view()),
    path('doctor_details', Doctor_Details.as_view()),
    path('ashaworker_view', Ashaworker_View.as_view()),
    path('ashaworker_details', Ashaworker_Details.as_view()),
    path('feedback_view', Feedback_View.as_view()),
    path('feedback_patients', Feedback_Patients.as_view()),
    path('feedback_ashaworker', Feedback_Ashaworker.as_view()),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='/'
        ),
        name='logout'
    ),


]


def urls():
    return urlpatterns,'admin','admin'