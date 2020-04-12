from django.db import models

# Create your models here.
class log(models.Model):
    studentcode = models.TextField()
    adminno = models.TextField()
    studentname = models.TextField()
    classname = models.TextField()
    section = models.TextField()
    dob = models.TextField()
    result = models.TextField()

    def __str__(self):
        return self.studentname
