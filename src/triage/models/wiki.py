import logging
import uuid

from django.db import models

from triage.models import BaseTimestampedModel, BaseUserTrackedModel, WorkItemState

logger = logging.getLogger(__name__)


class WikiArticleRevision(BaseTimestampedModel, BaseUserTrackedModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    article = models.ForeignKey("WikiArticle", on_delete=models.CASCADE, related_name="revisions")
    title = models.CharField(max_length=1024)
    content = models.TextField(null=True, blank=True)
    state = models.CharField(
        max_length=2, choices=WorkItemState.choices, default=WorkItemState.ACTIVE
    )
    change_comment = models.CharField(max_length=512, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.article.current = self
        self.article.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/wiki/{self.article.slug}/{self.uuid}"

    def get_absolute_edit_url(self):
        return f"/wiki/{self.article.slug}/{self.uuid}/edit"


class WikiArticle(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    slug = models.SlugField(unique=True)
    current = models.ForeignKey(
        WikiArticleRevision, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        if self.current:
            return self.current.title
        else:
            return "(No article)"

    def get_absolute_url(self):
        return f"/wiki/{self.slug}"

    def get_absolute_edit_url(self):
        return f"/wiki/{self.slug}/edit"

    @property
    def versions(self):
        return WikiArticleRevision.objects.filter(article=self).order_by("-created_at")
