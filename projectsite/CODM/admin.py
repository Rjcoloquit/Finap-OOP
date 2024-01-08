from django.contrib import admin
from .models import CODMPlayer, CODMWeapon,  CODMWeaponAssault, CODMWeaponSMG, CODMWeaponSniper, CODMWeaponShotgun, CODMWeaponLMG, CODMWeaponKnives

@admin.register(CODMPlayer)
class CODMPlayerAdmin(admin.ModelAdmin):
    list_display = ('username', 'level', 'rank')

class BaseCODMWeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'damage', 'fire_rate', 'ammo_capacity', 'weapon_type')


@admin.register(CODMWeapon)
class CODMWeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'damage', 'fire_rate', 'ammo_capacity', 'weapon_type')


@admin.register(CODMWeaponAssault)
class CODMWeaponAssaultAdmin(admin.ModelAdmin):
    list_display = ('name', 'damage', 'fire_rate', 'ammo_capacity', 'weapon_type')


@admin.register(CODMWeaponSMG)
class CODMWeaponSMGAdmin(admin.ModelAdmin):
    list_display = ('name', 'damage', 'fire_rate', 'ammo_capacity', 'weapon_type')


@admin.register(CODMWeaponSniper)
class CODMWeaponSniperAdmin(admin.ModelAdmin):
    list_display = ('name', 'damage', 'fire_rate', 'ammo_capacity', 'weapon_type')


@admin.register(CODMWeaponShotgun)
class CODMWeaponShotgunAdmin(admin.ModelAdmin):
    list_display = ('name', 'damage', 'fire_rate', 'ammo_capacity', 'weapon_type')


@admin.register(CODMWeaponLMG)
class CODMWeaponLMGAdmin(admin.ModelAdmin):
    list_display = ('name', 'damage', 'fire_rate', 'ammo_capacity', 'weapon_type')


@admin.register(CODMWeaponKnives)
class CODMWeaponKnivesAdmin(admin.ModelAdmin):
    list_display = ('name', 'damage', 'fire_rate', 'ammo_capacity', 'weapon_type')


