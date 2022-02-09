from django.urls import path
from .views import ChannelsView, SubscriptionByUser, SubscriptionDetails

urlpatterns = [
    path('', ChannelsView.as_view()),
    path('subscription', SubscriptionDetails.as_view()),
    path('subscription/user', SubscriptionByUser.as_view()),
]