from django import forms
from .models import Ariza, Kurslar, Konsultatsiya

class ArizaForm(forms.ModelForm):

    class Meta:
        model = Ariza
        fields = "__all__"


class KurslarForm(forms.ModelForm):

    class Meta:
        model = Kurslar
        fields = "__all__"

class KonsultatsiyaForm(forms.ModelForm):

    class Meta:
        models = Konsultatsiya
        fields ="__all__"

