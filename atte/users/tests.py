from django.test import TestCase


# from social_auth.tests.client import SocialClient

# class SomeTestClass(TestCase):

#     client = SocialClient
#     user = {
#         'first_name': 'Django',
#         'last_name': 'Reinhardt',
#         'verified': True,
#         'name': 'Django Reinhardt',
#         'locale': 'en_US',
#         'hometown': {
#             'id': '12345678',
#             'name': 'Any Town, Any State'
#         },
#         'expires': '4812',
#         'updated_time': '2012-01-29T19:27:32+0000',
#         'access_token': 'dummyToken',
#         'link': 'http://www.facebook.com/profile.php?id=1234',
#         'location': {
#             'id': '108659242498155',
#             'name': 'Chicago, Illinois'
#         },
#         'gender': 'male',
#         'timezone': -6,
#         'id': '1234',
#         'email': 'user@domain.com'
#     }

#     def test_something(self):
#         self.client.login(self.user, backend='facebook')
#         # do something with the logged in user.

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
