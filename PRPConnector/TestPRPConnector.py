import unittest
from typing import List

import Connector


class PRPConnectorTest(unittest.TestCase):
    connection: Connector.PRPConnector = Connector.PRPConnector('admin', 'adminTest')

    def test_test_message(self):
        response: dict = PRPConnectorTest.connection.test_message()
        self.assertEqual({'message': 'success'}, response)

    def test_login(self):
        response: int = PRPConnectorTest.connection.get_user()
        self.assertEqual(1, response)

    def test_get_index(self):
        response: List[dict] = PRPConnectorTest.connection.get_all('todo')
        self.assertEqual(list, type(response))

    def test_write_delete(self):
        write_response = PRPConnectorTest.connection.write_item('todo', 'title=test&description=test description')
        self.assertEqual({'message': 'Entry added successfully', 'type': 'success'}, write_response)
        read_response_1: List[dict] = PRPConnectorTest.connection.get_item('todo', 'title', 'test')
        self.assertEqual('test', read_response_1[0]['title'])
        self.assertEqual('test description', read_response_1[0]['description'])
        item_id: int = int(read_response_1[0]['id'])
        delete_response = PRPConnectorTest.connection.delete_item('todo', item_id)
        self.assertEqual({'message': 'Entry deleted successfully', 'type': 'success'}, delete_response)
        read_response_2 = PRPConnectorTest.connection.get_item('todo', 'title', 'test')
        self.assertEqual([], read_response_2)
