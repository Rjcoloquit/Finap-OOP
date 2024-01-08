from django import forms
from .models import CODMPlayer, CODMWeapon

class CODMPlayerForm(forms.ModelForm):
    class Meta:
        model = CODMPlayer
        fields = '__all__' 

class CODMWeaponForm(forms.ModelForm):
    class Meta:
        model = CODMWeapon
        fields = '__all__'  
