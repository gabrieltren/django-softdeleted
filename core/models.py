from django.db import models
import uuid
from django.utils import timezone

from .softdelete import DeleteManager

# from django.contrib.auth.models import User
from contas.models import Usuario

class BaseModel(models.Model):
    class Meta:
        abstract = True
        
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField("Criado em",auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado_em", auto_now=True)
    deleted_at = models.DateTimeField("Deletado em", null=True, blank=True)
    
    objects = DeleteManager()
    all_objects = models.Manager()
    
    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid4()
        super(BaseModel, self).save(*args, **kwargs)
        
    def delete(self, *args, **kwargs):
        self.deleted_at = timezone.now()
        self.save()
        
    def super_delete(self, *args, **kwargs):
        super(BaseModel, self).delete(*args, **kwargs)
    


class Movimentacao(BaseModel):
    TIPO_MOVIMENTACAO = (
        ('entrada', 'Entrada'),
        ('saida', 'Saida')
    )
    valor = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    data = models.DateTimeField(blank=True, null=True)
    tipo = models.CharField(max_length=100, choices=TIPO_MOVIMENTACAO, default="entrada")
    usuario = models.ForeignKey(Usuario, related_name="usuario_movimentacao", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Movimentação"
        verbose_name_plural = "Movimentações"
        ordering = ['-data']