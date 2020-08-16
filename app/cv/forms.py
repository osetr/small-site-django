from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Post


class PostForm(forms.ModelForm):
    full_name = forms.CharField(max_length=35, required=True)
    phone = PhoneNumberField(required=True)
    link = forms.URLField(label="Your website", required=True)

    class Meta:
        model = Post
        fields = "__all__"
