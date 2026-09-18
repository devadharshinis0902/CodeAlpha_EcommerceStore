from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Order


class UserRegistrationForm(forms.ModelForm):
    """User Registration Form with Validation"""
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Choose a username'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'name@example.com'})
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Last Name'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Create a password (min 6 chars)'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Confirm your password'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError("This username is already taken. Please choose another.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError("An account with this email address already exists.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        if password and len(password) < 6:
            self.add_error('password', "Password must be at least 6 characters long.")

        return cleaned_data


class UserLoginForm(forms.Form):
    """User Login Form"""
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Username or Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Password'})
    )


class CheckoutForm(forms.ModelForm):
    """Order Checkout Form"""
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'John Doe'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'john@example.com'})
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': '123 Main Street, Apt 4B'})
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'New York'})
    )
    postal_code = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': '10001'})
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': '+1 (555) 000-1234'})
    )
    payment_method = forms.ChoiceField(
        choices=[
            ('Demo Cash on Delivery', 'Cash on Delivery (Demo)'),
            ('Demo Card Payment', 'Simulated Credit / Debit Card (Demo)'),
            ('Demo UPI / NetBanking', 'Simulated NetBanking / UPI (Demo)')
        ],
        widget=forms.RadioSelect(attrs={'class': 'form-radio'})
    )

    class Meta:
        model = Order
        fields = ['full_name', 'email', 'address', 'city', 'postal_code', 'phone', 'payment_method']
