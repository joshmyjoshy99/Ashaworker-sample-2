from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.views.generic import TemplateView

from ashaworkapp.models import PatientEntry, UserType, Feedback_User, AskDoctor, Child_Module, Preg_Women, \
    Newly_Married, DoctorEntry, Tips


class Patient_Index(TemplateView):
    template_name = 'patient/patient_index.html'

    def get_context_data(self, **kwargs):
        context = super(Patient_Index, self).get_context_data(**kwargs)
        tip = Tips.objects.all()
        context['tipss'] = tip
        return context

class Feedback_from_Patient(TemplateView):
    template_name = 'patient/feedback_from_patient.html'

    def post(self, request, *args, **kwargs):
        message = request.POST['feedback']
        patients = PatientEntry.objects.get(user_id=self.request.user.id)
        user = UserType.objects.get(user_id=self.request.user.id)
        feedback = Feedback_User()
        feedback.feedback = message
        feedback.patients = patients
        feedback.user = user
        feedback.status = "not replied"
        feedback.save()
        return render(request,'patient/feedback_from_patient.html',{'message':" Feedback sent"})

class Ask_to_Doctor(TemplateView):
    template_name = 'patient/ask_to_doctor.html'

    def get_context_data(self,*args, **kwargs):
        context = super(Ask_to_Doctor, self).get_context_data(**kwargs)
        # user = self.request.user.id
        doctor = UserType.objects.filter(type='doctor')
        context['doc'] = doctor
        return context

    def post(self,request,*args,**kwargs):
        question = request.POST['question']
        assign = request.POST['assign']
        # doctor = DoctorEntry.objects.get(user_id=self.request.user.id)
        patients = PatientEntry.objects.get(user_id=self.request.user.id)
        user = UserType.objects.get(user_id=self.request.user.id)
        ask = AskDoctor()
        ask.question = question
        ask.assign = assign
        # ask.doctor = doctor
        ask.patients = patients
        ask.user = user
        ask.save()
        return render(request, 'patient/ask_to_doctor.html', {'message': " Feedback sent"})

class Add_Details(TemplateView):
    template_name = 'patient/add_details.html'

class Newlymarried(TemplateView):
    template_name = 'patient/newly_married.html'

    def post(self,request,*args,**kwargs):
        oldpanchayath = request.POST['oldpanchayath']
        oldstreet = request.POST['oldstreet']
        oldwardno = request.POST['oldwardno']
        medicines = request.POST['medicines']
        patients = PatientEntry.objects.get(user_id=self.request.user.id)
        # user = User.objects.get(user_id=self.request.user.id)
        newly = Newly_Married()
        newly.oldpanchayath = oldpanchayath
        newly.oldstreet = oldstreet
        newly.oldwardno = oldwardno
        newly.medicines = medicines
        newly.patients = patients
        # newly.user = user
        newly.save()
        return render(request, 'patient/newly_married.html', {'message': "Registered"})


class Pregnant(TemplateView):
    template_name = 'patient/pregnant.html'

    def post(self,request,*args,**kwargs):
        startdate = request.POST['startdate']
        firstcheckup = request.POST['firstcheckup']
        hospitalname = request.POST['hospitalname']
        patients = PatientEntry.objects.get(user_id=self.request.user.id)
        # user = UserType.objects.get(user__id=self.request.user.id)
        pregnant = Preg_Women()
        pregnant.startdate = startdate
        pregnant.firstcheckup = firstcheckup
        pregnant.hospitalname = hospitalname
        pregnant.patients = patients
        # pregnant.user = user
        pregnant.save()
        return render(request, 'patient/pregnant.html', {'message': "Registered" })

class Mother(TemplateView):
    template_name = 'patient/mother.html'

    def post(self,request,*args,**kwargs):
        name = request.POST['name']
        dob = request.POST['dob']
        hospitalname = request.POST['hospitalname']
        place = request.POST['place']
        gender = request.POST['gender']
        firstvaccinedate = request.POST['firstvaccinedate']
        birthcertificate = request.FILES['birthcertificate']
        fil = FileSystemStorage()
        birthcertificate = fil.save(birthcertificate.name, birthcertificate)
        patients = PatientEntry.objects.get(user_id=self.request.user.id)
        # user = User.objects.get(user_id=self.request.user.id)
        mother = Child_Module()
        mother.name = name
        mother.dob = dob
        mother.hospitalname = hospitalname
        mother.place = place
        mother.gender = gender
        mother.firstvaccinedate = firstvaccinedate
        mother.birthcertificate = birthcertificate
        mother.patients = patients
        # mother.user_id = user
        mother.save()
        return render(request, 'patient/mother.html', {'message': "Registered"})


class Patient_Profile(TemplateView):
    template_name = 'patient/profile.html'

    def get_context_data(self, **kwargs):
        context = super(Patient_Profile, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        if self.request.user.is_active:
            patients = PatientEntry.objects.get(user_id=self.request.user.id)
            context['patients'] = patients
        return context
    def post(self,request,*args,**kwargs):
        user = User.objects.get(id=self.request.user.id)
        patients = PatientEntry.objects.get(user_id=self.request.user.id)
        if request.POST['profile'] == "profile":
            patients.contact = request.POST['contact']
            patients.wardno = request.POST['wardno']
            patients.panchayath = request.POST['panchayath']
            patients.street = request.POST['street']
            patients.city = request.POST['city']
            patients.dob = request.POST['dob']
            patients.fahusname = request.POST['fahusname']
            patients.fahusno = request.POST['fahusno']
            patients.noofchild = request.POST['noofchild']
            patients.image = request.POST['image']
            patients.address = request.POST['address']
            patients.age = request.POST['age']
            patients.job = request.POST['job']
            patients.medicines = request.POST['medicines']
            patients.save()
            return render(request, 'patient/profile.html', {'message': "Profile Updated"})
        else:
            user.username = request.POST['username']
            user.set_password(request.POST['password'])
            user.save()
            return render(request, 'patient/profile.html', {'message': "Updated Username and Password"})
