from django.db import models

# Create your models here.

# sign up user account


# class signup(models.Model):
#     firstName = models.CharField(max_length=50)
#     lastName = models.CharField(max_length=50)
#     img = models.ImageField(upload_to="pics")
#     email = models.EmailField()
#     password = models.CharField(max_length=50)

#     def __str__(self):
#         return self.firstName

# # Time Table


# class TimeTable(models.Model):
#     day = models.CharField(max_length=50)
#     period1 = models.CharField(max_length=50)
#     period2 = models.CharField(max_length=50)
#     period3 = models.CharField(max_length=50)
#     period4 = models.CharField(max_length=50)
#     period5 = models.CharField(max_length=50)

#     def __str__(self):
#         return self.day

# # Student Class


# class StudentClass(models.Model):
#     className = models.CharField(max_length=50)
#     classNum = models.CharField(max_length=50)
#     classSec = models.CharField(max_length=50)

#     def __str__(self):
#         return self.className
