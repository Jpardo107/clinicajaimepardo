from django.shortcuts import render

from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from webapp.forms import PacienteForm
from webapp.models import Paciente


def index(request):
    pacientes = Paciente.objects.order_by('apellidos')
    if request.method == 'POST':
        formaPaciente = PacienteForm(request.POST)
        if formaPaciente.is_valid():
            if request.POST.get('rut') in Paciente.objects.values_list('rut', flat=True):
                messages.error(request, 'El rut ingresado ya existe, modifique desde el listado.')
                return redirect('index')
            else:
                formaPaciente.save()
                messages.success(request, 'Paciente ingresado correctamente.')
                return redirect('index')
    else:
        formaPaciente = PacienteForm()
    return render(request, 'index.html', {'formaPaciente': formaPaciente, 'pacientes': pacientes})


def editar(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    if request.method == 'POST':
        formaPaciente = PacienteForm(request.POST, instance=paciente)
        if formaPaciente.is_valid():
            formaPaciente.save()
            messages.success(request, 'Paciente ingresado correctamente.')
            return redirect('index')
    else:
        formaPaciente = PacienteForm(instance=paciente)
    return render(request, 'editar.html', {'formaPaciente': formaPaciente})


def eliminar(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    if paciente:
        paciente.delete()
    messages.success(request, 'Paciente eliminado correctamente.')
    return redirect('index')

