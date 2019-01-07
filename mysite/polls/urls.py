from django.urls import path
from . import views
from .views import PollsView,PollDetailView,ResultsView

app_name = 'polls'

urlpatterns = [
    path('', PollsView.as_view(), name='index'),
    path('<int:pk>/', PollDetailView.as_view(), name='detail'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]