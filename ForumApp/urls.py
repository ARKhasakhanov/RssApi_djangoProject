from django.urls import path

from ForumApp.views import MessageItemList, MessageItemDetail, SectionItemList, SectionItemDetail, ThreadItemList, ThreadItemDetail, UserItemList, UserItemDetail

urlpatterns = ((
    path('message/', MessageItemList.as_view()),
    path('message/<int:pk>', MessageItemDetail.as_view()),
    path('section/', SectionItemList.as_view()),
    path('section/<int:pk>', SectionItemDetail.as_view()),
    path('thread/', ThreadItemList.as_view()),
    path('thread/<int:pk>', ThreadItemDetail.as_view()),
    path('user/', UserItemList.as_view()),
    path('user/<int:pk>', UserItemDetail.as_view()),
), 'rss_api')
