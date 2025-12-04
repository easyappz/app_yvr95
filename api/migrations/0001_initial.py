from django.db import migrations, models
import api.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields([
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('about_me', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', api.models.MemberManager()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields([
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=models.CASCADE, to='api.member')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields([
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=models.CASCADE, to='api.member')),
                ('post', models.ForeignKey(on_delete=models.CASCADE, to='api.post')),
            ],
            options={
                'unique_together': (('user', 'post'),),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields([
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=models.CASCADE, to='api.member')),
                ('post', models.ForeignKey(on_delete=models.CASCADE, to='api.post')),
            ],
        ),
    ]
