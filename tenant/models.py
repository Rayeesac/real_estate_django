from django.db import models
from property.models import Unit, Property
from django.contrib.auth.models import User

class AflUser(User):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    document_proofs = models.TextField()
    agreement_end_date = models.DateField()
    monthly_rent_date = models.DateField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tenant_images/', null=True, blank=True)
