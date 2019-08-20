from django.db import models

# Create your models here.

class Game(models.Model):
    """Games being reviewed."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
    

class Entry(models.Model):
    """Something specific about a game"""
    topic = models.ForeignKey(Game, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

class Meta:

    verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."


