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



class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.filter(category=CHOICES_STATUS)
    
    def lastmod(self, obj):
        return obj.created_at