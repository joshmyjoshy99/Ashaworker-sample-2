from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from ashaworkapp.models import DoctorEntry, AshaworkerEntry, Feedback_Asha, Feedback_User


class Admin_Index(TemplateView):
    template_name = 'admin/admin_index.html'

class Doctor_Approve(TemplateView):
    template_name = 'admin/doctor_approval.html'

    def get_context_data(self, **kwargs):
        context = super(Doctor_Approve, self).get_context_data(**kwargs)

        new_doctor = DoctorEntry.objects.filter(user__last_name='0', user__is_staff='0', user__is_active='1')

        context['new_doctor'] = new_doctor
        return context

class Ashaworker_Approve(TemplateView):
    template_name = 'admin/ashaworker_approval.html'

    def get_context_data(self, **kwargs):
        context = super(Ashaworker_Approve, self).get_context_data(**kwargs)

        new_ashaworker = AshaworkerEntry.objects.filter(user__last_name='0', user__is_staff='0', user__is_active='1')

        context['new_ashaworker'] = new_ashaworker
        return context

class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})

class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/admin_index.html',{'message':" Account Approved"})

class Doctor_View(TemplateView):
    template_name = 'admin/doctor_view.html'

    def get_context_data(self, **kwargs):
        context = super(Doctor_View,self).get_context_data(**kwargs)
        doctor = DoctorEntry.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')
        context['doctor'] = doctor
        return context

class Doctor_Details(TemplateView):
    template_name = 'admin/doctor_details.html'

    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = DoctorEntry.objects.filter(user_id=id)
        return render(request,'admin/doctor_details.html',{'doctor_info':user})

class Ashaworker_View(TemplateView):
    template_name = 'admin/ashaworker_view.html'

    def get_context_data(self, **kwargs):
        context = super(Ashaworker_View,self).get_context_data(**kwargs)
        ashaworker = AshaworkerEntry.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')
        context['ashaworker'] = ashaworker
        return context

class Ashaworker_Details(TemplateView):
    template_name = 'admin/ashaworker_details.html'

    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = AshaworkerEntry.objects.filter(user_id=id)
        return render(request,'admin/ashaworker_details.html',{'ashaworker_info':user})

class Feedback_View(TemplateView):
    template_name = 'admin/feedback_view.html'

class Feedback_Patients(TemplateView):
    template_name = 'admin/feedback_patients.html'

    def get_context_data(self,*args, **kwargs):
        context = super(Feedback_Patients, self).get_context_data(**kwargs)
        feedback = Feedback_User.objects.all()
        context['feed'] = feedback
        return context
    def post(self,request,*args,**kwargs):
        feedb = request.POST['reply']
        iid = request.POST['iid']
        feed = Feedback_User.objects.get(id=iid)
        feed.reply = feedb
        feed.status = "replied"
        feed.save()
        return redirect(request.META['HTTP_REFERER'])

class Feedback_Ashaworker(TemplateView):
    template_name = 'admin/feedback_ashaworker.html'

    def get_context_data(self, **kwargs):
        context = super(Feedback_Ashaworker, self).get_context_data(**kwargs)
        feedback = Feedback_Asha.objects.all()
        context['feed'] = feedback
        return context
    def post(self,request,*args,**kwargs):
        feedb = request.POST['reply']
        iid = request.POST['iid']
        feed = Feedback_Asha.objects.get(id=iid)
        feed.reply = feedb
        feed.status = "replied"
        feed.save()
        return redirect(request.META['HTTP_REFERER'])