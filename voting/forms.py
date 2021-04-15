from django.forms import ModelForm
from .models import *


class VoteForm(ModelForm):

    class Meta:

        model = Poll
        fields = '__all__'


