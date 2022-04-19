from django.forms import ModelForm, EmailInput

from webapp.models import Paciente


class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets ={
            'email': EmailInput(attrs={'type': 'email'})
        }