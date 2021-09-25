from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Trip

class tripModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='Omar',password='omarpass')
        test_user.save()
        test_trip = Trip.objects.create(
            owner = test_user,
            title = 'Austria',
            comments = 'Trip to Vienna'
        )
        test_trip.save()

    def test_blog_content(self):
        trip = Trip.objects.get(id=1)
        self.assertEqual(str(trip.owner), 'Omar')
        self.assertEqual(trip.title, 'Austria')
        self.assertEqual(trip.comments, 'Trip to Vienna')

class APITest(APITestCase):
    def test_list(self):
        response = self.client.get(reverse('trips_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):
        test_user = get_user_model().objects.create_user(username='Omar',password='omarpass')
        test_user.save()
        test_trip = Trip.objects.create(
            owner = test_user,
            title = 'Austria',
            comments = 'Trip to Vienna'
        )
        test_trip.save()
        response = self.client.get(reverse('trips_detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id':1,
            'title': test_trip.title,
            'comments': test_trip.comments,
            'owner': test_user.id,
        })


    def test_create(self):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()
        url = reverse('trips_list')
        data = {
            "title":"Berlin was a lot of Fun!",
            "comments":"Trip to Berlin was great",
            "owner":test_user.id,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, test_user.id)
        self.assertEqual(Trip.objects.count(), 1)
        self.assertEqual(Trip.objects.get().title, data['title'])

    def test_update(self):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()
        test_trip = Trip.objects.create(
            owner = test_user,
            title = 'Austria 2',
            comments = 'Trip to Vienna'
        )
        test_trip.save()
        url = reverse('trips_detail',args=[test_trip.id])
        data = {
            "title":"Berlin was a lot of Fun!",
            "comments":"Trip to Berlin was great",
            "owner":test_user.id,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, url)
        self.assertEqual(Trip.objects.count(), test_trip.id)
        self.assertEqual(Trip.objects.get().title, data['title'])

    def test_delete(self):
        """Test the api can delete a trip."""

        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_trip = Trip.objects.create(
            owner = test_user,
            title = 'Austria',
            comments = 'Trip to Vienna'
        )
        test_trip.save()
        trip = Trip.objects.get()
        url = reverse('trips_detail', kwargs={'pk': trip.id})
        response = self.client.delete(url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)