from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import SimpleUser
# #
# # class SimpleUserForm(UserCreationForm):
# #
# #     # password = forms.CharField(widget=forms.PasswordInput())
# #     class Meta(UserCreationForm.Meta):
# #         model = SimpleUser
# #         fields = ('email','username', 'user_avatar')
# #
# #
# # class SimpleUserChangeForm(UserChangeForm):
# #
# #     class Meta(UserChangeForm.Meta):
# #         model = SimpleUser
# #         fields = ('email','username', 'user_avatar')
#
# # from django.contrib.auth.models import User
# #
# # user_to_change = User.objects.get(username=login)
# # user_to_change.save()
#
#
class SimpleUserForm(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    class Meta(UserCreationForm.Meta):
        model = SimpleUser
        fields = ('username','user_name','user_surname','email', 'user_avatar')

class SimpleUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = SimpleUser
        fields = ('username','user_name','user_surname','email', 'user_avatar')

#
# # from django.utils import timezone
# # from django.contrib.auth.models import User
# #
# #
# # class LoginForm(forms.Form):
# #
# # 	username = forms.CharField()
# # 	password = forms.CharField(widget=forms.PasswordInput)
# #
# # 	def __init__(self, *args, **kwargs):
# # 		super(LoginForm, self).__init__(*args, **kwargs)
# # 		self.fields['username'].label = 'Логин'
# # 		self.fields['password'].label = 'Пароль'
# #
# # 	def clean(self):
# # 		username = self.cleaned_data['username']
# # 		password = self.cleaned_data['password']
# # 		if not User.objects.filter(username=username).exists():
# # 			raise forms.ValidationError('Пользователь с данным логином не зарегистрирован в системе!')
# # 		user = User.objects.get(username=username)
# # 		if user and not user.check_password(password):
# # 			raise forms.ValidationError('Неверный пароль!')
# #
# # class RegistrationForm(forms.ModelForm):
# # 	password = forms.CharField(widget=forms.PasswordInput)
# # 	password_check = forms.CharField(widget=forms.PasswordInput)
# #
# # 	class Meta:
# # 		model = User
# # 		fields = [
# # 			'username',
# # 			'password',
# # 			'password_check',
# # 			'first_name',
# # 			'last_name',
# # 			'email'
# # 		]
# #
# # 	def __init__(self, *args, **kwargs):
# # 		super(RegistrationForm, self).__init__(*args, **kwargs)
# # 		self.fields['username'].label = 'Логин'
# # 		self.fields['password'].label = 'Пароль'
# # 		self.fields['password'].help_text = 'Придумайте пароль'
# # 		self.fields['password_check'].label = 'Повторите пароль'
# # 		self.fields['first_name'].label = 'Имя'
# # 		self.fields['last_name'].label = 'Фамилия'
# # 		self.fields['email'].label = 'Ваша почта'
# # 		self.fields['email'].help_text = 'Пожалуйста, указывайте реальный адрес'
# #
# #
# # 	def clean(self):
# # 		username = self.cleaned_data['username']
# # 		password = self.cleaned_data['password']
# # 		password_check = self.cleaned_data['password_check']
# # 		email = self.cleaned_data['email']
# # 		if User.objects.filter(username=username).exists():
# # 			raise forms.ValidationError('Пользователь с данным логином уже зарегистрирован в системе!')
# # 		if User.objects.filter(email=email).exists():
# # 			raise forms.ValidationError('Пользователь с данным почтовым адресом уже зарегистрирован!')
# # 		if password != password_check:
# # 			raise forms.ValidationError('Ваши пароли не совпадают! Попробуйте снова!')
