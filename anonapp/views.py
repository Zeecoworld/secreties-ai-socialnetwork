from django.shortcuts import render,redirect
from .models import Post
from textblob import TextBlob
from django.contrib import messages
from django.views.generic.list import ListView
from django.http.response import HttpResponse
from django.http import HttpResponse
# Create your views here.
# CHOICES_STATUS = (
#         (Davido, 'Davido'),
#         (Wizkid, 'Wizkid'),
#         (Drake, 'Drake'),
#         (JBeiber , 'JBeiber'),
#         (Cardib,  'Cardib')
#     )

def policy(request):


    return render(request, "policy.html")




def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /adminnnnn/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")


class FirstView(ListView):
    model = Post
    paginate_by = 7
    template_name = 'index.html'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(category='Davido').order_by('blob')
        return context
        # youtube = format_youtube(context['post_list'].description)
        # print(context['post_list'])
        # for p in context['post_list']:
        #     print(format_youtube(p.description))
        


class  CardView(ListView):
    model = Post
    paginate_by = 7
    template_name = 'cardib.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(category='Cardib').order_by('blob')
        return context



class WizView(ListView):
    model = Post
    paginate_by = 7
    template_name = 'wizkid.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(category='Wizkid').order_by('blob')
        return context


class DrakeView(ListView):
    model = Post
    paginate_by = 7
    template_name = 'drake.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(category='Drake').order_by('blob')
        return context



class JustView(ListView):
    model = Post
    paginate_by = 7
    template_name = 'justin.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(category='JBeiber').order_by('blob')
        return context



def post(request):
     if request.method == "POST":
        #  photos = request.FILES["photo"]
         name = request.POST["nam"]
         celeb_select = request.POST["se"]
         description = request.POST["text"]
         blob_rate = TextBlob(description)
         desc_blob = blob_rate.sentiment.polarity
         post = Post.objects.create(name=name,category=celeb_select,description=description,blob=desc_blob)
         post.save()
         messages.info(request, 'Your thought was submitted and check its rating pls')
         return redirect("post")


     else:
         return render(request, "edit-profile.html")

    


     return render(request, "edit-profile.html")