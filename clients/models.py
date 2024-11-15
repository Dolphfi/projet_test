from django.db import models
import uuid

# Modèle Client
class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.nom

# Modèle Compte (général pour Sol, Placement, Mutuelle)
class Compte(models.Model):
    TYPE_CHOICES = [
        ('sol', 'Sol'),
        ('placement', 'Placement'),
        ('mutuelle', 'Mutuelle'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero = models.CharField(max_length=50, unique=True)  # Numéro de compte unique
    type_compte = models.CharField(max_length=10, choices=TYPE_CHOICES)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Balance, initialisée à 0
    client = models.ForeignKey(Client, related_name='comptes', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type_compte.capitalize()} - {self.numero}"

# Modèle Placement (lié à un compte spécifique de type 'placement')
class Placement(models.Model):
    compte = models.OneToOneField(Compte, on_delete=models.CASCADE, limit_choices_to={'type_compte': 'placement'})
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    taux_interet = models.DecimalField(max_digits=5, decimal_places=2)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return f"Placement {self.compte.numero} - {self.montant}€"

# Modèle Mutuelle (lié à un compte spécifique de type 'mutuelle')
class Mutuelle(models.Model):
    compte = models.OneToOneField(Compte, on_delete=models.CASCADE, limit_choices_to={'type_compte': 'mutuelle'})
    montant_contribution = models.DecimalField(max_digits=10, decimal_places=2)
    date_adhesion = models.DateField()

    def __str__(self):
        return f"Mutuelle {self.compte.numero} - {self.montant_contribution}€"

# Modèle Sol (lié à un compte spécifique de type 'sol')
class Sol(models.Model):
    compte = models.OneToOneField(Compte, on_delete=models.CASCADE, limit_choices_to={'type_compte': 'sol'})
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    type_sol = models.CharField(max_length=50)

    def __str__(self):
        return f"Sol {self.compte.numero} - {self.montant}€"
