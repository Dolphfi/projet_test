from rest_framework import serializers
from .models import Client, Compte, Placement, Mutuelle, Sol

# Sérialiseur pour Client
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

# Sérialiseur pour Compte
class CompteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compte
        fields = '__all__'

# Sérialiseur pour Placement
class PlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        fields = '__all__'

# Sérialiseur pour Mutuelle
class MutuelleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mutuelle
        fields = '__all__'

# Sérialiseur pour Sol
class SolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sol
        fields = '__all__'
