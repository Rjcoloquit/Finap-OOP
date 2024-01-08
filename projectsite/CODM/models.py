from django.db import models

class CODMBaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CODMPlayer(CODMBaseModel):
    username = models.CharField(max_length=100, unique=True)
    level = models.IntegerField(default=1)
    rank = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.username


class CODMWeapon(CODMBaseModel):
    name = models.CharField(max_length=100)
    damage = models.IntegerField()
    fire_rate = models.FloatField()
    ammo_capacity = models.IntegerField()
    weapon_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CODMWeaponAssault(CODMWeapon):
    attachments = models.CharField(max_length=250)
    recoil = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} (Assault)"


class CODMWeaponSMG(CODMWeapon):
    attachments = models.CharField(max_length=250)
    mobility = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} (SMG)"


class CODMWeaponSniper(CODMWeapon):
    zoom_levels = models.IntegerField()
    bolt_action = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} (Sniper)"


class CODMWeaponShotgun(CODMWeapon):
    pellet_count = models.IntegerField()
    spread_range = models.FloatField()

    def __str__(self):
        return f"{self.name} (Shotgun)"


class CODMWeaponLMG(CODMWeapon):
    magazine_size = models.IntegerField()
    suppression = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} (LMG)"


class CODMWeaponKnives(CODMWeapon):
    throwable = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} (Knives)"


