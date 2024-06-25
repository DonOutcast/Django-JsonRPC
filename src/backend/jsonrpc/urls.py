from django.urls import path

from jsonrpc.views import JsonRpcView

urlpatterns = [
    path('', JsonRpcView.as_view(), name='jsonrpc_view')
]
