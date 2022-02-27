from django.test import SimpleTestCase
from django.urls import reverse, resolve

from core.views import index, user_login,logout_view, register, detailedView,search, blog, add_notes

class TestUrls(SimpleTestCase):
    
    def test_list_url_is_resolved(self):
        url = reverse('core:index')
        self.assertEquals(resolve(url).func, index)

        url = reverse('core:login')
        self.assertEquals(resolve(url).func, user_login)

        url = reverse('core:logout')
        self.assertEquals(resolve(url).func, logout_view)


        url = reverse('core:search')
        self.assertEquals(resolve(url).func, search)

        url = reverse('core:blog')
        self.assertEquals(resolve(url).func, blog)

        url = reverse('core:add-notes')
        self.assertEquals(resolve(url).func, add_notes)

        url = reverse('core:signup')
        self.assertEquals(resolve(url).func, register)