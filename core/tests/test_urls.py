from django.test import SimpleTestCase
from django.urls import reverse, resolve

from core.views import index, user_login,logout_view, register, detailedView,search, blog, add_notes

class TestUrls(SimpleTestCase):
    
    def test_index_url_is_resolved(self):
        url = reverse('core:index')
        self.assertEquals(resolve(url).func, index)

    def test_login_url_is_resolve(self):
        url = reverse('core:login')
        self.assertEquals(resolve(url).func, user_login)

    def test_logout_url_is_resolves(self):
        url = reverse('core:logout')
        self.assertEquals(resolve(url).func, logout_view)

    def test_search_url_is_resolves(self):
        url = reverse('core:search')
        self.assertEquals(resolve(url).func, search)
    
    def test_blog_url_is_resolves(self):
        url = reverse('core:blog')
        self.assertEquals(resolve(url).func, blog)

    def test_add_notes_url_is_resolves(self):
        url = reverse('core:add-notes')
        self.assertEquals(resolve(url).func, add_notes)

    def test_signupp_url_is_resolves(self):
        url = reverse('core:signup')
        self.assertEquals(resolve(url).func, register)


    def test_detailed_blog_url_is_resolves(self):
        url = reverse('core:detailed-blog', args=['some-slug'])
        self.assertEquals(resolve(url).func, detailedView)
    
