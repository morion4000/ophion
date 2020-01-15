from django.contrib.auth.models import User

if User.objects.count() == 0:
	admin = User.objects.create_user('ophion', 'morion4000@gmail.com', 'ophion')
	admin.is_superuser = True
	admin.is_staff = True
	admin.save()