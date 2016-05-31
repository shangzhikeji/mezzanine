from django.apps import apps
from django.apps import AppConfig
from mezzanine.boot.utils import parse_extra_model_fields


class BootConfig(AppConfig):

    name = 'mezzanine.boot'

    def ready(self):
        from mezzanine.conf import settings
        fields = parse_extra_model_fields(settings.EXTRA_MODEL_FIELDS)

        for model_key, model_fields in fields.items():
            model_class = apps.get_model(*model_key)
            for field_name, field in model_fields:
                print("Injecting %s into %s" % (field_name, model_class))
                model_class.add_to_class(field_name, field)
                for cls in [model_class] + model_class.__subclasses__():
                    cls._meta._expire_cache()
