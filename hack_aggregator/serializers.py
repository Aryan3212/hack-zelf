from rest_framework import serializers
from .models import Author, Content
from .hack_api import get_author
class ContentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        author = Author.objects.filter(id = obj.author)
        print(author.count())
        if author.count() == 1:
            print('returning')
            return author
        else:
            retries = 0
            print('asrt')
            returnedAuthor = {
                "status_code": 400
            }
            while returnedAuthor.status_code != 200 and retries < 3:
                returnedAuthor = get_author(obj.author)
                print(returnedAuthor)
                retries += 1
            if not author:
                return None
            try:
                savedAuthor = {}
                savedAuthor['id'] = author['unique_id']
                savedAuthor['name'] = author['info']['name']
                savedAuthor['platform'] = author['info']['platform']
                savedAuthor['username'] = author['username']
                savedAuthor['avatar'] = author['avatar']['urls'][0]
                savedAuthor['profile_text'] = author['texts']['profile_text']
                savedAuthor['followers'] = int(author['stats']['digg_count']['followers']['count'])
            except:
                return None


    class Meta:
        model = Content
        fields = ['id', 'created_at', 'author', 'main_text', 'origin_url', 'media', 'likes', 'views', 'comments']
