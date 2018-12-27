from django import forms
from .models import Attendant
from django.forms import Field
from django.utils.translation import ugettext_lazy

Field.default_error_messages = {
    'required': ugettext_lazy('وارد کردن تمامی فیلدها ضروری است.'),
    'invalid': ugettext_lazy('اطلاعات وارد شده صحیح نمی‌باشد.'),
    'unique': ugettext_lazy('ایمیل وارد شده تکراری است.')
}


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Attendant
        fields = ('first_name', 'last_name', 'email', 'major', 'university')
