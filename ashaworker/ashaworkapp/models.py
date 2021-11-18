from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class PatientEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password2 = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    adharno = models.CharField(max_length=100)
    wardno =  models.CharField(max_length=100)
    panchayath = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    dob = models.CharField(max_length=100)
    fahusname = models.CharField(max_length=200)
    fahusno = models.CharField(max_length=200)
    noofchild = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True)
    address = models.CharField(max_length=1000, default='0')
    wedding = models.DateField(default='2021-10-11')
    qualification = models.CharField(max_length=100, default='0')
    age = models.CharField(max_length=100, default='0', null=True)
    job = models.CharField(max_length=100, default='0')
    medicines = models.CharField(max_length=1000, default='0')
    checkstart = models.DateField(default='2021-10-11')
    confirmdate = models.DateField(default='2021-10-11')
    issue = models.CharField(max_length=1000, default='0')


class DoctorEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password2 = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    adharno = models.CharField(max_length=100)
    idcard = models.ImageField(upload_to='images/', null=True)
    image = models.ImageField(upload_to='images/', null=True)
    qualification = models.ImageField(upload_to='images/', null=True)

class AshaworkerEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password2 = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    ward = models.CharField(max_length=100, default='0')
    husname = models.CharField(max_length=100, default='0')
    street = models.CharField(max_length=500, default='0')
    city = models.CharField(max_length=300, default='0')
    panchayath = models.CharField(max_length=300, default='0')
    adharcard = models.ImageField(upload_to='images/', null=True)
    idcard = models.ImageField(upload_to='images/', null=True)
    profilepic = models.ImageField(upload_to='images/', null=True)

class Feedback_Asha(models.Model):
    ashaworker = models.ForeignKey(AshaworkerEntry, on_delete=models.CASCADE)
    user = models.ForeignKey(UserType, on_delete=models.CASCADE)
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)
    reply = models.CharField(max_length=1000)
    status = models.CharField(max_length=500)
    feedback = models.CharField(max_length=1000)

class Feedback_User(models.Model):
    patients = models.ForeignKey(PatientEntry, on_delete=models.CASCADE)
    user = models.ForeignKey(UserType, on_delete=models.CASCADE)
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)
    reply = models.CharField(max_length=1000)
    status = models.CharField(max_length=500)
    feedback = models.CharField(max_length=1000)

class AskDoctor(models.Model):
    patients = models.ForeignKey(PatientEntry, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorEntry, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(UserType, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    assign = models.CharField(max_length=200)
    answer = models.CharField(max_length=1000)

class Child_Module(models.Model):
    patients = models.ForeignKey(PatientEntry, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField(default='2021-10-11')
    hospitalname = models.CharField(max_length=400)
    place = models.CharField(max_length=500)
    gender = models.CharField(max_length=200)
    firstvaccinedate = models.DateField(default='2021-10-11')
    birthcertificate = models.ImageField(upload_to='images/', null=True)

class Preg_Women(models.Model):
    patients = models.ForeignKey(PatientEntry, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    startdate = models.DateField(default='2021-10-11')
    firstcheckup = models.DateField(default='2021-10-11')
    hospitalname = models.CharField(max_length=500)

class Newly_Married(models.Model):
    patients = models.ForeignKey(PatientEntry, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    oldpanchayath = models.CharField(max_length=300)
    oldstreet = models.CharField(max_length=300)
    oldwardno = models.CharField(max_length=200)
    medicines = models.CharField(max_length=500)

class Tips(models.Model):
    doctor = models.ForeignKey(DoctorEntry, on_delete=models.CASCADE)
    tips = models.CharField(max_length=1000)
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)
