from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0003_familymember_nationality'),
    ]

    operations = [
        migrations.AddField(
            model_name='familymember',
            name='religious_rank_text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
