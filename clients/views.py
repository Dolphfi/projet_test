from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Client, Compte, Placement, Mutuelle, Sol
from .serializers import ClientSerializer, CompteSerializer, PlacementSerializer, MutuelleSerializer, SolSerializer

# Vue pour récupérer un client par téléphone
class ClientView(APIView):
    def get(self, request, telephone):
        try:
            client = Client.objects.get(telephone=telephone)
            serializer = ClientSerializer(client)
            return Response(serializer.data)
        except Client.DoesNotExist:
            return Response({"error": "Client non trouvé"}, status=status.HTTP_404_NOT_FOUND)

# Vue pour créer un client
class ClientCreateView(APIView):
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vue pour afficher les comptes d'un client
class CompteView(APIView):
    def get(self, request, client_id):
        comptes = Compte.objects.filter(client__id=client_id)
        serializer = CompteSerializer(comptes, many=True)
        return Response(serializer.data)

# Vue pour créer un compte pour un client
class CompteCreateView(APIView):
    def post(self, request, client_id):
        # Associer le compte au client en utilisant l'ID du client
        data = request.data
        data['client'] = client_id  # Associer le client au compte
        serializer = CompteSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vue pour afficher un placement
class PlacementView(APIView):
    def get(self, request, compte_id):
        try:
            compte = Compte.objects.get(id=compte_id, type_compte='placement')
            placement = Placement.objects.get(compte=compte)
            serializer = PlacementSerializer(placement)
            return Response(serializer.data)
        except (Compte.DoesNotExist, Placement.DoesNotExist):
            return Response({"error": "Placement non trouvé"}, status=status.HTTP_404_NOT_FOUND)

# Vue pour afficher une mutuelle
class MutuelleView(APIView):
    def get(self, request, compte_id):
        try:
            compte = Compte.objects.get(id=compte_id, type_compte='mutuelle')
            mutuelle = Mutuelle.objects.get(compte=compte)
            serializer = MutuelleSerializer(mutuelle)
            return Response(serializer.data)
        except (Compte.DoesNotExist, Mutuelle.DoesNotExist):
            return Response({"error": "Mutuelle non trouvée"}, status=status.HTTP_404_NOT_FOUND)

# Vue pour afficher un sol
class SolView(APIView):
    def get(self, request, compte_id):
        try:
            compte = Compte.objects.get(id=compte_id, type_compte='sol')
            sol = Sol.objects.get(compte=compte)
            serializer = SolSerializer(sol)
            return Response(serializer.data)
        except (Compte.DoesNotExist, Sol.DoesNotExist):
            return Response({"error": "Sol non trouvé"}, status=status.HTTP_404_NOT_FOUND)
        
# Vue pour récupérer tous les clients
class ClientListView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer