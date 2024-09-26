from django.forms import  ModelForm
from .models import userInfo
class userinfo(ModelForm):
    class Meta:
        model = userInfo 
        fields=['Name','email','Address','MobNO']
        

