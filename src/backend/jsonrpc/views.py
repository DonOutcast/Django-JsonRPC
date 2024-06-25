import json
from typing import Dict, Any

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from jsonrpc.commands import verify_jsonrpc_method


class JsonRpcView(View):

    template_name: str = 'jsonrpc_ui/index.html'

    def get(self, request, *args, **kwargs) -> render:
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs) -> JsonResponse:
        method: str = request.POST.get('method', '')
        params: str = request.POST.get('params', '{}')

        try:
            params_dict: Dict[str, Any] = json.loads(params)
        except json.JSONDecodeError:
            params_dict: Dict[str, Any] = {}

        response: Dict[str, Any] = verify_jsonrpc_method(method, params_dict)

        return JsonResponse(response)

