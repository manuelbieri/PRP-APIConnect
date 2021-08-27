import urllib.request
import urllib.parse
import json
from typing import Dict, List


class PRPConnector:
    def __init__(self, username: str, password: str, base_url: str):
        self.base_url: str = base_url
        self.base_path: str = 'api/v1/'
        self.url = self.base_url + self.base_path
        self.header: Dict[str, str] = self.login(username, password)

    def login(self, username: str, password: str) -> Dict[str, str]:
        """
        Login for session with the api.

        :param username: of the current user.<br>
        :param password: of the current user.<br>
        :return: auth-token ({'Authorization': Bearer token'})
        """
        assert username is not None
        assert password is not None
        request = urllib.request.Request(f"""{self.url}login?username={username}&password={password}""", method='POST')
        response = urllib.request.urlopen(request)
        token: str = response.read().decode('utf-8')[1:-2]
        return {'Authorization': f"""Bearer {token}"""}

    def test_message(self) -> Dict[str, str]:
        """
        Tests whether a connection to the api can be established.
        """
        return self._get_response('')

    def get_all(self, api_part: str) -> List[dict]:
        """
        Returns all items of the user in the specified part of the api.

        :param api_part: to specify by the client.<br>
        :return: all items of the user in the specified part of the api.
        """
        api_url: str = api_part + '/index'
        return self._get_response(api_url)

    def get_user(self) -> int:
        """
        Returns the id of the user.

        :return: id of the user.
        """
        return self._get_response('user')

    def _get_response(self, api_url: str):
        """
        Gets a response according to the supplied url.

        :param api_url: to get a response for.<br>
        :return: response of the api for the specified url.
        """
        request = self._request_builder(api_url)
        response = urllib.request.urlopen(request)
        return self._parse_response(response)

    @staticmethod
    def _parse_response(response):
        """
        Parses a response from a string to json.

        :param response: string to parse.<br>
        :return: parsed json.
        """
        raw_data = response.read().decode()
        data_json = json.loads(raw_data)
        return data_json

    def _request_builder(self, api_url: str, method: str = 'GET') -> urllib.request.Request:
        """
        Builds a request out of a url and a method.

        :param api_url: for the request to the api.<br>
        :param method: for the request.<br>
        :return: complete request for the api.
        """
        url: str = self.url + api_url
        return urllib.request.Request(url, headers=self.header, method=method)

    def write_item(self, api_part: str, write_query: str) -> dict:
        """
        Write an item into the database over the api.

        :param api_part: part of the database to manipulate.<br>
        :param write_query: consisting of the necessary information for a new entry.<br>
        :return: status information.
        """
        assert api_part is not None
        assert write_query is not None
        write_query = write_query.replace(' ', '%20')
        request: urllib.request.Request = self._request_builder(api_part + '?' + write_query, method='POST')
        response = urllib.request.urlopen(request)
        return self._parse_response(response)

    def delete_item(self, api_part: str, delete_id: int) -> dict:
        """
        Delete an item in the database over the api.

        :param api_part: part of the database to manipulate.<br>
        :param delete_id: of the item to delete.<br>
        :return: status information.
        """
        assert api_part is not None
        assert delete_id > 0
        request: urllib.request.Request = self._request_builder(api_part + '?id=' + str(delete_id), method='DELETE')
        response = urllib.request.urlopen(request)
        return self._parse_response(response)

    def get_item(self, api_part: str, key: str, value: str) -> List[dict]:
        """
        Get items from the database over the api.

        :param api_part: part of the database to search in.<br>
        :param key: the column in the database to search in.<br>
        :param value: the value the column in the database has to satisfy.<br>
        :return: list of all entries satisfying the input key-value specifications.
        """
        assert api_part is not None
        assert key is not None
        assert value is not None
        api_url: str = api_part + '?key=' + key + '&value=' + value
        request: urllib.request.Request = self._request_builder(api_url)
        response = urllib.request.urlopen(request)
        return self._parse_response(response)

    def update_item(self, api_part: str, update_query: str) -> dict:
        """
        Updates an item in the database over the api.

        :param api_part: part of the database to manipulate.<br>
        :param update_query: consisting of the necessary information to update an entry.<br>
        :return: status information.
        """
        assert api_part is not None
        assert update_query is not None
        update_query = update_query.replace(' ', '%20')
        api_url: str = api_part + '?' + update_query
        request: urllib.request.Request = self._request_builder(api_url, method='PUT')
        response = urllib.request.urlopen(request)
        return self._parse_response(response)


class ToDoConnector(PRPConnector):
    def __init__(self, username: str, password: str, base_url: str) -> None:
        super().__init__(username, password, base_url)
        self.api_part = 'todo'

    def get_all_todo(self) -> List[dict]:
        return self.get_all(self.api_part)

    def get_item_todo(self, key: str, value: str) -> List[dict]:
        assert key in ['id', 'title', 'description']
        assert value is not None
        return self.get_item(self.api_part, key, value)

    def write_item_todo(self, title: str, description: str) -> dict:
        assert title is not None
        assert description is not None
        query: str = f'title={title}&description={description}'
        return self.write_item(self.api_part, query)

    def delete_item_todo(self, delete_id: int) -> dict:
        assert delete_id > 0
        return self.delete_item(self.api_part, delete_id)

    def update_item_todo(self, item_id: int, title: str, description: str) -> dict:
        assert item_id > 0
        assert title is not None
        assert description is not None
        query: str = f'id={str(item_id)}&title={title}&description={description}'
        return self.update_item(self.api_part, query)
