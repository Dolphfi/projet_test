from django.urls import path
from .views import ClientView, ClientCreateView, CompteView, PlacementView, MutuelleView, SolView, CompteCreateView, ClientListView

urlpatterns = [
    path('client/', ClientCreateView.as_view(), name='client-create'),  # Créer un client
    path('client/<str:telephone>/', ClientView.as_view(), name='client-detail'),  # Récupérer un client par téléphone
    path('clients/', ClientListView.as_view(), name='client-list'),  # Afficher tous les clients
    path('compte/<uuid:client_id>/', CompteView.as_view(), name='compte-list'),  # Récupérer les comptes d'un client
    path('compte/create/<uuid:client_id>/', CompteCreateView.as_view(), name='compte-create'),  # Créer un compte pour un client
    path('placement/<uuid:compte_id>/', PlacementView.as_view(), name='placement-detail'),  # Récupérer un placement
    path('mutuelle/<uuid:compte_id>/', MutuelleView.as_view(), name='mutuelle-detail'),  # Récupérer une mutuelle
    path('sol/<uuid:compte_id>/', SolView.as_view(), name='sol-detail'),  # Récupérer un sol

]
