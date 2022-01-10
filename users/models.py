from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.managers import CustomUserManager
from users.validators import birthday_validator, phone_validator
from users.utils import user_directory_path


class Users(AbstractUser):
    email = models.EmailField('email address', unique=True)
    birthday = models.DateField('birthday', validators=[birthday_validator])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'birthday']

    objects = CustomUserManager()


class UserProfiles(models.Model):
    class RegionChoice(models.TextChoices):
        RU = 'RU', 'Russia'
        EN = 'EN', 'English'

    class GenderChoice(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'W', 'Female'

    user = models.OneToOneField(Users, unique=True, null=False,
                                db_index=True, on_delete=models.CASCADE)
    gender = models.CharField(verbose_name='gender', max_length=10, choices=GenderChoice.choices, default='Male')
    avatar = models.ImageField(verbose_name='avatar', upload_to=user_directory_path, blank=True)
    region = models.CharField(verbose_name='region', max_length=8, choices=RegionChoice.choices, default='Russia')
    phone = models.CharField(verbose_name='phone', validators=[phone_validator],
                             max_length=16, blank=True, help_text='+7..........')


@receiver(post_save, sender=Users)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfiles.objects.create(user=instance)


@receiver(post_save, sender=Users)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofiles.save()
