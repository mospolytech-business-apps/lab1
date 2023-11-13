from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, Email, FirstName, LastName, password=None):
        user = self.model(
            Email=self.normalize_email(Email),
            FirstName=FirstName,
            LastName=LastName,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, Email, FirstName, LastName, password=None):
        user = self.create_user(
            Email=Email,
            FirstName=FirstName,
            LastName=LastName,
            password=password,
        )
        user.Active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user
