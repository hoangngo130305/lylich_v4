from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0005_add_custom_label_to_family_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='familymember',
            name='party_dang_bo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
