import urllib.request
import urllib.parse
import json
from typing import Dict, List


class PRPConnector:
    def __init__(self, username: str, password: str):
        self.base_url: str = 'https://marblch.pythonanywhere.com/'
        self.base_path: str = 'api/v1/'
        self.url = self.base_url + self.base_path
        self.header: Dict[str, str] = self.login(username, password)

    def login(self, username: str, password: str) -> Dict[str, str]:
        request = urllib.request.Request(f"""{self.url}login?username={username}&password={password}""", method='POST')
        response = urllib.request.urlopen(request)
        token: str = response.read().decode('utf-8')[1:-2]
        return {'Authorization': f"""Bearer {token}"""}

    def test_message(self) -> Dict[str, str]:
        return self._get_response('')

    def get_all(self, api_part: str) -> List[dict]:
        api_url: str = api_part + '/index'
        return self._get_response(api_url)

    def get_user(self) -> int:
        return self._get_response('user')

    def _get_response(self, api_url: str):
        request = self._request_builder(api_url)
        response = urllib.request.urlopen(request)
        return self._parse_response(response)

    @staticmethod
    def _parse_response(response):
        raw_data = response.read().decode()
        data_json = json.loads(raw_data)
        return data_json

    def _request_builder(self, api_url: str, method: str = 'GET') -> urllib.request.Request:
        url: str = self.url + api_url
        return urllib.request.Request(url, headers=self.header, method=method)

    def write_item(self, api_part: str, write_query: str):
        assert api_part is not None
        assert write_query is not None
        write_query = write_query.replace(' ', '%20')
        request: urllib.request.Request = self._request_builder(api_part + '?' + write_query, method='POST')
        response = urllib.request.urlopen(request)
        return self._parse_response(response)

    def delete_item(self, api_part: str, delete_id: int):
        assert api_part is not None
        assert delete_id > 0
        request: urllib.request.Request = self._request_builder(api_part + '?id=' + str(delete_id), method='DELETE')
        response = urllib.request.urlopen(request)
        return self._parse_response(response)

    def get_item(self, api_part: str, key: str, value: str):
        assert api_part is not None
        assert key is not None
        assert value is not None
        api_url: str = api_part + '?key=' + key + '&value=' + value
        request: urllib.request.Request = self._request_builder(api_url)
        response = urllib.request.urlopen(request)
        return self._parse_response(response)
