import re
from traceback import print_tb
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from health_worker.models import HealthWorker, District, Report
from django.http import JsonResponse

from django.db.models import Count, Sum
from django.db.models import Q
import json
import random

from django.contrib.auth.decorators import user_passes_test

def user_check(user):
    return user.is_staff
def otp(request):
    number = random.randint(1000,9999)
    print(number)

    OTP=request.POST.get("OTP")
def tabular(request):
    
    current_user=request.user
    user_id=current_user.id
    district_list=[]
    all_dist = District.objects.all()
   
    i = 1
    dist = {}
    for district in all_dist:
        dist[i] = district
        i += 1
        district_list.append(district.name)

    context={
    'districts_list':district_list,

    }
    return render(request, 'pages/tabular.html', context=context)

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.user.is_staff:
        return redirect('/dashboard')
    else:
        return redirect('profile')

def user_login(request):
    
    context = {}
    if request.method == 'POST':
        
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            if "@" in username:
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(username=username)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                context["error"] = "Wrong password"
        except ObjectDoesNotExist:
            context["error"] = "User not found"

    return render(request, 'pages-login.html', context=context)







@login_required(login_url='/login')
@user_passes_test(user_check, login_url='/login')
def dashboard(request):

    current_user=request.user
    user_id=current_user.id

    all_dist = District.objects.all()
   
    i = 1
    dist = {}

    # for first table
    total_district_reports = District.objects.annotate(reportCount = Count('report'))
    # for district list in graph
    district_list = []
    imr=[]
    infants_deaths=[]
    deaths_more_than_one_week=[]
    new_natal_death=[]
    maternal_deaths=[]
    mmr=[]
    totaldeathslist=[]
    total_of_deliveries=[]
    # for second graph
    no_of_live_births = []
    women_delivered_anc_visits=[]
    perc_no_of_newborn_immune_started=[]
    no_of_new_born_started_breastfeeding = []
    no_of_childrenhaving_maucdone =[]
    no_of_sixto_fivenine_childern =[]
    no_of_lessthanfive_chidlren_sachet_provided = []
    no_of_less_than_fiveyear_children = []
    no_of_new_born_whose_immune_started =[]
    perc_Bf=[]
    perc_ANC=[]
    # for third graph
    for district in all_dist:
        dist[i] = district
        i += 1
        district_list.append(district.name)

        # for second graph
       
        queryset = Report.objects.filter(district = district)
        print(queryset) 
        report = queryset.aggregate(Sum('livebirths'), Sum('noofnewbirthstartedbreastfeeding'),\
             Sum('sixtofiveninechildrenhavingmaucdone'), Sum('sixtofiveninemonthchildren'),\
             Sum('lessthanfiveyearchildrenprovidedsachet'), Sum('lessthanfiveyearchildren'),\
             Sum('womendeliveredancvisits'),Sum('totalofdeliveries'),Sum('noofnewbornimmunestarted'), Sum('deathmorethanoneweek'), Sum('newnataldeaths'),Sum('infantsdeaths'), Sum('maternaldeaths'), Sum('alldeaths'))
        try:
            women_delivered_anc_visits.append(float(report['womendeliveredancvisits__sum']))
            total_of_deliveries.append(float(report['totalofdeliveries__sum']))
            totaldeathslist.append(float(report['alldeaths__sum']))
            maternal_deaths.append(float(report['maternaldeaths__sum']))
            infants_deaths.append(float(report['infantsdeaths__sum']))
            new_natal_death.append(float(report['newnataldeaths__sum']))
            deaths_more_than_one_week.append(float(report['deathmorethanoneweek__sum']))
            no_of_live_births.append(float(report['livebirths__sum']))
            no_of_new_born_started_breastfeeding.append(float(report['noofnewbirthstartedbreastfeeding__sum']))
            no_of_childrenhaving_maucdone.append(float(report['sixtofiveninechildrenhavingmaucdone__sum']))
            no_of_sixto_fivenine_childern.append(float(report['sixtofiveninemonthchildren__sum']))
            no_of_lessthanfive_chidlren_sachet_provided.append(float(report['lessthanfiveyearchildrenprovidedsachet__sum']))
            no_of_less_than_fiveyear_children.append(float(report['lessthanfiveyearchildren__sum']))
            no_of_new_born_whose_immune_started.append(float(report['noofnewbornimmunestarted__sum']))
        except TypeError:
            women_delivered_anc_visits.append(0)
            total_of_deliveries.append(0)
            totaldeathslist.append(0)
            maternal_deaths.append(0)
            infants_deaths.append(0)
            new_natal_death.append(0)
            deaths_more_than_one_week.append(0)
            no_of_live_births.append(0)
            no_of_new_born_started_breastfeeding.append(0)
            no_of_childrenhaving_maucdone.append(0)
            no_of_sixto_fivenine_childern.append(0)
            no_of_lessthanfive_chidlren_sachet_provided.append(0)
            no_of_less_than_fiveyear_children.append(0)
            no_of_new_born_whose_immune_started.append(0)
  
    for x in range(len(district_list)):
          # declaration of the list  
        mmr.append(int(maternal_deaths[x]/(no_of_live_births[x]+0.0000000000000001)*100000))

    
    for x in range(len(district_list)):
          # declaration of the list  
        perc_ANC.append(round( women_delivered_anc_visits[x]/(total_of_deliveries[x]+0.00000000001)*100,2))
    for x in range(len(district_list)):
          # declaration of the list  
        imr.append( int(((new_natal_death[x] + deaths_more_than_one_week[x] + infants_deaths[x])/(no_of_live_births[x]+0.000001))*1000))
    
    for x in range(len(district_list)):
        perc_Bf.append(round(no_of_new_born_started_breastfeeding[x]/(no_of_live_births[x]+0.0000000000001)*100,2))
    
    total_live_births= sum(no_of_live_births)
    total_live_births= int(total_live_births)
    sum_alldeaths= sum(totaldeathslist)
    sum_alldeaths= int(sum_alldeaths)
    
    perc_death=sum_alldeaths/(total_live_births+0.00001)*100
    sum_infantsdeaths= sum(infants_deaths)
    sum_infantsdeaths= int(sum_infantsdeaths)

    sum_matdeaths= sum(maternal_deaths)
    sum_matdeaths= int(sum_matdeaths)
    bfData=zip(no_of_new_born_started_breastfeeding,no_of_live_births,perc_Bf, district_list)
    
    if(total_live_births==0):
        mort_rate= sum_alldeaths/(total_live_births+0.0001)*100
      
        matmortrate=sum_matdeaths/(total_live_births+0.0000001)*100000
        matmortrate=int(matmortrate)
    else:
        mort_rate= round(sum_alldeaths/total_live_births*100,2)
        matmortrate=sum_matdeaths/total_live_births*100000
        matmortrate=int(matmortrate)
    
    for x in range(len(no_of_live_births)):
        perc_no_of_newborn_immune_started.append(round(no_of_new_born_whose_immune_started[x]/(no_of_live_births[x]+0.00001)*100,2))
    chartlist=zip(maternal_deaths,no_of_live_births,infants_deaths, district_list)
    ziplist=zip(maternal_deaths,no_of_live_births,infants_deaths, district_list,totaldeathslist, imr, mmr, new_natal_death, deaths_more_than_one_week)
    context = {
        'perc_ANC':perc_ANC,
        'women_delivered_anc_visits':women_delivered_anc_visits,
        'total_of_deliveries':total_of_deliveries,
        'bfData':bfData,
        'matmortrate':matmortrate,
        'sum_matdeaths':sum_matdeaths,
        'sum_infantsdeaths':sum_infantsdeaths,
        'perc_no_of_newborn_immune_started':perc_no_of_newborn_immune_started,
        'chartlist':chartlist,
        'ziplist':ziplist,
        'mort_rate':mort_rate,
        'sum_alldeaths':sum_alldeaths,
        'total_live_births':total_live_births,
        'user_id':user_id,
        'maternal_deaths':maternal_deaths,
        'mmr':mmr,
        'infants_deaths':infants_deaths,
        'imr':imr,
        'new_natal_death':new_natal_death,
        'deaths_more_than_one_week':deaths_more_than_one_week,
        'filename':'index',
        'districts':dist,
        'districts_list':district_list,
        'total_district_reports':total_district_reports,
        # for second graph
        'no_of_live_births':no_of_live_births,
        'no_of_new_born_started_breastfeeding':no_of_new_born_started_breastfeeding,
        'no_of_childrenhaving_maucdone':no_of_childrenhaving_maucdone,
        'no_of_sixto_fivenine_children':no_of_sixto_fivenine_childern,
        'no_of_less_thanfive_children_sachet_provided':no_of_lessthanfive_chidlren_sachet_provided,
        'no_of_less_than_fiveyear_children':no_of_less_than_fiveyear_children,
        'no_of_new_born_whose_immune_started':no_of_new_born_whose_immune_started,


    }
    return render(request, 'pages/dashboard.html', context=context)


def check_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)








def html(request, filename):
    context = {"filename": filename,
               "collapse": ""}
    if request.user.is_anonymous and filename != "login":
        return redirect("/login.html")
    if filename == "logout":
        logout(request)
        return redirect("/")
    if filename == "login" and request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            if "@" in username:
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(username=username)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                context["error"] = "Wrong password"
        except ObjectDoesNotExist:
            context["error"] = "User not found"

        print("login")
        print(username, password)
    print(filename, request.method)
    if filename in ["buttons", "cards"]:
        context["collapse"] = "components"
    if filename in ["utilities-color", "utilities-border", "utilities-animation", "utilities-other"]:
        context["collapse"] = "utilities"
    if filename in ["404", "blank"]:
        context["collapse"] = "pages"

    return render(request, f"{filename}.html", context=context)
