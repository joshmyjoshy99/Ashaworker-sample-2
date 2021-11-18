from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from ashaworkapp.models import PatientEntry, AshaworkerEntry, UserType, Feedback_Asha, Child_Module


class Ashaworker_Index(TemplateView):
    template_name = 'ashaworker/ashaworker_index.html'

class Patient_Approve(TemplateView):
    template_name = 'ashaworker/patient_approval.html'

    def get_context_data(self, **kwargs):
        context = super(Patient_Approve, self).get_context_data(**kwargs)

        new_patient = PatientEntry.objects.filter(user__last_name='0', user__is_staff='0', user__is_active='1')

        context['new_patient'] = new_patient
        return context

class Patient_RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'ashaworker/ashaworker_index.html',{'message':"Account Removed"})

class Patient_ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'ashaworker/ashaworker_index.html',{'message':" Account Approved"})

class Patient_View(TemplateView):
    template_name = 'ashaworker/patient_view.html'

    def get_context_data(self, **kwargs):
        context = super(Patient_View,self).get_context_data(**kwargs)
        patient = PatientEntry.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')
        context['patient'] = patient
        return context

class Patient_Details(TemplateView):
    template_name = 'ashaworker/patient_details.html'

    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = PatientEntry.objects.filter(user_id=id)
        return render(request,'ashaworker/patient_details.html',{'patient_info':user})

class Feedback_to_Admin(TemplateView):
    template_name = 'ashaworker/feedback_to_admin.html'

    def post(self, request, *args, **kwargs):
        message = request.POST['feedback']
        ashaworker = AshaworkerEntry.objects.get(user_id=self.request.user.id)
        user = UserType.objects.get(user_id=self.request.user.id)
        feedback = Feedback_Asha()
        feedback.feedback = message
        feedback.ashaworker = ashaworker
        feedback.user = user
        feedback.status = "not replied"
        feedback.save()
        return render(request,'ashaworker/feedback_to_admin.html',{'message':" Feedback sent"})

class Ashaworker_Profile(TemplateView):
    template_name = 'ashaworker/profile.html'

    def get_context_data(self, **kwargs):
        context = super(Ashaworker_Profile, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        if self.request.user.is_active:
            ashaworker = AshaworkerEntry.objects.get(user_id=self.request.user.id)
            context['ashaworker'] = ashaworker
        return context
    def post(self,request, *args, **kwargs):
        user = User.objects.get(id=self.request.user.id)
        ashaworker = AshaworkerEntry.objects.get(user_id=self.request.user.id)
        if request.POST['profile'] == "profile":
            ashaworker.contact = request.POST['contact']
            ashaworker.ward = request.POST['ward']
            ashaworker.panchayath = request.POST['panchayath']
            ashaworker.street = request.POST['street']
            ashaworker.city = request.POST['city']
            ashaworker.dob = request.POST['dob']
            ashaworker.husname = request.POST['husname']
            ashaworker.profilepic = request.POST['profilepic']
            ashaworker.save()
            return render(request, 'ashaworker/profile.html', {'message': "Profile Updated"})
        else:
            user.username = request.POST['username']
            user.set_password(request.POST['password'])
            user.save()
            return render(request, 'ashaworker/profile.html', {'message': "Updated Username and Password"})


class Child_Approve(TemplateView):
    template_name = 'ashaworker/child_approval.html'

    def get_context_data(self, **kwargs):
        context = super(Child_Approve, self).get_context_data(**kwargs)

        new_child = Child_Module.objects.all()

        context['new_child'] = new_child
        return context

class Child_RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'ashaworker/ashaworker_index.html',{'message':"Account Removed"})

class Child_ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'ashaworker/ashaworker_index.html',{'message':" Account Approved"})

class Child_View(TemplateView):
    template_name = 'ashaworker/child_view.html'

    def get_context_data(self, **kwargs):
        context = super(Child_View,self).get_context_data(**kwargs)
        child = Child_Module.objects.all()
        context['child'] = child
        return context

class Child_Details(TemplateView):
    template_name = 'ashaworker/child_details.html'

    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = Child_Module.objects.filter(user_id=id)
        return render(request,'ashaworker/child_details.html',{'child_info':user})
