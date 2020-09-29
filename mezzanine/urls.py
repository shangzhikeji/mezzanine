"""
This is the main ``urlconf`` for Mezzanine - it sets up patterns for
all the various Mezzanine apps, third-party apps like Grappelli and
filebrowser.
"""

from __future__ import unicode_literals
from future.builtins import str

from django.conf.urls import include, url
from django.contrib.sitemaps.views import sitemap
from django.views.i18n import JavaScriptCatalog
from django.http import HttpResponse

from mezzanine.conf import settings
from mezzanine.core.sitemaps import DisplayableSitemap
from django.contrib.sitemaps import Sitemap

urlpatterns = []

# JavaScript localization feature
js_info_dict = {'domain': 'django'}
urlpatterns += [
    url(r'^jsi18n/(?P<packages>\S+?)/$', JavaScriptCatalog.as_view(),
        js_info_dict),
]

if settings.DEBUG and "debug_toolbar" in settings.INSTALLED_APPS:
    try:
        import debug_toolbar
    except ImportError:
        pass
    else:
        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]

# Django's sitemap app.
if "django.contrib.sitemaps" in settings.INSTALLED_APPS:

    # pageNo = 0
    # while(pageNo < 100):
    #     ds = DisplayableSitemap(pageNo)
    #     #ds.set_page(pageNo)
    #     sitemaps = {"sitemaps": {"all": DisplayableSitemap(pageNo)}}
    #     urlpatterns += [
    #         url(r"^sitemap-(?P<pageNo>\d+).xml",sitemap, sitemaps),
    #     ]
    #     pageNo = pageNo + 1
    urlpatterns += [
        url(r"^sitemap-0.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(0)}}),
        url(r"^sitemap-1.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(1)}}),
        url(r"^sitemap-2.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(2)}}),
        url(r"^sitemap-3.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(3)}}),
        url(r"^sitemap-4.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(4)}}),
        url(r"^sitemap-5.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(5)}}),
        url(r"^sitemap-6.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(6)}}),
        url(r"^sitemap-7.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(7)}}),
        url(r"^sitemap-8.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(8)}}),
        url(r"^sitemap-9.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(9)}}),
        url(r"^sitemap-10.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(10)}}),
        url(r"^sitemap-11.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(11)}}),
        url(r"^sitemap-12.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(12)}}),
        url(r"^sitemap-13.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(13)}}),
        url(r"^sitemap-14.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(14)}}),
        url(r"^sitemap-15.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(15)}}),
        url(r"^sitemap-16.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(16)}}),
        url(r"^sitemap-17.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(17)}}),
        url(r"^sitemap-18.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(18)}}),
        url(r"^sitemap-19.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(19)}}),
        url(r"^sitemap-20.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(20)}}),
        url(r"^sitemap-21.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(21)}}),
        url(r"^sitemap-22.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(22)}}),
        url(r"^sitemap-23.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(23)}}),
        url(r"^sitemap-24.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(24)}}),
        url(r"^sitemap-25.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(25)}}),
        url(r"^sitemap-26.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(26)}}),
        url(r"^sitemap-27.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(27)}}),
        url(r"^sitemap-28.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(28)}}),
        url(r"^sitemap-29.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(29)}}),
        url(r"^sitemap-30.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(30)}}),
        url(r"^sitemap-31.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(31)}}),
        url(r"^sitemap-32.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(32)}}),
        url(r"^sitemap-33.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(33)}}),
        url(r"^sitemap-34.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(34)}}),
        url(r"^sitemap-35.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(35)}}),
        url(r"^sitemap-36.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(36)}}),
        url(r"^sitemap-37.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(37)}}),
        url(r"^sitemap-38.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(38)}}),
        url(r"^sitemap-39.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(39)}}),
        url(r"^sitemap-40.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(40)}}),
        url(r"^sitemap-41.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(41)}}),
        url(r"^sitemap-42.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(42)}}),
        url(r"^sitemap-43.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(43)}}),
        url(r"^sitemap-44.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(44)}}),
        url(r"^sitemap-45.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(45)}}),
        url(r"^sitemap-46.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(46)}}),
        url(r"^sitemap-47.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(47)}}),
        url(r"^sitemap-48.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(48)}}),
        url(r"^sitemap-49.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(49)}}),
        url(r"^sitemap-50.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(50)}}),
        url(r"^sitemap-51.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(51)}}),
        url(r"^sitemap-52.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(52)}}),
        url(r"^sitemap-53.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(53)}}),
        url(r"^sitemap-54.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(54)}}),
        url(r"^sitemap-55.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(55)}}),
        url(r"^sitemap-56.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(56)}}),
        url(r"^sitemap-57.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(57)}}),
        url(r"^sitemap-58.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(58)}}),
        url(r"^sitemap-59.xml", sitemap,
            {"sitemaps": {"all": DisplayableSitemap(59)}}),
    ]
# Return a robots.txt that disallows all spiders when DEBUG is True.
if getattr(settings, "DEBUG", False):
    urlpatterns += [
        url(r"^robots\.txt$",
            lambda r: HttpResponse("User-agent: *\nDisallow: /",
                                   content_type="text/plain")),
    ]

# Miscellanous Mezzanine patterns.
urlpatterns += [
    url(r"^", include("mezzanine.core.urls")),
    url(r"^", include("mezzanine.generic.urls")),
]

# Mezzanine's Accounts app
if "mezzanine.accounts" in settings.INSTALLED_APPS:
    # We don't define a URL prefix here such as /account/ since we want
    # to honour the LOGIN_* settings, which Django has prefixed with
    # /account/ by default. So those settings are used in accounts.urls
    urlpatterns += [
        url(r"^", include("mezzanine.accounts.urls")),
    ]

# Mezzanine's Blog app.
blog_installed="mezzanine.blog" in settings.INSTALLED_APPS
if blog_installed:
    BLOG_SLUG=settings.BLOG_SLUG.rstrip("/")
    if BLOG_SLUG:
        BLOG_SLUG += "/"
    blog_patterns=[
        url(r"^%s" % BLOG_SLUG, include("mezzanine.blog.urls")),
    ]
    urlpatterns += blog_patterns

# Mezzanine's Pages app.
PAGES_SLUG=""
if "mezzanine.pages" in settings.INSTALLED_APPS:
    # No BLOG_SLUG means catch-all patterns belong to the blog,
    # so give pages their own prefix and inject them before the
    # blog urlpatterns.
    if blog_installed and not BLOG_SLUG.rstrip("/"):
        PAGES_SLUG=getattr(settings, "PAGES_SLUG", "pages").strip("/") + "/"
        blog_patterns_start=urlpatterns.index(blog_patterns[0])
        urlpatterns[blog_patterns_start:len(blog_patterns)]=[
            url(r"^%s" % str(PAGES_SLUG), include("mezzanine.pages.urls")),
        ]
    else:
        urlpatterns += [
            url(r"^", include("mezzanine.pages.urls")),
        ]
