from django.core.management.base import BaseCommand
from CODM.models import CODMPlayer, CODMWeapon

class Command(BaseCommand):
    help = 'Creates initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_codm_players()
        self.create_codm_weapons()

    def create_codm_players(self):
        player1 = CODMPlayer(username="kyle", level=30, rank="Master")
        player2 = CODMPlayer(username="Ken", level=25, rank="Diamond")
        player3 = CODMPlayer(username="Rolando", level=40, rank="Legendary")
        player4 = CODMPlayer(username="Darwin", level=15, rank="Platinum")
        player5 = CODMPlayer(username="Rafael", level=22, rank="Gold")
        player6 = CODMPlayer(username="Michael", level=18, rank="Silver")
        player7 = CODMPlayer(username="Wynne", level=35, rank="Elite")
        player8 = CODMPlayer(username="Owen", level=28, rank="Pro")
        player9 = CODMPlayer(username="Ronald", level=32, rank="Master")
        player10 = CODMPlayer(username="Lester", level=23, rank="Diamond")

        codm_players = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10]
        for player in codm_players:
            player.save()

        self.stdout.write(self.style.SUCCESS('Successfully created CODM players.'))

    def create_codm_weapons(self):
        weapon1 = CODMWeapon(name="M4", damage=40, fire_rate=600, ammo_capacity=30, weapon_type="Assault")
        weapon2 = CODMWeapon(name="Fennic", damage=35, fire_rate=800, ammo_capacity=25, weapon_type="SMG")
        weapon3 = CODMWeapon(name="DL Q33", damage=90, fire_rate=120, ammo_capacity=5, weapon_type="Sniper")
        weapon4 = CODMWeapon(name="KRM", damage=60, fire_rate=150, ammo_capacity=8, weapon_type="Shotgun")
        weapon5 = CODMWeapon(name="RPD", damage=48, fire_rate=550, ammo_capacity=50, weapon_type="LMG")
        weapon6 = CODMWeapon(name="Karambit", damage=100, fire_rate=1, ammo_capacity=1, weapon_type="Melee")
        weapon7 = CODMWeapon(name="50 GS", damage=30, fire_rate=400, ammo_capacity=12, weapon_type="Pistol")
        weapon8 = CODMWeapon(name="QQ9", damage=38, fire_rate=700, ammo_capacity=30, weapon_type="SMG")
        weapon9 = CODMWeapon(name="SMRS", damage=80, fire_rate=60, ammo_capacity=1, weapon_type="Launcher")
        weapon10 = CODMWeapon(name="J358", damage=45, fire_rate=500, ammo_capacity=6, weapon_type="Pistol")

        codm_weapons = [weapon1, weapon2, weapon3, weapon4, weapon5, weapon6, weapon7, weapon8, weapon9, weapon10]
        for weapon in codm_weapons:
            weapon.save()

        self.stdout.write(self.style.SUCCESS('Successfully created CODM weapons.'))
