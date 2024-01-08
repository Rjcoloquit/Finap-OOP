from django.urls import path
from .views import (
    HomePageView, CODMPlayerListView, CODMPlayerCreateView, CODMPlayerUpdateView, CODMPlayerDeleteView,
    CODMWeaponListView, CODMWeaponCreateView, CODMWeaponUpdateView, CODMWeaponDeleteView, AboutUsView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),

    path('codm_players/', CODMPlayerListView.as_view(), name='codm-player-list'),
    path('codm_players/add/', CODMPlayerCreateView.as_view(), name='codm-player-add'),
    path('codm_players/<int:pk>/edit/', CODMPlayerUpdateView.as_view(), name='codm-player-edit'),
    path('codm_players/<int:pk>/delete/', CODMPlayerDeleteView.as_view(), name='codm-player-delete'),

    path('codm_weapons/', CODMWeaponListView.as_view(), name='codm-weapon-list'),
    path('codm_weapons/add/', CODMWeaponCreateView.as_view(), name='codm-weapon-add'),
    path('codm_weapons/<int:pk>/edit/', CODMWeaponUpdateView.as_view(), name='codm-weapon-edit'),
    path('codm_weapons/<int:pk>/delete/', CODMWeaponDeleteView.as_view(), name='codm-weapon-delete'),
    
    path('about-us/', AboutUsView.as_view(), name='about-us'),
]
