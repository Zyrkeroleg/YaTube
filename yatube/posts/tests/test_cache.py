from django.test import Client, TestCase
from django.urls import reverse
from django.core.cache import cache
from posts.models import Post, User


class CacheTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.post = Post.objects.create(
            author=User.objects.create_user(username='HasNoName'),
            text='Тестовая запись для создания поста')

    def setUp(self):
        self.guest_client = Client()
        self.user = User.objects.create_user(username='mob2556')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_cache_index(self):
        response = self.authorized_client.get(reverse('posts:index'))
        resp_1 = response.content
        post = Post.objects.get(id=1)
        post.delete()
        response_2 = self.authorized_client.get(reverse('posts:index'))
        resp_2 = response_2.content
        self.assertTrue(resp_1 == resp_2)
        cache.clear()
        response_3 = self.authorized_client.get(reverse('posts:index'))
        resp_3 = response_3.content
        self.assertTrue(resp_3 != resp_2)
