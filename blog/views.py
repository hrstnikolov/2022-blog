from msilib.schema import ListView
from .models import Post
from django.views.generic import ListView


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'