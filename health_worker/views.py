from django.db import connection
from csv import Dialect
import imp
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import HealthWorkerForm, ReportForm, ReportEditForm, HealthWorkerCreateForm, \
     HealthWorkerEditForm, ReportViewForm
from datetime import datetime
from django.contrib.auth.models import User, Group
from .models import HealthWorker, Report, District
from django.db.models import ObjectDoesNotExist
from django.db.models import Q
from django.contrib import messages
from django.db.models import Count, Sum
import functools
from django.contrib.auth.decorators import user_passes_test
from twilio.rest import Client


body=       f'''
              This is a formal notice of your retirement. You are going to retire next year from SHWS.
              We would like to thank you for such an amazing service and dedication and hardword you put into your work.
              Without you, it would have been impossible to create such an impact. We enjoyed working with you.
              Thank you so much for your service. Wish you a very blessed after-retirement life. God bless you.

              Sincerely:

              SHWS System.

              Note: This is a system generated SMS. No need to reply. :) 
            '''
   

body1= f'''  
              This is a formal notice of your retirement. You have been officially declared retired from SHWS system.
              From now onwards, you won't be able to login into your SHWS account. You will be deleted from the system
              after this message.
              We would like to thank you for such an amazing service and dedication and hardword you put into your work.
              Without you, it would have been impossible to create such an impact. We enjoyed working with you.
              Thank you so much for your service. Wish you a very blessed after-retirement life. God bless you.

              Sincerely:

              SHWS System.

              Note: This is a system generated SMS. No need to reply. :) 
    
    '''

def sendSMS(name, district, year, phone,Body):
    TWILIO_ACCOUNT_SID='AC9f092dc426dce5f2e55affe05669e411'
    TWILIO_AUTH_TOKEN='5eaa4a61a1b8577e32ea8b666ea864eb'
    body=f''' {name} 
              From: {district}

              Dear {name}!
         '''+ Body   
    
    client=Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
    client.messages.create(
        from_='+18647785492',
        body=body,
        to=phone
    )
def month_getter():
    x=datetime.today().strftime('%m')
    if x=='01':
        return 'January'
    if x=='02':
        return 'February'
    if x=='03':
        return 'March'
    if x=='04':
        return 'April'
    if x=='05':
        return 'May'
    if x=='06':
        return 'June'
    if x=='07':
        return 'July'
    if x=='08':
        return 'August'
    if x=='09':
        return 'September'
    if x=='10':
        return 'October'
    if x=='11':
        return 'November'
    if x=='12':
        return 'December'


def tup_to_int(t):
    test_tuple=t
    res = functools.reduce(lambda sub, ele: sub * 10 + ele, test_tuple)
    return res
def user_check(user):
    return user.is_staff

# Create your views here.


@login_required(login_url='/login')
def profile(request):
    try:
        healthworker = HealthWorker.objects.get(user=request.user)
        x=healthworker.name
        print(x)        
    except HealthWorker.DoesNotExist:
        healthworker = None
    context ={
        'filename':'profile',
        'healthworker': healthworker
    }
 
    return render(request, 'pages/profile.html', context = context)
from datetime import date
import datetime
def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str
@login_required(login_url='/login')
def details(request):
    HW=HealthWorker.objects.all()
    Age=HealthWorker.objects.values_list('age', flat=True).all()

    print(Age)
    DOB=HealthWorker.objects.values_list('dateofbirth', flat=True).all()
    total=len(HW)
    
    Age=list(Age)
    
    
    import datetime

   
    
    context = {
        'filename':'healthworker',
        'healthworkers': HW,
        'total':total,
        'Age':Age,
        

        
    }
    return render(request, 'pages/details.html', context)
 
    

@login_required(login_url='/login')
def data_entry(request):
    
    x=month_getter()
    healthworker = HealthWorker.objects.get(user=request.user)
    isStaff=request.user.is_staff
    current_user=request.user
    user_id=current_user.id
    name=healthworker.name
    query="""SELECT COUNT(datesubmitted) FROM health_worker_report WHERE strftime('%%m', date(datesubmitted))= %s and user_id= %s"""
    tuple1 = (x, user_id)
    c=connection.cursor()

    c.execute(query,tuple1)
    ps=c.fetchone()
    ps=tup_to_int(ps)
    if isStaff==1:
        rep=0
    else:
        if ps >=1:
            rep= 1
        else:
            rep= 0
   
    context = {'rep':rep,
    'x':x,
    'name':name}

    if request.method == "POST":       
        form = ReportForm(request.POST)
       
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.district = request.user.healthworker.district
            
            
            context['success'] = 'Report successfully added'
            report.save()

            return render(request, 'pages/profile.html',context = context)
        else:
            print(form.errors.as_data())
        
        
    try:
        healthworker = HealthWorker.objects.get(user=request.user)
    except HealthWorker.DoesNotExist:
        # healthworker = None
        return render(request, 'pages/not-healthworker.html')

    context['filename'] = 'profile'
    context['healthworker'] = healthworker
    
    
 
    return render(request, 'pages/data-entry.html', context = context)

def dash2(request):
    abc="Nauman"
    context={
        'abc':abc
    }
    return render(request, 'pages/dash2.html', context=context)

@login_required(login_url='/login')
def my_reports(request):
    
    x=month_getter()
  

    healthworker = HealthWorker.objects.get(user=request.user)
    isStaff=request.user.is_staff
    current_user=request.user
    user_id=current_user.id
    
    query="""SELECT COUNT(datesubmitted) FROM health_worker_report WHERE strftime('%%m', date(datesubmitted))= %s and user_id= %s"""
    
    tuple1 = (x, user_id)
    c=connection.cursor()

    c.execute(query,tuple1)
    ps=c.fetchone()
    ps=tup_to_int(ps)
    print(ps)
    if isStaff==0:

        query1="""SELECT id FROM health_worker_report WHERE strftime('%%m', date(datesubmitted))= %s and user_id= %s"""
        tuple2 = (x, user_id)
        cs=connection.cursor()

        cs.execute(query1,tuple2)
        iid=cs.fetchall()
        
        iid=list(iid)
        if (len(iid)>0):
            iid.remove(min(iid))
            
            for x in range(len(iid)):
                query2="""DELETE FROM health_worker_report WHERE id= %s"""
                tuple3 = (iid[x])
                cs1=connection.cursor()

                cs1.execute(query2,tuple3)

    
    if isStaff==1:
        rep=0
    else:
        if ps >=1:
            rep= 1
        else:
            rep= 0
   
    print(rep) 
    if request.user.is_superuser:
        reports = Report.objects.all()
    else:

        reports = Report.objects.filter(user = request.user)
    
    total= len(reports)
    context = {
        'total':total,
        'rep':rep,
        'isStaff':isStaff,
        'user_id':user_id,
        'reports':reports,
        'healthworker':healthworker,
        'filename':'myreports'
    }



    return render(request, 'pages/my-reports.html', context)

@login_required(login_url='/login')
def delete_report(request, id):
    report = Report.objects.get(pk = id)
    report.delete()

    return redirect('/my_reports')

@login_required(login_url='/login')
def edit_report(request, id):
    report = Report.objects.get(pk = id)
    if request.method  == 'POST':
        form = ReportEditForm(request.POST, instance = report)
        if form.is_valid():
            form.save()
            messages.success(request, 'Report Edited successfully!')
            return redirect('my-reports')
        else:
            print(form.errors.as_data())
    
    form = ReportEditForm(instance = report)
    context = {
        'form': form
    }     
    return render(request,'pages/edit-reports.html', context)


@login_required(login_url='/login')
def view_report(request, id):
    report = Report.objects.get(pk = id)
    form = ReportViewForm(instance = report)
    context = {
        'form': form
    }
    return render(request,'pages/view-reports.html', context)




# ################# health worker section ########################

@login_required(login_url='/login')
def view_hw(request, id):
    healthworker = HealthWorker.objects.get(pk = id)
   
    context = {
        'HW': healthworker
    }
    return render(request,'pages/view-healthworker.html', context)





@login_required(login_url='/login')
@user_passes_test(user_check, login_url='/login')
def sendsms(request,id):
   

    health_worker = HealthWorker.objects.get(pk = id)
    now=datetime.today()
    Name=health_worker.name
    Phone=health_worker.phone
    District=health_worker.district
    age=int(health_worker.age)
    if(age==59):

        # sendSMS(Name, District, 1, Phone,body)
        messages.success(request, 'Message was successfully sent to ' + Name, extra_tags='alert') 
        return redirect('details')
    
    elif(age>=60):
        # sendSMS(Name, District, 1, Phone,body1)
        health_worker.delete()
        messages.success(request, 'Message was successfully sent to ' + Name +'. He is officially being retired and deleted from system', extra_tags='alert') 
        return redirect('details')
    


@login_required(login_url='/login')
@user_passes_test(user_check, login_url='/login')
def healthworkers(request):
    context = {
        'filename':'healthworker',
        'healthworkers': HealthWorker.objects.all()
    }
    return render(request, 'pages/users/health-workers.html', context)

from datetime import datetime
@login_required(login_url='/login')
@user_passes_test(user_check, login_url='/login')
def create_health_worker(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        dob=request.POST.get('dateofbirth')
        mm=' 18:54:55.099000'
        DOB=dob+mm
        date_time_obj=datetime.strptime(DOB, '%Y-%m-%d %H:%M:%S.%f')
        AGE=age(date_time_obj)
        
        today=datetime.today()
        x=AGE
        y=60-x
        z=today.year
        w=z+y
        if(AGE>=60):
            retired=True
        else:
            retired=False
        user = User.objects.create_user(username = username, password = password)
        # user.save()
    
        
        
        form = HealthWorkerCreateForm(request.POST,request.FILES)
        if form.is_valid():
            hwform = form.save(commit=False)
            hwform.user = user
            hwform.age = AGE
            hwform.retirementyear=w
            hwform.isRetired=retired
           
            hwform.save()
            user.save()
            messages.success(request,'Health Worker successfully added!')
            return redirect('health-workers')
        else:
            print(form.errors.as_data())
        

    else:
        context={
            'filename':'healthworker',
            'users': User.objects.all(),
            'districts':District.objects.all()
        }

        return render(request, 'pages/users/create-health-worker.html', context)


@login_required(login_url='/login')
@user_passes_test(user_check, login_url='/login')
def edit_health_worker(request, pk):
    query=""" SELECT dateofbirth FROM health_worker_healthworker WHERE id= %s """
    tuple1 = [pk,]
    c=connection.cursor()

    c.execute(query,tuple1)
    ps=c.fetchone()
    A=ps[0]
    date_time = A.strftime("%Y-%m-%d")

    mm=' 18:54:55.099000'
    DOB=date_time+mm
    
    date_time_obj=datetime.strptime(DOB, '%Y-%m-%d %H:%M:%S.%f')
    AGE=age(date_time_obj)
    if request.method == 'POST':
        form = HealthWorkerEditForm(request.POST, request.FILES, instance=HealthWorker.objects.get(pk = pk))
        if form.is_valid():
            Date=request.POST.get('dateofbirth')
            mm=' 18:54:55.099000'
            DOB=Date+mm
            date_time_obj=datetime.strptime(DOB, '%Y-%m-%d %H:%M:%S.%f')
            AGE=age(date_time_obj)
            today=datetime.today()
            x=AGE
            y=60-x
            z=today.year
            w=z+y
            if(x>=60):
                retired=True
            else:
                retired=False

            hwform = form.save(commit=False)
            hwform.age=AGE
            hwform.isRetired=retired
            hwform.retirementyear=w
            
            hwform.save()
            messages.success(request, 'Health worker edited successfully!')
            return redirect('health-workers')
        else:
            print(form.errors.as_data())
    else:
        context ={
            'hw': HealthWorker.objects.get(pk = pk),
            'A':date_time
        }
        return render(request, 'pages/users/edit-health-worker.html', context)



@login_required(login_url='/login')
@user_passes_test(user_check, login_url='/login')
def delete_healthworker(request, pk):
    health_worker = HealthWorker.objects.get(pk = pk)
    user = health_worker.user
    user.delete()
    health_worker.delete()
    messages.success(request, 'User was successfully deleted!', extra_tags='alert') 
    return redirect('health-workers')

@login_required(login_url='/login')
@user_passes_test(user_check, login_url='/login')
def visualization(request,dist_name):
    dis = District.objects.get(district = dist_name)

    
    
    all_dist = District.objects.all()
    i = 1
    dist = {}
    series = []
    radarseries = []
    series1=[]
    live_births=[]
    all_deaths=[]
    LIVEBIRTHS=[]
    infants_deaths=[]
    maternal_deaths=[]
    percentage=[]
    death_more_than_one_week=[]
    new_natal_death=[]
    IMR=[]
    radar=[]
    MMR=[]
    poly=[]
    death=[]
    LIVEBIRTHS=[]
    no_of_newborn_immune_started=[]
    perc_no_of_newborn_immune_started=[]
    pc2=[]
    no_of_new_birth_started_breast_feeding=[]
    nnw=[]
    nnw1=[]
    for district in all_dist:
        dist[i] = district
        i += 1

    # for graph
    try:
        district = District.objects.get(district = dist_name)

        queryset = Report.objects.filter(district = district)
        report = queryset.aggregate(Sum('totalpregnantwomenvisited'), Sum('totalpregnantwomen'), \
        Sum('deliveredbyskilledattendants'), Sum('totalofdeliveries'), Sum('womendeliveredancvisits'))
        infantsdeaths=queryset.aggregate(Sum('infantsdeaths'))
        maternaldeaths = queryset.aggregate(Sum('maternaldeaths'))
        report2 = queryset.aggregate(Sum('alldeaths'), Sum('infantsdeaths'), Sum('maternaldeaths'))
        report3=queryset.aggregate(Sum('livebirths'), Sum('alldeaths'))
        livebirths=queryset.aggregate(Sum('livebirths'))
        alldeaths=queryset.aggregate(Sum('alldeaths'))
        dmtow=queryset.aggregate(Sum('deathmorethanoneweek'))
        NND=queryset.aggregate(Sum('newnataldeaths'))
        noofnewbornimmunestarted=queryset.aggregate(Sum('noofnewbornimmunestarted'))
        noofnewbirthstartedbreastfeeding=queryset.aggregate(Sum('noofnewbirthstartedbreastfeeding'))

        for key, values in noofnewbirthstartedbreastfeeding.items():
            try:
                no_of_new_birth_started_breast_feeding.append(float(values))
            except TypeError:
                no_of_new_birth_started_breast_feeding.append(0)
        
        for key, values in noofnewbornimmunestarted.items():
            try:
                no_of_newborn_immune_started.append(float(values))
            except TypeError:
                no_of_newborn_immune_started.append(0)
        

        for key, values in NND.items():
            try:
                new_natal_death.append(float(values))
            except TypeError:
                new_natal_death.append(0)
        
        
        for key, values in dmtow.items():
            try:
                death_more_than_one_week.append(float(values))
            except TypeError:
                death_more_than_one_week.append(0)

        
        for key, values in infantsdeaths.items():
            try:
                infants_deaths.append(float(values))
            except TypeError:
                infants_deaths.append(0)

        for key, values in maternaldeaths.items():
            try:
                maternal_deaths.append(float(values))
            except TypeError:
                maternal_deaths.append(0)

        for key, values in alldeaths.items():
            try:
                all_deaths.append(float(values))
            except TypeError:
                all_deaths.append(0)


        for key, values in livebirths.items():
            try:
                live_births.append(float(values))
            except TypeError:
                live_births.append(0)


        for key, values in report3.items():
            try:
                series1.append(float(values))
            except TypeError:
                series1.append(0)

        for key, values in report.items():
            try:
                series.append(float(values))
            except TypeError:
                series.append(0)


        for key, values in report2.items():
            try:
                radarseries.append(float(values))
            except TypeError:
                radarseries.append(0)


    except ObjectDoesNotExist:
        pass
    
    for x in range(len(no_of_new_birth_started_breast_feeding)):
          # declaration of the list  
        nnw.append(round(no_of_new_birth_started_breast_feeding[x]/(live_births[x]+0.01)*100,2))


    for x in range(len(no_of_newborn_immune_started)):
          # declaration of the list  
        perc_no_of_newborn_immune_started.append(round(no_of_newborn_immune_started[x]/(live_births[x]+0.01)*100,2))

    
    for x in range(len(radarseries)):
          # declaration of the list  
        percentage.append(round(radarseries[x]/(live_births[0]+1)*100,2))

    for x in range(len(new_natal_death)):
          # declaration of the list  
        IMR.append(round((new_natal_death[x]+death_more_than_one_week[x]+infants_deaths[x])/(live_births[x]+1)*100,2))    
    
    for x in range(len(new_natal_death)):
        MMR.append(round(maternal_deaths[x]/(live_births[x]+1)*10000,2))    
    
    
    radar=infants_deaths+death_more_than_one_week+new_natal_death+live_births+all_deaths+IMR
    poly=maternal_deaths+live_births+MMR
    death=IMR+MMR
    pc2=no_of_newborn_immune_started+live_births
    nnw1=no_of_new_birth_started_breast_feeding+live_births

    maternal=int(maternal_deaths[0])
    tdeaths=int(all_deaths[0])
    infDeaths=int(infants_deaths[0])
    live=int(live_births[0])
   
    context = {
        'infDeaths':infDeaths,
        'tdeaths':tdeaths,
        'Livebirths':LIVEBIRTHS,
        'live':live,
        'dis':dis,
        'maternal': maternal,
        'perc_no_of_newborn_immune_started':perc_no_of_newborn_immune_started,
        'pc2':pc2,
        'nnw':nnw,
        'nnw1':nnw1,
        'death':death,
        'poly':poly,
        'radar':radar,
        'death_more_than_one_week':death_more_than_one_week,
        'percentage':percentage,
        'maternal_deaths':maternal_deaths,
        'infants_deaths':infants_deaths,
        'all_deaths':all_deaths,
        'live_births':live_births,
        'filename':'index',
        'districts':dist,
        'series1':series1,
        'series':series,
        'radarseries':radarseries
        
    }
    return render(request, 'pages/visualization.html', context=context)




