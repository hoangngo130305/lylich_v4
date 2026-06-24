from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timelines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyentry',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
