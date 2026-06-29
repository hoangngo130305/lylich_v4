from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timelines', '0002_historyentry_description_blank'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyentry',
            name='is_deceased',
            field=models.BooleanField(default=False),
        ),
    ]
