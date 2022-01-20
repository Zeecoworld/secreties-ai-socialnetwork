from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from anonapp.models import Post
from django.shortcuts import reverse
# class CategorySitemap(Sitemap):
#     def items(self):
#         return Post.objects.all

Davido = 'Davido'
Wizkid = 'Wizkid'
Drake = 'Drake'
JBeiber = 'JBeiber'
Cardib = 'Cardib'

CHOICES_STATUS = (
        (Davido, 'Davido'),
        (Wizkid, 'Wizkid'),
        (Drake, 'Drake'),
        (JBeiber , 'JBeiber'),
        (Cardib,  'Cardib')
    )

class StaticSiteMap(Sitemap):
    priority = 1.0
    changefreq = 'weekly'

    def items(self):
        return ['policy']

    def location(self,item):
        return reverse(item)


class PostSitemap(Sitemap):
    priority = 0.7
    changefreq = 'daily'

    def items(self):
        return ['index','wizkid','just','drake','card']

    def location(self,item):
        return reverse(item)

    # def lastmod(self, obj):
    #     return obj.create_date