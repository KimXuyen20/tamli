from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        # if not username:
        #     raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
           
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
         
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    
    DOCTOR = 1
    CUSTOMER = 2

    ROLE_CHOICE = (
        (DOCTOR, 'Doctor'),
        (CUSTOMER, 'Customer'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
 
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)

    def full_name(self):
        return f'{self.first_name}{self.last_name}'
    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_role(self):
        if self.role == 1:
            user_role = 'Doctor'
        elif self.role == 2:
            user_role = 'Customer'
        return user_role

class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)    
    address = models.CharField(blank=True, max_length=50)
    photo = models.ImageField(blank=True, upload_to='uploads/photos/')
    country = models.CharField(null=True, blank=True, max_length=20)
    city = models.CharField(null=True, blank=True, max_length=20)


    @property
    def photo(self):
        if self.image:
            return self.image.url
        return f'{settings.STATIC_URL}images/avatar.svg'


    def __str__(self):
        return self.user.email
    
    def full_address(self):
        return self.address 