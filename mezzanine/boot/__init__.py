"""
An app that is forced to the top of the list in ``INSTALLED_APPS``
for the purpose of hooking into Django's ``class_prepared`` signal
and adding custom fields as defined by the ``EXTRA_MODEL_FIELDS``
setting. Also patches ``django.contrib.admin.site`` to use
``LazyAdminSite`` that defers certains register/unregister calls
until ``admin.autodiscover`` to avoid some timing issues around
custom fields not being available when custom admin classes are
registered.
"""
from __future__ import unicode_literals

from django.contrib import admin
from mezzanine.boot.lazy_admin import LazyAdminSite


default_app_config = 'mezzanine.boot.apps.BootConfig'

# Override django.contrib.admin.site with LazyAdminSite. It must
# be bound to a separate name (admin_site) for access in autodiscover
# below.

admin_site = LazyAdminSite()
admin.site = admin_site
django_autodiscover = admin.autodiscover


def autodiscover(*args, **kwargs):
    """
    Replaces django's original autodiscover to add a call to
    LazyAdminSite's lazy_registration.
    """
    django_autodiscover(*args, **kwargs)
    admin_site.lazy_registration()

admin.autodiscover = autodiscover
