from django.views.generic.base import TemplateView, RedirectView
from django.shortcuts import render, redirect
from django.urls import reverse

from . import models


class PageView(TemplateView):
    template_name = "pages/page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_type = self.request.path.replace("/", "")
        context["page"] = models.Page.objects.filter(page_type=page_type).first()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if context.get("page"):
            return self.render_to_response(context)
        else:
            return redirect("pages:not_found")


class PageRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return "/{}".format(models.HOME_TYPE)


class NotFoundView(TemplateView):
    template_name = "pages/404.html"
