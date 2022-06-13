from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from datetime import date

from PIL import Image
from django.utils.html import mark_safe


YES_NO_CHOICES = [
    ('yes', 'Yes'),
    ('no', 'No')
]

AVAILABILITY_CHOICES = [
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
       
    ]

FUNCTIONAL_CHOICES = [
        ('Functional', 'Functional'),
        ('Non Functional', 'Non Functional'),
       
    ]


class District(models.Model):
    district = models.CharField(max_length=500, blank=False, null=False)

    @property
    def name(self):
        return str(self.district)

    def __str__(self):
        return self.district


        
class HealthWorker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='healthworker/thumbnail/%Y/%m/%d/', default = 'profile-img.jpg', null=True, blank=True)
    code = models.CharField(max_length = 50)
    name = models.CharField(max_length=50)
    cnic = models.CharField(max_length=50)
    father_or_husband_name = models.CharField(max_length=50)
    attached_facility= models.CharField(max_length=50)
    union_council = models.CharField(max_length=50)
    tehsil = models.CharField(max_length=50)
    catchment_of_population_of_flcf = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    population_registered_by_lhws = models.CharField(max_length=50)
    dateofbirth=models.DateTimeField(
          null=True
    )
    age=models.CharField(max_length=2, null=True)
    retirementyear=models.CharField(max_length=4, null=True)
    isRetired=models.BooleanField(null=True)
    phone=models.CharField(max_length=13, null=True)
    def __str__(self):
        return self.user.username

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.thumbnail.path) # Open image using self

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.thumbnail.path)

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.thumbnail.url))
        return ""

    class Meta:
        permissions = (("can_view_healthwoker", "Users Can view Health Worker Table"),)


class Report(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    district = models.ForeignKey(District, null=True, on_delete=models.SET_NULL)
    isheathcommittesformulated = models.CharField(max_length=50,choices=YES_NO_CHOICES, default='yes')
    iswomensupportgroupformulated = models.CharField(max_length=50, choices=YES_NO_CHOICES, default='yes')
    householdregisteredbyhw = models.IntegerField (default=0  )
    householdusingiodine = models.IntegerField (default=0  )
    tap=models.IntegerField (default=0  )
    canal=models.IntegerField (default=0  )
    otherdrinkingsource=models.IntegerField (default=0  )
    handpump=models.IntegerField (default=0  )
    well=models.IntegerField (default=0  )
    totalhouseholdwithdrinkingwatersource=models.IntegerField (default=0  )
    pit=models.IntegerField (default=0  )
    flush=models.IntegerField (default=0  )
    openfields=models.IntegerField (default=0  )
    total=models.IntegerField (default=0  )
    noofhealthcommitteemeeting=models.IntegerField (default=0  )
    noofhealtheducationsessionsheld=models.IntegerField (default=0  )
    noofnewbornsweighted=models.IntegerField (default=0  )
    nooflowbirthweighted=models.IntegerField (default=0  )
    noofnewbirthstartedbreastfeeding=models.IntegerField (default=0  )
    noofnewbornappliedchx=models.IntegerField (default=0  )
    noofnewbornimmunestarted=models.IntegerField (default=0  )
    sixmontholdchildren=models.IntegerField (default=0  )
    sixmontholdchildrenhavingbreastfeed=models.IntegerField (default=0  )
    sixtofiveninemonthchildren=models.IntegerField (default=0  )
    sixtofiveninechildrenhavingmaucdone=models.IntegerField (default=0  )
    malnutritionchildren=models.IntegerField (default=0  )
    sixtofiveninemalnutritionchildren=models.IntegerField (default=0  )
    twelvetotwentythreemonthchildren=models.IntegerField (default=0  )
    twelvetotwentythreechildrenfullyimmunized=models.IntegerField (default=0  )
    lessthanfiveyearchildrenprovidedsachet=models.IntegerField (default=0  )
    lessthanfiveyearchildren=models.IntegerField (default=0  )
    lessthanfiveyearchildrengmdone=models.IntegerField (default=0  )
    lessthanfiveyearchildrenlowweight=models.IntegerField (default=0  )

    ######################pregnancy data###############
    totalpregnantwomen=models.IntegerField (default=0  )
    totalpregnantwomenvisited=models.IntegerField (default=0  )
    noofpregnantandbreastfeddingwomen=models.IntegerField (default=0  )
    ironsuppliedpregnantwomen=models.IntegerField (default=0  )
    noofabortions=models.IntegerField (default=0  )
    totalofdeliveries=models.IntegerField (default=0  )
    womendeliveredtabprovided=models.IntegerField (default=0  )
    womendeliveredancvisits=models.IntegerField (default=0  )
    womendeliveredwithttcompleted=models.IntegerField (default=0  )
    deliveredbyskilledattendants=models.IntegerField (default=0  )
    postnatalcasevisited=models.IntegerField (default=0  )

    #############################family palnning
    eligiblecouples=models.IntegerField (default=0  )
    newfamilyplanningclients=models.IntegerField (default=0  )
    followupcasesforfamilyplanning=models.IntegerField (default=0  )
    traditionalmethodusers=models.IntegerField (default=0  )
    modernmethodusers=models.IntegerField (default=0  )
    condomusers=models.IntegerField (default=0  )
    oralpillusers=models.IntegerField (default=0  )
    cocusers=models.IntegerField (default=0  )
    ecpusers=models.IntegerField (default=0  )
    contraceptiveusers=models.IntegerField (default=0  )
    twomonthinjection=models.IntegerField (default=0  )
    threemonthinjection=models.IntegerField (default=0  )
    iucdclient=models.IntegerField (default=0  )
    surgicalclient=models.IntegerField (default=0  )
    othermoderncontraceptiveusers=models.IntegerField (default=0  )
    clientsreferred=models.IntegerField (default=0  )
    suppliedwithcondoms=models.IntegerField (default=0  )
    suppliedwithoral=models.IntegerField (default=0  )
    administeredwithinjectablecontraceptive=models.IntegerField (default=0  )

    # ailments

    diarrhoea=models.IntegerField (default=0  )
    ari=models.IntegerField (default=0  )
    fever=models.IntegerField (default=0  )
    injuries=models.IntegerField (default=0  )
    anameia=models.IntegerField (default=0  )
    scabies=models.IntegerField (default=0  )
    eyeinfection=models.IntegerField (default=0  )
    tractinfection=models.IntegerField (default=0  )
    worminfection=models.IntegerField (default=0  )
    malaria=models.IntegerField (default=0  )
    tbcases=models.IntegerField (default=0  )
    fistulacases=models.IntegerField (default=0  )
    hepatitas=models.IntegerField (default=0  )
    otherdiseases=models.IntegerField (default=0  )
    referalcasestohealthfacility=models.IntegerField (default=0  )
    followupcases=models.IntegerField (default=0  )

    ####misceallnous

    
    kitbagavailability=models.CharField(max_length=50, blank= True, choices=AVAILABILITY_CHOICES)
    kitbagfunctional=models.CharField(max_length=50, choices=FUNCTIONAL_CHOICES, blank= True)
    weighingmachineavailability=models.CharField(max_length=50, choices=AVAILABILITY_CHOICES, blank= True)
    weighingmachinefunction=models.CharField(max_length=50, choices=FUNCTIONAL_CHOICES, blank= True)
    thermometeravailable=models.CharField(max_length=50, blank= True, choices=AVAILABILITY_CHOICES)
    thermometerfunction=models.CharField(max_length=50, blank= True, choices=FUNCTIONAL_CHOICES)
    torchavailable=models.CharField(max_length=50, blank= True, choices=AVAILABILITY_CHOICES)
    torchfunction=models.CharField(max_length=50, blank= True, choices=FUNCTIONAL_CHOICES)
    scissorsavailable=models.CharField(max_length=50, blank= True, choices=AVAILABILITY_CHOICES)
    scissorsfunction=models.CharField(max_length=50, blank= True, choices=FUNCTIONAL_CHOICES)
    healthboardavailable=models.CharField(max_length=50, blank= True,choices=AVAILABILITY_CHOICES)
    healtboardfunction=models.CharField(max_length=50, blank= True, choices=FUNCTIONAL_CHOICES)
    bloodpressureavailable=models.CharField(max_length=50, blank= True, choices=AVAILABILITY_CHOICES)
    bloodpressurefunction=models.CharField(max_length=50, blank= True, choices=FUNCTIONAL_CHOICES)
    stethoscopeavailable=models.CharField(max_length=50, blank= True, choices=AVAILABILITY_CHOICES)
    stethoscopefunction=models.CharField(max_length=50, blank= True, choices=FUNCTIONAL_CHOICES)
    maucforchildrenavailable=models.CharField(max_length=50, blank= True, choices=AVAILABILITY_CHOICES)
    maucforchildrenfunction=models.CharField(max_length=50, blank= True, choices=FUNCTIONAL_CHOICES)
    maucformotheravailable=models.CharField(max_length=50, blank= True, choices=AVAILABILITY_CHOICES)
    maucformotherfunction=models.CharField(max_length=50, blank= True, choices=FUNCTIONAL_CHOICES)
    aritimeravailable=models.CharField(max_length=50, blank= True, choices=AVAILABILITY_CHOICES)
    aritimerfunction=models.CharField(max_length=50, blank= True, choices=FUNCTIONAL_CHOICES)
    otheravailable=models.CharField(max_length=50, blank= True, choices=AVAILABILITY_CHOICES)
    otherfunction=models.CharField(max_length=55, blank= True, choices=FUNCTIONAL_CHOICES)


    # birhs

    maternaldeaths=models.IntegerField (default=0  )
    deathsofchildren=models.IntegerField (default=0  )
    infantsdeaths=models.IntegerField (default=0  )
    deathmorethanoneweek=models.IntegerField (default=0  )
    newnataldeaths=models.IntegerField (default=0  )
    alldeaths=models.IntegerField (default=0  )
    stillbirths=models.IntegerField (default=0  )
    livebirths=models.IntegerField (default=0  )

    # supervision

    visitsbylhs=models.IntegerField (default=0  )
    visitsbydco=models.IntegerField (default=0  )
    visitsbyadc=models.IntegerField (default=0  )
    visitsbyfpo=models.IntegerField (default=0  )
    visitsbyppiu=models.IntegerField (default=0  )

    # otherthings
    comments=models.TextField(blank=True)
    datesubmitted=models.DateField(default=date.today)

    def __str__(self):
        return str(self.datesubmitted)








