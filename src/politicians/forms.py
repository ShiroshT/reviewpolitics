from django import forms

from .models import Politician

class PoliticianModelForm(forms.ModelForm):
    # shortname = models.CharField(max_length=60, unique=False)
    # fullname_polit = models.CharField(max_length=60, unique=False)
    # dateofbirth_polit = models.DateField()
    # summary_header = models.TextField(max_length=500)
    # detailed_descrpt = models.TextField(max_length=500)
    # timestamp = models.DateTimeField(auto_now_add = True)

    YEARS= [x for x in range(1920,2018)]

    shortname = forms.CharField(label='', 
                widget=forms.TextInput(
                        attrs={'placeholder': "Candidate ID", 
                            "class": "form-control"}
                    ))
    
    fullname_polit = forms.CharField(label='', 
                widget=forms.TextInput(
                        attrs={'placeholder': "Candidate Name", 
                            "class": "form-control"}
                    ))

    dateofbirth_polit  = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS))

    summary_header = forms.CharField(label='', 
                widget=forms.Textarea(
                        attrs={'placeholder': "Summary", 
                            "class": "form-control"}
                    ))

    detailed_descrpt = forms.CharField(label='', 
                widget=forms.Textarea(
                        attrs={'placeholder': "Descriptions", 
                            "class": "form-control"}
                    ))
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Politician
        fields = (
            'shortname',  
            'fullname_polit', 
            'dateofbirth_polit', 
            'summary_header',
            'detailed_descrpt')

