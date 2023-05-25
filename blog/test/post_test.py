import json

from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post, Category, Tag, Comment, LikeDislike
from users.models import User

client = Client()


# Create your tests here.
class TestBlog(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(name='python backend', )
        self.tag = Tag.objects.create(name='Python', )
        self.user = User.objects.create(
            email='for@mail.ru',
            username='for',
            password='1'
        )

        self.post = Post.objects.create(

            title='backend',
            text='kgegslgjlkdsjglksjglk',
            category=self.category,
            tag=self.tag,
            author=self.user
        )
        client.login(username=self.user.username, password='1')
        self.comment = Comment.objects.create(post=self.post, author=self.user)
        self.like_dislike = LikeDislike.objects.create(user=self.user, post=self.post)
        self.post_data = {
            "title": 'test_title1',
            "body": 'body',
            "author": self.user,
            "category": self.category
        }

        self.new_post = {
            "title": "steweweqewring",
            "text": "wwww",
            "tag": self.tag.id,
            "category": self.category.id
        }

        self.comment_data = {
            "content": "strinadadssg"
        }

    # Post
    def test_post_list(self):
        url = reverse("post-list")
        client.force_login(user=self.user)
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_delete(self):
        url = reverse('post-detail', kwargs={"slug": self.post.slug})
        client.force_login(user=self.user)
        response = client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_post_get(self):
        url = reverse('post-detail', kwargs={"slug": self.post.slug})
        client.force_login(user=self.user)
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_create(self):
        client.force_login(user=self.user)
        url = reverse('post-list')
        response = client.post(url, data=self.new_post)

        self.assertEquals(response.status_code, 201)
        self.assertNotEqual(response.status_code, 400)
        self.assertEqual(response.data["title"], self.new_post["title"])

    # Comment

    def test_comment_post(self):
        client.force_login(user=self.user)
        url = reverse('comment-add', kwargs={"slug": self.post.slug})

        response = client.post(url, data=self.comment_data)

        self.assertEqual(response.status_code, 201)

        self.assertNotEqual(response.status_code, 400)

    def test_comment_delete(self):
        client.force_login(user=self.user)
        url = reverse('comment-detail', kwargs={"pk": self.comment.id})
        response = client.delete(url)

        self.assertEqual(response.status_code, 204)

    def test_comment_get(self):
        client.force_login(user=self.user)
        url = reverse('comment-detail', kwargs={"pk": self.comment.id})
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_comment_put(self):
        client.force_login(user=self.user)
        url = reverse('comment-detail', kwargs={"pk": self.comment.id})
        data = {
            "content": "stridadadsnadadssg",
            "parent": self.comment.id
        }
        response = client.put(url, data=data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["content"], data["content"])

    # LikeDislike

    def test_like_post(self):
        self.like = {
            "type": 1
        }
        self.dislike = {
            "type": -1
        }

        url = reverse('like_dislike', kwargs={"slug": self.post.slug})
        client.force_login(user=self.user)
        response = client.post(url, data=self.dislike)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 400)
        self.assertEqual(response.data["type"], self.dislike["type"])

    def test_like_list(self):
        url = reverse('like_dislike-list')
        client.force_login(user=self.user)
        response = client.get(url)
        self.assertEqual(response.status_code, 200)


# Category
class TestCategory(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(name='python backend', )

    def test_list(self):
        url = reverse('category-list')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)


# Tag
class TestTag(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(name='python backend', )

    def test_list(self):
        url = reverse('tag-list')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
