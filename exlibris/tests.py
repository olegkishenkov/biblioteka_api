from django.test import TestCase
from django.urls import reverse, get_resolver
from .models import Author

# Create your tests here.

def multiply(a, b):
    assert isinstance(a, int)
    return a*b

try:
    multiply(40, 20)
except IndexError:
    print('Error occured')
finally:
    print('program finished')


class TestExlibrisViews(TestCase):
    def test_author_list_get(self):
        response = self.client.get(reverse('author-list'))
        self.assertEqual(response.status_code, 200)

    def test_author_list_post__form_invalid(self):
        name = ''
        data = {
            'name': name
        }
        self.assertFalse(Author.objects.filter(name=name))
        author = Author.objects.create(name=name)
        response = self.client.post(reverse('author-list'), data)
        self.assertEqual(response.status_code, 400)
        self.assertTrue(Author.objects.filter(id=author.id, name=author.name))

    def test_author_list_post__form_valid(self):
        name = 'asdf'
        data = {
            'name': name
        }
        self.assertFalse(Author.objects.filter(name=name))
        response = self.client.post(reverse('author-list'), data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Author.objects.filter(name=name))


    def test_author_detail_get__author_exists(self):
        author = Author.objects.create(name='asdf')
        response = self.client.get(reverse('author-detail', args=[author.id]))
        self.assertEqual(response.status_code, 200)

    def test_author_detail_get__author_does_not_exist(self):
        author = Author.objects.create(name='asdf')
        response = self.client.get(reverse('author-detail', args=[author.id+1]))
        self.assertEqual(response.status_code, 404)

    def test_author_detail_put__author_exists(self):
        author = Author.objects.create(name='asdf')
        data = {
            'id': author.id,
            'name': 'zxcv'
        }
        response = self.client.put(reverse('author-detail', args=[author.id]), data)
        self.assertEqual(response.status_code, 200)

    def test_author_detail_put__author_does_not_exist(self):
        author = Author.objects.create(name='asdf')
        data = {
            'id': author.id,
            'name': 'zxcv'
        }
        response = self.client.put(reverse('author-detail', args=[author.id+1]), data)
        self.assertEqual(response.status_code, 404)

    def test_author_detail_delete__author_exists(self):
        author = Author.objects.create(name='asdf')
        response = self.client.delete(reverse('author-detail', args=[author.id]))
        self.assertEqual(response.status_code, 204)

    def test_author_detail_delete__author_does_not_exist(self):
        author = Author.objects.create(name='asdf')
        response = self.client.delete(reverse('author-detail', args=[author.id+1]))
        self.assertEqual(response.status_code, 404)

    def biography_list_get(self):
        author = Author(name='asdf')
        biography = Biography(author=author, date_born='1980-01-01', place_born='England', education='Oxford')
        response = rest.get(reverse('biography-list'))
        self.assertEqual(response.status_code, 200)

    def biography_list_post__form_valid(self):
        author = Author.objects.create(name='asdf')
        author.save()
        data = {
            'author': author.id,
            'date_born': '1980-01-01',
            'place_born': 'England',
            'education': 'Oxford'
        }
        response = self.request(reverse('biography-list'), data=data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Author.objects.filter(name=data.name))

    def biography_list_post__form_invalid_author_not_unique(self):
        author = Author.objects.create(name='asdf')
        author.save()
        data = {
            'author': author.id,
            'date_born': '1980-01-01',
            'place_born': 'England',
            'education': 'Oxford'
        }
        biography = Biography.objects.create(data)
        response = self.request(reverse('biography-list'), data=data)
        self.assertEqual(response.status_code, 400)










