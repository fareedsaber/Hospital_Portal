# Generated by Django 3.1.5 on 2021-05-22 02:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DepName', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='FollowUpFrequency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FUFName', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='MonitoringTool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SourceName', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=150)),
                ('Dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TaskMent.department')),
            ],
        ),
        migrations.CreateModel(
            name='TaskOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TOName', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='TaskSituation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SituationName', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(choices=[('Open', 'Open'), ('In_Progress', 'In_Progress'), ('Struggling', 'Struggling'), ('Complete', 'Complete')], max_length=150)),
                ('Task', models.CharField(max_length=150)),
                ('TaskDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('DueDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('Comment', models.TextField(blank=True, max_length=250, null=True)),
                ('DepName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TaskMent.department', verbose_name='Department')),
                ('FOF', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TaskMent.followupfrequency', verbose_name='FollowUpFrequency')),
                ('MonitoringTool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TaskMent.monitoringtool', verbose_name='MonitoringTool')),
                ('TaskOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TaskMent.taskowner', verbose_name='TaskOwner')),
                ('TaskSituation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TaskMent.tasksituation', verbose_name='TaskSituation')),
                ('sec', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TaskMent.section', verbose_name='section')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
