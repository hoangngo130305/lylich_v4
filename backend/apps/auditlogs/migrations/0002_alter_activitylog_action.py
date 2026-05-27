from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditlogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitylog',
            name='action',
            field=models.CharField(max_length=50, choices=[
                ('create', 'Tạo mới'), ('update', 'Cập nhật'), ('delete', 'Xóa'),
                ('view', 'Xem'), ('export', 'Xuất'), ('login', 'Đăng nhập'),
                ('logout', 'Đăng xuất'), ('approve', 'Duyệt'), ('reject', 'Từ chối'),
                ('submit', 'Nộp'), ('send', 'Gửi'),
            ]),
        ),
    ]
