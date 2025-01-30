from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class MyUser(AbstractBaseUser, PermissionsMixin):
    mobile_number = models.CharField(max_length=10, blank=True, null=True)
    agree = models.BooleanField(default=False, blank=True)
    forget_password_token = models.CharField(max_length=300, blank=True)
    profile_img = models.ImageField(
        upload_to='profife_imgs', null=True, blank=True, default="{% static 'image/nav/profile.png' %}")

    title = models.CharField(max_length=100, null=True, blank=True)
    age = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    about_me = models.TextField(null=True, blank=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=30, default=None, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)

    created_at = models.DateTimeField(null=True, default=timezone.now)
    is_staff = True

    # Add your groups and user_permissions inside the class
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='myuser_groups',  # Custom related_name to avoid conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='myuser_permissions',  # Custom related_name to avoid conflict
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        super(MyUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def days_since_creation(self):
        return (timezone.now() - self.created_at).days
