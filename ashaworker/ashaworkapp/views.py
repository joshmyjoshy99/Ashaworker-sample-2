from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView

from ashaworkapp.models import UserType, PatientEntry, DoctorEntry, AshaworkerEntry


class Index_View(TemplateView):
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self,request,*args,**kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        det = User.objects.get(id=1)
        det.last_name = 1
        det.save()

        if user is not None:
            login(request,user)
            if user.last_name == '1':

                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "patient":
                    return redirect('/patient')
                elif UserType.objects.get(user_id=user.id).type == "doctor":
                    return redirect('/doctor')
                else:
                    return redirect('/ashaworker')
            else:
                return render(request, 'login.html',{'message': "User account not authenticate" })
        else:
            return render(request, 'login.html', {'message': "Invalid username or password" })




class Patient_Reg(TemplateView):
    template_name = 'patient_reg.html'
    def post(self,request,*args,**kwargs):
        fullname = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        wardno = request.POST['wardno']
        dob = request.POST['dob']
        adharno = request.POST['adharno']
        contact = request.POST['contact']
        panchayath = request.POST['panchayath']
        street = request.POST['street']
        city = request.POST['city']
        status = request.POST['status']
        fahusname = request.POST['fahusname']
        fahusno = request.POST['fahusno']
        noofchild = request.POST['noofchild']
        image = request.FILES['image']
        fi = FileSystemStorage()
        files = fi.save(image.name, image)
        password = request.POST['password']
        confirmpassword = request.POST['password2']
        try:
            user = User.objects.create_user(username=username,first_name=fullname,email=email,password=password,is_staff='0',last_name='0')
            user.save()
            Patient_Reg = PatientEntry()
            Patient_Reg.user = user
            Patient_Reg.password2 = confirmpassword
            Patient_Reg.contact = contact
            Patient_Reg.adharno = adharno
            Patient_Reg.wardno = wardno
            Patient_Reg.panchayath = panchayath
            Patient_Reg.street = street
            Patient_Reg.city = city
            Patient_Reg.dob = dob
            Patient_Reg.fahusname = fahusname
            Patient_Reg.fahusno = fahusno
            Patient_Reg.noofchild = noofchild
            Patient_Reg.status = status
            Patient_Reg.image = files
            Patient_Reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "patient"
            usertype.save()
            return redirect('/')
        except:
            messages = "Enter another username"
            return render(request, 'index,html',{'messages': messages})


class Doctor_Reg(TemplateView):
    template_name = 'doctor_reg.html'
    def post(self,request,*args,**kwargs):
        fullname = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        dob = request.POST['dob']
        contact = request.POST['contact']
        adharno = request.POST['adharno']
        image = request.FILES['image']
        fi = FileSystemStorage()
        files = fi.save(image.name, image)
        idcard = request.FILES['idcard']
        fil = FileSystemStorage()
        idcard = fil.save(idcard.name, idcard)
        qualification = request.FILES['qualification']
        file = FileSystemStorage()
        qualification = file.save(qualification.name, qualification)
        password = request.POST['password']
        confirmpassword = request.POST['password2']
        try:
            user = User.objects.create_user(username=username, first_name=fullname,email=email,password=password,is_staff='0',last_name='0')
            user.save()
            Doctor_Reg = DoctorEntry()
            Doctor_Reg.user = user
            Doctor_Reg.password2 = confirmpassword
            Doctor_Reg.dob = dob
            Doctor_Reg.contact = contact
            Doctor_Reg.adharno = adharno
            Doctor_Reg.image = files
            Doctor_Reg.idcard = idcard
            Doctor_Reg.qualification = qualification
            Doctor_Reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "doctor"
            usertype.save()
            return redirect('/')
        except:
            messages = "Enter another username"
            return render(request, 'index.html', {'messages': messages})

class Ashaworker_Reg(TemplateView):
    template_name = 'ashaworker_reg.html'

    def post(self,request,*args,**kwargs):
        fullname = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        dob = request.POST['dob']
        contact = request.POST['contact']
        adharcard = request.FILES['adharcard']
        fi = FileSystemStorage()
        files = fi.save(adharcard.name, adharcard)
        idcard = request.FILES['idcard']
        fil = FileSystemStorage()
        idcard = fil.save(idcard.name,idcard)
        profilepic = request.FILES['profilepic']
        pic = FileSystemStorage()
        profilepic = pic.save(profilepic.name, profilepic)
        password = request.POST['password']
        confirmpassword = request.POST['password2']
        try:
            user = User.objects.create_user(username=username, first_name=fullname, email=email, password=password,
                                            is_staff='0', last_name='0')
            user.save()
            Ashaworker_Reg = AshaworkerEntry()
            Ashaworker_Reg.user = user
            Ashaworker_Reg.dob = dob
            Ashaworker_Reg.contact = contact
            Ashaworker_Reg.adharcard = files
            Ashaworker_Reg.idcard = idcard
            Ashaworker_Reg.profilepic = profilepic
            Ashaworker_Reg.password2 = confirmpassword
            Ashaworker_Reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "ashaworker"
            usertype.save()
            return redirect('/')
        except:
            messages = "Enter another username"
            return render(request, 'index.html', {'messages': messages})


class Services(TemplateView):
    template_name = 'services.html'

class Forgot(TemplateView):
    template_name = 'forgot.html'

    def post(self,request,*args,**kwargs):
        username = request.POST['username']
        email = request.POST['email']
        user = authenticate(username=username, email=email)

        det = User.objects.get(id=1)
        det.last_name = 1
        det.save()

        if user is not None:
            login(request, user)
            if user.last_name == '1':

                if UserType.objects.get(user_id=user.id).type == "patient":
                    return redirect('/patient')
                elif UserType.objects.get(user_id=user.id).type == "doctor":
                    return redirect('/doctor')
                else:
                    return redirect('/ashaworker')
            else:
                return render(request, 'forgot.html', {'message': "User account not authenticate"})
        else:
            return render(request, 'forgot.html', {'message': "Invalid username or password"})

























