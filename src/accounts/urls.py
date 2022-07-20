from accounts.views import AccountLoginView
from accounts.views import AccountLogoutView
from accounts.views import AccountRegisterView
from accounts.views import AccountUpdateProfileView
from accounts.views import account_profile_view
from accounts.views import user_activate

from django.urls import path
from django.views.generic import TemplateView

app_name = 'accounts'

urlpatterns = [
    path('registration/activate/<str:sign>/', user_activate, name='register_activate'),
    path('registration/done/', TemplateView.as_view(template_name='accounts/register_done.html'), name='register_done'),
    path('registration/', AccountRegisterView.as_view(), name='registration'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    path('profile/', account_profile_view, name='profile'),
    path('profile_change/', AccountUpdateProfileView.as_view(), name='profile_change'),
]
