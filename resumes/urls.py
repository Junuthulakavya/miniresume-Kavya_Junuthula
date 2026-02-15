from django.urls import path
from .views import HealthCheckView, ResumeCreateView, ResumeListView

urlpatterns = [
    path('health/', HealthCheckView.as_view(), name='health'),
    path('resumes/', ResumeCreateView.as_view(), name='create-resume'),
    path('resumes/list/', ResumeListView.as_view(), name='list-resumes'),
]
