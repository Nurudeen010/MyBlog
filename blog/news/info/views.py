from django.shortcuts import render
from django.views import generic
from .models import Pos


class PostListView(generic.ListView):
    queryset = Pos.objects.filter(status=1).order_by('-created_at')
    template_name = 'info/index.html'


class PostDetailView(generic.DetailView):
    model = Pos
    template_name = 'info/info_detail.html'