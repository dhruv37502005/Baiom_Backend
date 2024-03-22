# Generated by Django 4.2 on 2024-03-20 06:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Batch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("batch_name", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("program_overview", models.TextField(blank=True, null=True)),
                ("instructor", models.CharField(max_length=50)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="course_images/"
                    ),
                ),
                (
                    "video",
                    models.FileField(blank=True, null=True, upload_to="course_videos/"),
                ),
                ("price", models.FloatField(blank=True, null=True)),
                (
                    "discount",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("slug", models.SlugField(blank=True, unique=True)),
                ("duration_field", models.DurationField(default=datetime.timedelta)),
                ("watch_percent", models.FloatField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "Active"),
                            ("inactive", "Inactive"),
                            ("draft", "Draft"),
                        ],
                        default="draft",
                        max_length=10,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="CourseCarriculum",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("carriculum_title", models.CharField(default=False, max_length=100)),
                ("carriculum_desc", models.TextField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="CourseCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                ("file", models.FileField(null=True, upload_to="media/file/")),
            ],
        ),
        migrations.CreateModel(
            name="Testimonial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("role", models.CharField(max_length=255)),
                ("content", models.TextField()),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="CourseTestimonial_images/"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="testimonials",
                        to="course.coursecategory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Resource",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "notes",
                    models.FileField(blank=True, null=True, upload_to="course_notes/"),
                ),
                (
                    "recorded_video_link",
                    models.FileField(
                        blank=True, null=True, upload_to="course_recorded_lectures/"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "batch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="course.batch"
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="course.course"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="course",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="course.coursecategory"
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="curriculum",
            field=models.ManyToManyField(
                blank=True, related_name="carriculum", to="course.coursecarriculum"
            ),
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("mobile", models.CharField(max_length=20)),
                ("profession", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "course_category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course.coursecategory",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="batch",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="course.course"
            ),
        ),
    ]
