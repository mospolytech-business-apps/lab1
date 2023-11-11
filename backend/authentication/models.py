from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from offices.models import Office
from roles.models import Role
from authentication.managers import UserManager

class User(AbstractBaseUser,PermissionsMixin):
    OfficeID = models.ForeignKey(Office, on_delete=models.CASCADE,null=True)
    RoleID = models.ForeignKey(Role, on_delete=models.CASCADE,null=True)
    Email=models.EmailField(verbose_name="Email name",max_length=255,unique=True)
    password = models.CharField(max_length=255)
    FirstName=models.CharField(verbose_name="Имя",max_length=255)
    LastName=models.CharField(verbose_name="Фамилия",max_length=255)
    Birthday = models.DateField(null=True, blank=True)
    Active =models.BooleanField(verbose_name='Активирован',default=False)
    is_staff=models.BooleanField(verbose_name='Персонал',default=False)
    is_superuser=models.BooleanField(verbose_name='Администратор',default=False)
    is_client = models.BooleanField(verbose_name='Клиент', default=False)
    is_banned = models.BooleanField(verbose_name='Заблокирован', default=False)

    USERNAME_FIELD='Email'
    REQUIRED_FIELDS=['FirstName','LastName']

    objects = UserManager()

    def __str__(self):
        return self.Email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
