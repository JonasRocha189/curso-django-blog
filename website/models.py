from django.db import models

class Categorias(models.TextChoices):
  TECH = 'TC', 'Tecnologia'
  CR = 'CR', 'Curiosidades'
  GERAL = 'GR', 'Geral'

class Post(models.Model):
  title = models.CharField(max_length=100)
  sub_title = models.CharField(max_length=200)
  content = models.TextField()
  categories = models.CharField(
    max_length=2,
    choices=Categorias.choices,
    default=Categorias.GERAL,
  )

  imagem = models.ImageField(upload_to='posts', null=True, blank=True)

  def get_category_label(self):
    return self.get_categories_display()

  def __str__(self):
    return self.title