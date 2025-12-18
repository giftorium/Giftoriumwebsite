from django.db import migrations


SLUG = "yalda-hafez-faal-capsule"
OLD_MEDIUM = "Scented merch + printed keepsakes"
NEW_MEDIUM = "Experience design + merch suite + interactive installation"
OLD_DESCRIPTION = (
    "A limited merch drop created for the CBC Yalda celebration. "
    "We translated the ritual of pulling a Hafez verse into a tactile retail "
    "moment, layering foil, night/day palettes, and keepsake packaging so "
    "guests leave with an artifact of the gathering."
)
NEW_DESCRIPTION = (
    "We partnered with CBC's Yalda Night team to storyboard the entire experience—"
    "from the spatial flow and tactile merch system to the companion landing page—"
    "while co-building the string-based interactive art that powered each guest's fāl."
)
OLD_OUTCOME = (
    "Sold out the full capsule in under two hours and extended the event "
    "storytelling through take-home pieces guests continue to photograph and share."
)
NEW_OUTCOME = (
    "Guests moved through a cohesive ritual that tied the installation, string instrument, "
    "collectible merch, and digital page together, giving CBC a reusable platform for future drops."
)


def update_portfolio_copy(apps, schema_editor):
    PortfolioItem = apps.get_model('experiences', 'PortfolioItem')
    PortfolioItem.objects.filter(slug=SLUG).update(
        medium=NEW_MEDIUM,
        description=NEW_DESCRIPTION,
        outcome=NEW_OUTCOME,
    )


def revert_portfolio_copy(apps, schema_editor):
    PortfolioItem = apps.get_model('experiences', 'PortfolioItem')
    PortfolioItem.objects.filter(slug=SLUG).update(
        medium=OLD_MEDIUM,
        description=OLD_DESCRIPTION,
        outcome=OLD_OUTCOME,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0009_alter_studiosettings_intro_and_more'),
    ]

    operations = [
        migrations.RunPython(update_portfolio_copy, revert_portfolio_copy),
    ]
