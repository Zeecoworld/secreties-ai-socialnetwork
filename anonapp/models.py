from django.db import models
from textblob import TextBlob
import random
# Create your models here


default_image_urls = [
    "https://images.pexels.com/photos/685674/pexels-photo-685674.jpeg?cs=srgb&dl=pexels-neosiam-685674.jpg&fm=jpg",
    "https://images.pexels.com/photos/3880049/pexels-photo-3880049.jpeg?cs=srgb&dl=pexels-jakson-martins-3880049.jpg&fm=jpg",
    "https://images.pexels.com/photos/228844/pexels-photo-228844.jpeg?cs=srgb&dl=pexels-james-sutton-228844.jpg&fm=jpg",
    "https://images.pexels.com/photos/5457316/pexels-photo-5457316.jpeg?cs=srgb&dl=pexels-preet-lovi-5457316.jpg&fm=jpg",
    "https://images.pexels.com/photos/3179911/pexels-photo-3179911.jpeg?cs=srgb&dl=pexels-pablo-ezequiel-nieva-3179911.jpg&fm=jpg",
    "https://images.pexels.com/photos/1482476/pexels-photo-1482476.jpeg?cs=srgb&dl=pexels-sebastiaan-stam-1482476.jpg&fm=jpg",
    "https://images.pexels.com/photos/1097456/pexels-photo-1097456.jpeg?cs=srgb&dl=pexels-sebastiaan-stam-1097456.jpg&fm=jpg",
    "https://images.pexels.com/photos/3066542/pexels-photo-3066542.jpeg?cs=srgb&dl=pexels-warley-venancio-3066542.jpg&fm=jpg",
    "https://images.pexels.com/photos/3216904/pexels-photo-3216904.jpeg?cs=srgb&dl=pexels-laura-garcia-3216904.jpg&fm=jpg",
    "https://images.pexels.com/photos/1482480/pexels-photo-1482480.jpeg?cs=srgb&dl=pexels-sebastiaan-stam-1482480.jpg&fm=jpg",
    "https://images.pexels.com/photos/1097486/pexels-photo-1097486.jpeg?cs=srgb&dl=pexels-sebastiaan-stam-1097486.jpg&fm=jpg",
    "https://images.pexels.com/photos/5600238/pexels-photo-5600238.jpeg?cs=srgb&dl=pexels-a-koolshooter-5600238.jpg&fm=jpg",
    "https://images.pexels.com/photos/5600205/pexels-photo-5600205.jpeg?cs=srgb&dl=pexels-a-koolshooter-5600205.jpg&fm=jpg",
    
]

def choice():
    return random.choice(default_image_urls)


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



class Post(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=128,choices=CHOICES_STATUS, verbose_name="category")
    description = models.CharField(max_length=2000)
    blob = models.DecimalField(max_digits=3, decimal_places=2)
    banner_image_url = models.URLField(help_text="Provide a banner image for your post", default=choice) 
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('post_detail', kwargs={'pk':self.pk})

    
   





