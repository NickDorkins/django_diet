from django.urls import path
from .views import DietListView, DietCreateView, DietUpdateView, DietDetailView, DietDeleteView

urlpatterns = [
    path('', DietListView.as_view(), name='diet_list'),
    path('<int:pk>/', DietDetailView.as_view(), name='diet_detail'),
    path('new/', DietCreateView.as_view(), name='diet_create'),
    path('<int:pk>/edit', DietUpdateView.as_view(), name='diet_update'),
    path('<int:pk>/delete', DietDeleteView.as_view(), name='diet_delete'),
]