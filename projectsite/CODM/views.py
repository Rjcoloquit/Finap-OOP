from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CODMPlayer, CODMWeapon
from django.views.generic import TemplateView
from .forms import CODMPlayerForm, CODMWeaponForm

# CODM Player Views
class HomePageView(TemplateView):
    template_name = 'home.html'

class CODMPlayerListView(ListView):
    model = CODMPlayer
    template_name = 'codm-player-list.html'
    context_object_name = 'players'
    paginate_by = 5

class CODMPlayerUpdateView(UpdateView):
    model = CODMPlayer
    form_class = CODMPlayerForm
    template_name = 'codm-player-edit.html' 
    success_url = reverse_lazy('codm-player-list')

class CODMPlayerDetailView(DetailView):
    model = CODMPlayer
    template_name = 'codm-player-detail.html'

class CODMPlayerCreateView(CreateView):
    model = CODMPlayer
    form_class = CODMPlayerForm
    template_name = 'codm-player-add.html'  
    success_url = reverse_lazy('codm-player-list')

class CODMPlayerDeleteView(DeleteView):
    model = CODMPlayer
    template_name = 'codm-player-delete.html'
    success_url = reverse_lazy('codm-player-list')

# CODM Weapon Views
class CODMWeaponListView(ListView):
    model = CODMWeapon
    template_name = 'codm-weapon-list.html'
    context_object_name = 'weapons'
    paginate_by = 5

class CODMWeaponDetailView(DetailView):
    model = CODMWeapon
    template_name = 'codm-weapon-detail.html'

class CODMWeaponCreateView(CreateView):
    model = CODMWeapon
    form_class = CODMWeaponForm
    template_name = 'codm-weapon-add.html'
    success_url = reverse_lazy('codm-weapon-list')

class CODMWeaponUpdateView(UpdateView):
    model = CODMWeapon
    form_class = CODMWeaponForm
    template_name = 'codm-weapon-edit.html'
    success_url = reverse_lazy('codm-weapon-list')

class CODMWeaponDeleteView(DeleteView):
    model = CODMWeapon
    template_name = 'codm-weapon-confirm-delete.html'
    success_url = reverse_lazy('codm-weapon-list')


class AboutUsView(TemplateView):
    template_name = 'about-us.html'