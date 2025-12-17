from .models import StudioSettings


def studio_settings(request):
    """Expose studio branding data to all templates."""
    settings_obj = StudioSettings.objects.first()
    return {
        "studio_settings": settings_obj,
    }
