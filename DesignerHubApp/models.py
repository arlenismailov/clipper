from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.utils import timezone
import uuid


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name=None, password=None):
        if not email:
            raise ValueError('Поле электронной почты обязательно')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name=None, password=None):
        user = self.create_user(email, first_name, last_name, password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin


class PasswordResetToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        now = timezone.now()
        return now - self.created_at < timezone.timedelta(hours=24)


class Category(models.Model):
    name = models.CharField(max_length=42)

    def __str__(self) -> str:
        return f'{self.name}'


class DesignerWork(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    design_title = models.CharField(max_length=65, unique=True, blank=True, null=True)
    media_data = models.ImageField(upload_to='media_data/')
    descriptions = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    hashtag = models.CharField(max_length=24, verbose_name='Хэштеги')
    views = models.PositiveIntegerField(default=0, verbose_name='Счетчик просмотров')
    likes = models.PositiveIntegerField(default=0, verbose_name='Счетчик лайков')
    publicated_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.last_name} - {self.designe_title}'


class View(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    designe = models.ForeignKey(DesignerWork, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'designe')

    def __str__(self):
        return f'{self.user.last_name}'


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    user_descriptions = models.TextField()

    def __str__(self) -> str:
        return f'{self.user.first_name}'


class UserSocialNetworkLink(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    social_network_title = models.CharField(max_length=32)
    link_to_social_networks = models.TextField()

    def __str__(self) -> str:
        return f'{self.user.user.first_name}'


class UserContactData(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    contact_title = models.CharField(max_length=32)
    contact_data = models.TextField()

    def __str__(self) -> str:
        return f'{self.user.user.first_name}'


class Favorite(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Пользователь')
    designs = models.ManyToManyField(DesignerWork, related_name='Избранные')

    def __str__(self):
        return f"{self.user} - {self.designs}"


class Like(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='like')
    designs = models.ManyToManyField(DesignerWork, related_name='favorites')

    def __str__(self):
        return f"{self.user} - {self.designs}"


class DesigneWorkReview(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    design = models.ForeignKey(DesignerWork, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self) -> str:
        return f'{self.user.user.first_name}'


class Chat(models.Model):
    user1 = models.ForeignKey(UserProfile, related_name='chats_initiated', on_delete=models.CASCADE)
    user2 = models.ForeignKey(UserProfile, related_name='chats_received', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user1', 'user2')

    def __str__(self):
        return f"Чат {self.user1.user.first_name} с {self.user2.user.first_name}"


class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Сообщения от {self.sender.user.first_name}, в {self.timestamp}"
