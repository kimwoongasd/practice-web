from .models import Post


def validate_post():
    # 1. 모든 포스트 데이터 가져오기
    posts = Post.objects.all()

    # 2. 각 포스트 데이터를 보면서 내용안 체크
    for post in posts:
        if '&' in post.content:
            print(post.id, '번 글에 &가 있습니다')
            
    # 3. 만약 '&'있다면 '&'삭제
            post.content = post.content.replace("&", "")
    # 4. 데이터 저장
            post.save()

        if post.dt_modified < post.dt_create:
            print(post.id, '번 글의 수정일이 생성일보다 과거입니다.')
            post.save()