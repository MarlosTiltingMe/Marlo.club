from __future__ import unicode_literals
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models

class UserAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have a valid email address.')
		if not username:
			raise ValueError('Users must have a valid username')
		user = self.model(
			email=email,
			username=username,
		)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(email, username, password)
		user.is_admin = True
		user.save()
		return user

class UserAccount(AbstractBaseUser):
    email = models.EmailField(unique=True, blank=False)
    username = models.CharField(max_length=16, unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    avatar = models.CharField(max_length=1024, unique=False, blank=False, default='http://imgcp.aacdn.jp/img-a/auto/auto/global-aaj-front/article/2015/12/567e7867bf57d_567e785d7742b_1319131272.JPG')
    description = models.CharField(max_length=2028, unique=False, blank=False, default='No description available.')
    is_admin = models.BooleanField(default=False)
    count = models.IntegerField(null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserAccountManager()
    def get_date(self):
	    return self.created_at
    def get_count(self):
	    return self.count
    def __str__(self):
	    return self.username
    def get_image(self):
	    return self.avatar
    def get_desc(self):
	    return self.description
    def get_full_name(self):
	    return self.full_name
    def get_short_name(self):
	    print('a')
    @property
    def is_superuser(self):
	    return self.is_admin
    @property
    def is_staff(self):
	    return self.is_admin
    def has_perm(self, obj=None):
	    return self.is_admin
    def has_module_perms(self, app_label):
	    return self.is_admin

class Posts(models.Model):
    title_text = models.CharField(max_length=72, primary_key=True)
    author = models.CharField(max_length=30)
    body_text = models.CharField(max_length=2048)
    img = models.CharField(max_length=1024)
    log_text = models.CharField(max_length=9000, default="No logs available.")
    def __str__(self):
        return self.title_text

class Comments(models.Model):
	parent_thread = models.ForeignKey(Posts, on_delete=models.CASCADE)
	comment_text = models.CharField(max_length=1024)
	author = models.CharField(max_length=30, default='Anon')
	image = models.ForeignKey(UserAccount, on_delete=models.CASCADE, default=None, null=True, blank=True)
	def __str__(self):
		return self.comment_text
	def get_image(self):
		return self.image
