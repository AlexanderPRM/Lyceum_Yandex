from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from users.managers import UserManager
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('почта'), unique=True, blank=False)
    password = models.CharField(_('пароль'), max_length=128)
    first_name = models.CharField(_('имя'), max_length=30, blank=True)
    last_name = models.CharField(_('фамилия'), max_length=30, blank=True)
    date_joined = models.DateTimeField(
                                    _('дата регистрации'),
                                    auto_now_add=True)
    is_active = models.BooleanField(_('активный'), default=True)
    is_staff = models.BooleanField(_('персонал'), default=False,)
    birthday = models.DateField(verbose_name='день рождения', null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
