from django import forms
from .models import Post
from django.core.exceptions import ValidationError
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {'title' : forms.TextInput(attrs={
            'class' : 'title',
            'placeholder': '제목을 입력 하세요'}),
                   'content' : forms.Textarea(attrs={
                       'placeholder':'내용을 입력하세요'})}
        
        # 모든 필드 적용
        # fields = '__all__'
        
    def clean_title(self):
        # cleaned_data = 모든 form 클래스는 cleaned_data를 가지고 있다.
        # cleaned_data안에는 form필드를 정의할 떄 넣어준 유효성검증을 통과한 데이터가 있다.
        title = self.cleaned_data['title']
        if '*' in title:
            raise ValidationError("*는 포함될 수 없습니다.")
        
        return title