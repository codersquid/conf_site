from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

import symposion.views


WIKI_SLUG = r"(([\w-]{2,})(/[\w-]{2,})*)"


urlpatterns = patterns(
    "",
    url(r"^$", TemplateView.as_view(template_name="pydata-home/index.html"), name="index"),
    url(r"^testseattle2015/$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^testseattle2015/admin/", include(admin.site.urls)),

    url(r"^testseattle2015/account/signup/$", symposion.views.SignupView.as_view(), name="account_signup"),
    url(r"^testseattle2015/account/login/$", symposion.views.LoginView.as_view(), name="account_login"),
    url(r"^testseattle2015/account/", include("account.urls")),

    url(r"^testseattle2015/dashboard/", symposion.views.dashboard, name="dashboard"),
    url(r"^testseattle2015/speaker/", include("symposion.speakers.urls")),
    url(r"^testseattle2015/proposals/", include("symposion.proposals.urls")),
    url(r"^testseattle2015/sponsors/", include("symposion.sponsorship.urls")),
    url(r"^testseattle2015/boxes/", include("symposion.boxes.urls")),
    url(r"^testseattle2015/teams/", include("symposion.teams.urls")),
    url(r"^testseattle2015/reviews/", include("symposion.reviews.urls")),
    url(r"^testseattle2015/schedule/", include("symposion.schedule.urls")),
    url(r"^testseattle2015/markitup/", include("markitup.urls")),

    url(r"^testseattle2015/", include("symposion.cms.urls")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
