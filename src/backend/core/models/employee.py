from django.db import models


class Employee(models.Model):
    """Model definition for Employee."""

    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        """Meta definition for Employee."""

        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.name
