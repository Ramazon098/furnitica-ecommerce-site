from django.contrib.auth.models import BaseUserManager  

from knox.auth import AuthToken


# Create your managers here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email must be set.")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.save()

        user.set_password(password)
        user.save(using=self._db)

        AuthToken.objects.create(user)

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(email, password, **extra_fields)
