from django import forms
from .models import Post
#폼을 지정해서 마늘때는 class를 이용해서 만들게 ㅗ딥니다.
#forms.modelsForm을 필요 내부에 넣어주셔야 합니다.
class PostForm(forms.ModelForm):
    # Post 모델에 자료를 집어넣주기 위한 세부사항느 
    
    class Meta:
        model = Post
        fields = ('title', 'text')

