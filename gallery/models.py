from django.db import models

class Gallery(models.Model):
    CATEGORY_CHOICES = [
        ('educational', 'Educational'),
        ('development', 'Development'),
        ('economic', 'Economic'),
        ('meetings', 'Meetings'),
        ('events', 'Events'),
    ]

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='events')

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)  # Allow marking news as featured

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)  # Optional event time
    location = models.CharField(max_length=255, blank=True, null=True)  # Add event location
    image = models.ImageField(upload_to='events/', blank=True, null=True)  # Optional image

    def __str__(self):
        return f"{self.title} on {self.date}"

class Issue(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
