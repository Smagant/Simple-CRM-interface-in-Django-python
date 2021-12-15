from django.forms import ModelForm
from .models import Client, Video

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = '__all__'

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'