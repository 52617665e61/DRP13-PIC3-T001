from django.test import SimpleTestCase
from django.urls import reverse, resolve
from appoitments.views import addAppoitment

class AppoitmentUrlTest(SimpleTestCase):
    def test_addAppoitment_url_resolves(self):
        url = reverse('addAppoitment')
        self.assertEqual(resolve(url).func, addAppoitment) 