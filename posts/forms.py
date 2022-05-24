from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content']
        
        # 모든 필드 적용
        # fields = '__all__'