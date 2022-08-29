from django.db import models
# from django.contrib.auth.models import User

from contas.models import Usuario

import uuid
from django.utils import timezone
from .softdelete import SoftDeleteManager
# Create your models here.

class BaseModel(models.Model):
    class Meta:
        abstract = True
        ordering = ["-criado_em"]
        
    uuid = models.UUIDField("UUID", max_length=255, blank=True, null=True, unique=True, default=uuid.uuid4)
    
    criado_em = models.DateTimeField("Criado em", auto_now_add=True)
    atualizado_em = models.DateTimeField("Atualizado em", auto_now=True)
    deletado_em = models.DateTimeField("Deletado em", null=True, blank=True)
    ativo = models.BooleanField("Ativo", default=True)
    
    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def delete(self, *args, **kwargs):
        self.deletado_em = timezone.now()
        self.save()
        
    def super_delete(self, *args, **kwargs):
        super(BaseModel, self).delete(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid4()
        super(BaseModel, self).save(*args, **kwargs)


class Post(BaseModel):
    titulo = models.CharField("Titulo", max_length=255)
    texto = models.TextField("Texto", blank=True, null=True)
    imagem = models.ImageField("Imagem", blank=True, null=True, upload_to='blog')
    usuario = models.ForeignKey(Usuario, related_name="usuario_post", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id} - {self.titulo}"
    
    @property
    def palavras(self):
        return len(self.texto.split(' '))