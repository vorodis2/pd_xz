from django.urls import path


from .views import GroupViewSet, GroupFileViewSet, GroupSortViewSet, GroupSmallViewSet,GroupCommentViewSet, get_last_change_time


APP_NAME = 'group'
# app_name = APP_NAME  # Django parses it by default

# передастник 
urlpatterns = [
    path('last_change/', get_last_change_time),

    path('me/', GroupViewSet.as_view({
        'get': 'list_me',
    }), name=f'{APP_NAME}_list_me'),

    path('', GroupViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name=f'{APP_NAME}_list'),

    path('<int:pk>/', GroupViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name=f'{APP_NAME}_detail'),

    path('export/', GroupViewSet.as_view({
        'get': 'export',
    }), name=f'{APP_NAME}_export'),

    path('files/', GroupFileViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='files_list'),

    path('files/<int:pk>/', GroupFileViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='files_detail'),


    path('sorts/', GroupSortViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='sorts_list'),

    path('sorts/<int:pk>/', GroupSortViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    }), name='sorts_detail'),


    path('littel/', GroupSmallViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name=f'{APP_NAME}_littel'),



    path('comment/', GroupCommentViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name=f'{APP_NAME}_list'),  

    path('comment/<int:pk>/', GroupCommentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name=f'{APP_NAME}_detail'),
]
