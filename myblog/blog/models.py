from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):

    CATEGORY_CHOICES = [
        ('Python', 'Python'),
        ('Django', 'Django'),
        ('AI', 'AI'),
        ('Java', 'Java'),
        ('JavaScript', 'JavaScript'),
        ('C++', 'C++'),
        ('C#', 'C#'),
        ('PHP', 'PHP'),
        ('Ruby', 'Ruby'),
        ('Go', 'Go'),
        ('Swift', 'Swift'),
        ('Kotlin', 'Kotlin'),
        ('Rust', 'Rust'),
        ('TypeScript', 'TypeScript'),
        ('SQL', 'SQL'),
        ('HTML/CSS', 'HTML/CSS'),
        ('Other', 'Other'),

    ]

    title = models.CharField(max_length=100)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Python'
    )

    content = models.TextField()

    image = models.ImageField(
        upload_to='posts/',
        blank=True,
        null=True
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Comment(models.Model):

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.author.username

    likes = models.ManyToManyField(
    User,
    related_name='liked_posts',
    blank=True
)