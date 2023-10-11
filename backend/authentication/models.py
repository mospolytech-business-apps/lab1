from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from offices.models import Office
from roles.models import Role
from authentication.managers import UserManager

class User(AbstractBaseUser,PermissionsMixin):
    office = models.ForeignKey(Office, on_delete=models.CASCADE,null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE,null=True)
    email=models.EmailField(verbose_name="Email name",max_length=255,unique=True)
    password = models.CharField(max_length=255)
    first_name=models.CharField(verbose_name="Имя",max_length=255)
    last_name=models.CharField(verbose_name="Фамилия",max_length=255)
    birthday = models.DateField(null=True, blank=True)
    is_active =models.BooleanField(verbose_name='Активирован',default=False)
    is_staff=models.BooleanField(verbose_name='Персонал',default=False)
    is_superuser=models.BooleanField(verbose_name='Администратор',default=False)
    is_client = models.BooleanField(verbose_name='Клиент', default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
