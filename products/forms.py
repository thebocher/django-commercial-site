from django.forms import ModelForm

from .models import Feedback, Customer

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['description', 'attitude']

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ('user', 'pfp')