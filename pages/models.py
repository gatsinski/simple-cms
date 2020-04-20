from django.db import models
from django.utils.translation import ugettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField


HOME_TYPE = "home"
ABOUT_TYPE = "about"
SERVICES_TYPE = "services"
CONTACT_TYPE = "contact"

PAGE_TYPE_CHOICES = (
    (HOME_TYPE, _("Home")),
    (ABOUT_TYPE, _("About")),
    (SERVICES_TYPE, _("Services")),
    (CONTACT_TYPE, _("Contact")),
)


class Page(models.Model):
    page_type = models.CharField(
        _("Type"), max_length=254, choices=PAGE_TYPE_CHOICES
    )
    title = models.CharField(_("Title"), max_length=254)
    slug = models.SlugField(_("Slug"), max_length=254, unique=True)
    description = models.CharField(_("Description"), max_length=1000, blank=True)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")

    def __str__(self):
        return self.title
