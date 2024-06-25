import json
import tempfile
from typing import Optional, Dict, Any

from django.conf import settings

import requests


def verify_jsonrpc_method(method: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    headers: Dict[str, str] = {'Content-Type': 'application/json'}
    payload: Dict[str, Any] = {
        'jsonrpc': '2.0',
        'method': method,
        'params': params or {},
        'id': 1
    }

    try:
        with tempfile.NamedTemporaryFile(delete=False) as cert_file, \
                tempfile.NamedTemporaryFile(delete=False) as key_file:

            cert_file.write(settings.CLIENT_CERT.encode('utf-8'))
            key_file.write(settings.CLIENT_KEY.encode('utf-8'))
            cert_file.flush()
            key_file.flush()
            response: requests.Response = requests.post(
                settings.TEST_API,
                headers=headers,
                data=json.dumps(payload),
                cert=(cert_file.name, key_file.name),
                verify=True
            )
            response.raise_for_status()

            json_response: Dict[str, Any] = response.json()
            if 'error' in json_response:
                return json_response

            return json_response
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}
