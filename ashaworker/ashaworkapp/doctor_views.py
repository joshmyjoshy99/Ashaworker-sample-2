from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView

from ashaworkapp.models import DoctorEntry, Tips


class Doctor_Index(TemplateView):
    template_name = 'doctor/doctor_index.html'

class Tips_to_user(TemplateView):
    template_name = 'doctor/tips.html'

    def post(self,request,*args,**kwargs):
        doctortips = request.POST['tips']
        doctor = DoctorEntry.objects.get(user_id=self.request.user.id)
        tip = Tips()
        tip.tips = doctortips
        tip.doctor = doctor
        tip.save()
        return render(request, 'doctor/tips.html')

class Profile(TemplateView):
    template_name = 'doctor/profile.html'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        if self.request.user.is_active:
            doctor = DoctorEntry.objects.get(user_id=self.request.user.id)
            context['doctor'] = doctor
        return context
    def post(self,request, *args, **kwargs):
        user = User.objects.get(id=self.request.user.id)
        doctor = DoctorEntry.objects.get(user_id=self.request.user.id)
        if request.POST['profile'] == "profile":
            doctor.contact = request.POST['contact']
            doctor.idcard = request.FILES['idcard']
            doctor.image = request.FILES['image']
            doctor.qualification = request.FILES['qualification']
            doctor.save()
            return render(request, 'doctor/profile.html', {'message': "Profile Updated"})
        else:
            user.username = request.POST['username']
            user.set_password(request.POST['password'])
            user.save()
            return render(request, 'doctor/profile.html', {'message': "Updated Username and Password"})



class Answer(TemplateView):
    template_name = 'doctor/answer_doctor.html'

