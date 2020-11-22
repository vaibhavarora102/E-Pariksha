from django.forms import ModelForm
from .models import ansMCQ25, ansMCQ10, ansQnA10


class formQnA10(ModelForm):
    class Meta:
        model = ansMCQ25
        fields = '__all__'
class formMCQ10(ModelForm):
    class Meta:
        model = ansMCQ10
        fields = '__all__'
class formMCQ25(ModelForm):
    class Meta:
        model = ansQnA10
        fields = '__all__'