from django.shortcuts import render
from .models import Post


def hello_blog(request):
  lista = [
    'Django', 'Python', 'Git', 'HTML', 'Banco de Dados', 'Linux', 'Nginx', 'Uwsgi', 'Systemcitl'
  ]
  
  list_posts = Post.objects.all() 
 
  data = {
    'name': 'Curso de Django 3',
    'lista_tecnologias':lista,
    'posts': list_posts 
  }

  return render(request, 'index.html', data)

def post_detail(request, id):
  post = Post.objects.get(id=id)
  return render(request, 'post_detail.html', {'post': post})