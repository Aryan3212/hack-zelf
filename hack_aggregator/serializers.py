from rest_framework import serializers
from .models import Author, Content
from .hack_api import get_author
class ContentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        author = Author.objects.filter(id = obj.author)
        if author.count() == 1:
            return author
        else:
            retries = 0
            returnedAuthor = {}
            while retries < 3:
                returnedAuthor = get_author(obj.author)
                if returnedAuthor.status_code == 200:
                    break
                retries += 1
            if returnedAuthor and returnedAuthor.status_code != 200:
                return None
            try:
                savedAuthor = {}
                savedAuthor['id'] = returnedAuthor['unique_id']
                savedAuthor['name'] = returnedAuthor['info']['name']
                savedAuthor['platform'] = returnedAuthor['info']['platform']
                savedAuthor['username'] = returnedAuthor['username']
                savedAuthor['avatar'] = returnedAuthor['avatar']['urls'][0]
                savedAuthor['profile_text'] = returnedAuthor['texts']['profile_text']
                savedAuthor['followers'] = int(returnedAuthor['stats']['digg_count']['followers']['count'])
                saved = Author(**savedAuthor).save()
            except:
                return None


    class Meta:
        model = Content
        fields = ['id', 'created_at', 'author', 'main_text', 'origin_url', 'media', 'likes', 'views', 'comments']
