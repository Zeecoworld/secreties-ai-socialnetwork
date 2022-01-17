from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from anonapp.models import Post

# class CategorySitemap(Sitemap):
#     def items(self):
#         return Post.objects.all
# CHOICES_STATUS = (
#         (Davido, 'Davido'),
#         (Wizkid, 'Wizkid'),
#         (Drake, 'Drake'),
#         (JBeiber , 'JBeiber'),
#         (Cardib,  'Cardib')
#     )

class StaticSiteMap(Sitemap):
    priority = 1.0
    changefreq = 'yearly'

    def items(self):
        return ['policy']

    def location(self,item):
        return reverse(item)


class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.filter(category=CHOICES_STATUS)
    
    def lastmod(self, obj):
        return obj.create_date