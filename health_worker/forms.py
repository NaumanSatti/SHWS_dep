from django.forms import ModelForm
from .models import HealthWorker, Report


class HealthWorkerForm(ModelForm):
    # specify the name of model to use
    class Meta:
        model = HealthWorker
        fields = "__all__"

class ReportForm(ModelForm):
    class Meta:
        model = Report
        exclude = ['user', 'district']
class ReportEditForm(ModelForm):
    class Meta:
        model = Report
        exclude = ['user','district']

    def __init__(self, *args, **kwargs):
        super(ReportEditForm, self).__init__(*args, **kwargs)
        self.fields['totalhouseholdwithdrinkingwatersource'].widget.attrs['readonly'] = True
        
        self.fields['total'].widget.attrs['readonly'] = True
        self.fields['tap'].widget.attrs['aria-labelledby'] =  'sourceofdrinkingwater'
        self.fields['canal'].widget.attrs['aria-labelledby'] =  'sourceofdrinkingwater'
        self.fields['otherdrinkingsource'].widget.attrs['aria-labelledby'] =  'sourceofdrinkingwater'
        self.fields['handpump'].widget.attrs['aria-labelledby'] =  'sourceofdrinkingwater'
        self.fields['well'].widget.attrs['aria-labelledby'] =  'sourceofdrinkingwater'

        # for sewerage system

        self.fields['pit'].widget.attrs['aria-labelledby'] =  'seweragetype'
        self.fields['flush'].widget.attrs['aria-labelledby'] =  'seweragetype'
        self.fields['openfields'].widget.attrs['aria-labelledby'] =  'seweragetype'

class ReportViewForm(ModelForm):
    class Meta:
        model = Report
        exclude = ['user',]

    def __init__(self, *args, **kwargs):
        super(ReportViewForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            for field in self.fields:
                self.fields[field].widget.attrs['readonly'] = "readonly"
        


class HealthWorkerCreateForm(ModelForm):
    class Meta:
        model = HealthWorker
        exclude = ['user','age','retirementyear',]

class HealthWorkerEditForm(ModelForm):
    class Meta:
        model = HealthWorker
        exclude = ['user','age','retirementyear',]

    def __init__(self, *args, **kwargs):
        super(HealthWorkerEditForm, self).__init__(*args, **kwargs)
        self.fields['thumbnail'].required = False