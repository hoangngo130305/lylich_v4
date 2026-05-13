import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='profile',
            field=models.ForeignKey(
                blank=True, null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='uploaded_files',
                to='profiles.profile',
            ),
        ),
        migrations.AddIndex(
            model_name='uploadedfile',
            index=models.Index(fields=['profile'], name='uploaded_fi_profile_b67583_idx'),
        ),
    ]
