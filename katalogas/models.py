from django.db import models
class Preke(models.Model):
    KATEGORIJOS = [
        ('ELE', 'Elektronika'),
        ('APR', 'Apranga'),
        ('MAI', 'Maistas'),
        ('KIT', 'Kita'),
    ]
    pavadinimas = models.CharField(max_length=100)
    aprasymas = models.TextField()
    kaina = models.DecimalField(max_digits=10, decimal_places=2)
    kategorija = models.CharField(max_length=3, choices=KATEGORIJOS)

    def __str__(self):
        return self.pavadinimas