from django.db.models import QuerySet, Manager
from django.utils import timezone

class DeleteQuerySet(QuerySet):
    def delete(self):
        for obj in self:
            obj.deleted_at = timezone.now()
            obj.save()
            
class DeleteManager(Manager):
    def get_queryset(self):
        return DeleteQuerySet(self.model, using=self._db).filter(
            deleted_at__isnull=True
        )
            
        