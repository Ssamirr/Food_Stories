from django.db import models
from django.contrib.auth.models import AbstractUser
from stories.tools.slug_generator import slugify
from django.urls import reverse_lazy
from datetime import datetime
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    image = models.ImageField(upload_to='user_images', null=True, blank=True)
    bio = models.TextField(_('Biography'), null=True, blank=True)
    slug= models.SlugField('slug',max_length=255, editable = False , unique = True)


    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_avatar(self):
        if self.image:
            return self.image.url
        return 'https://cdt.org/files/2015/10/2015-10-06-FB-person.png'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.username)}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('home')

    @property
    def is_author(self):
        return self.groups.filter(name='Author').exists()


# Create your models here.
