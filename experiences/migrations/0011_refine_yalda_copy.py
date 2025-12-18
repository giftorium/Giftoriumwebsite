from django.db import migrations


SLUG = "yalda-hafez-faal-capsule"
OLD_MEDIUM = "Experience design + merch suite + interactive installation"
NEW_MEDIUM = "Experience masterplan + interactive installation + digital companion"
OLD_DESCRIPTION = (
    "We partnered with CBC's Yalda Night team to storyboard the entire experience—"
    "from the spatial flow and tactile merch system to the companion landing page—"
    "while co-building the string-based interactive art that powered each guest's fāl."
)
NEW_DESCRIPTION = (
    "We partnered with CBC's Yalda Night team to choreograph the full guest journey—"
    "from spatial flow and operations to the responsive landing page—"
    "while co-building the string-based interactive art anchoring each fāl."
)
OLD_OUTCOME = (
    "Guests moved through a cohesive ritual that tied the installation, string instrument, "
    "collectible merch, and digital page together, giving CBC a reusable platform for future drops."
)
NEW_OUTCOME = (
    "The integrated environment, instrument, and digital follow-up kept the ritual cohesive and gave CBC "
    "a reusable framework for future cultural nights."
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
        ('experiences', '0010_update_yalda_copy'),
    ]

    operations = [
        migrations.RunPython(update_portfolio_copy, revert_portfolio_copy),
    ]
