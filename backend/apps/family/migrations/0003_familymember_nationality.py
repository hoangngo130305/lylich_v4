from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familymember',
            name='nationality',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
