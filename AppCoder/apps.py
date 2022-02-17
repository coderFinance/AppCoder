from django.apps import AppConfig


class AppcoderConfig(AppConfig):
    name = 'AppCoder'

    def ready(self):
        import AppCoder.signals

