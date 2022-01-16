from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from slugger import AutoSlugField

# Create your models here.
STATUS = (
    (0, 'Undone'),
    (1, 'Done')
)

TAGS = (
    ('priority', 'Priority'),
    ('home', 'Home'),
    ('work', 'Work'),
    ('family', 'Family'),
    ('leisure', 'Leisure')
)

class ReminderModel(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = AutoSlugField(populate_from='title')
    reminder = models.TextField()
    set_for = models.DateTimeField(auto_now_add=False)
    tag = models.CharField(max_length=50, choices=TAGS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.title


