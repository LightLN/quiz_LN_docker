from django.urls import path

from quiz.views import ExamDetailView
from quiz.views import ExamListView
from quiz.views import ExamResultCreateView
from quiz.views import ExamResultDeleteView
from quiz.views import ExamResultDetailView
from quiz.views import ExamResultQuestionView
from quiz.views import ExamResultUpdateView

app_name = 'quiz'

urlpatterns = [
    path('', ExamListView.as_view(), name='list'),
    path('<uuid:uuid>/', ExamDetailView.as_view(), name='details'),
    path('<uuid:uuid>/result/create/', ExamResultCreateView.as_view(), name='result_create'),
    path('<uuid:uuid>/result/<uuid:res_uuid>/details/', ExamResultDetailView.as_view(), name='result_details'),
    path('<uuid:uuid>/result/<uuid:res_uuid>/update/', ExamResultUpdateView.as_view(), name='result_update'),
    path('<uuid:uuid>/result/<uuid:res_uuid>/delete/', ExamResultDeleteView.as_view(), name='result_delete'),
    path('<uuid:uuid>/result/<uuid:res_uuid>/question/next/', ExamResultQuestionView.as_view(), name='question'),
]
