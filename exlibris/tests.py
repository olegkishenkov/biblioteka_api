import json
from random import random, randrange
from secrets import randbelow

from django.test import TestCase
from unittest.mock import patch
from django.urls import reverse, get_resolver
from .models import Author, Biography

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
    @patch('exlibris.models.Author.objects')
    def test_author_list_get(self, mocked_author):
        mocked_author.get.return_value = 1
        author = Author.objects.get(id=1)
        response = self.client.get(reverse('author-list'))
        self.assertEqual(response.status_code, 200)

    @patch('exlibris.views.Author')
    def test_author_list_get_functions(self, mocked_author):
        response = self.client.get(reverse('authors_functions'))
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

    @patch('exlibris.views.Author._get_bar')
    def test_author_detail_get__author_exists(self, mocked__get_bar):
        mocked__get_bar.return_value = 'some data'
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
        response = self.client.put(reverse('author-detail', args=[author.id]), data=json.dumps(data), content_type='application/json')
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

class TestJustAMathView(TestCase):
    def test_function_returns_1_if_given_number_below_0(self):
        data = {
            'key': -1*randbelow(1000000)
        }

        response = self.client.get(reverse('just_math'), data)
        self.assertEqual(int(response.content), 1)

    def test_function_returns_2_if_given_number_in_range_0_10(self):
        data = {
            'key': randrange(0, 10)
        }

        response = self.client.get(reverse('just_math'), data)
        self.assertEqual(int(response.content), 2)

    def test_function_returns_3_if_given_number_greater_than_10(self):
        data = {
            'key': randrange(11, 1000000000)
        }

        response = self.client.get(reverse('just_math'), data)
        self.assertEqual(int(response.content), 3)











