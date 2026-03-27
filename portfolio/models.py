from django.db import models

# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=100)  # Allow custom name
    email = models.EmailField()
    content = models.TextField(max_length=500)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name