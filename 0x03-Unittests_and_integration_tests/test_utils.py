#!/usr/bin/env python3
""""
Test utils
"""
import unittest
import requests
import utils
from unittest.mock import Mock, patch
from parameterized import parameterized


class TestGetJson(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mocked_get):
        """_summary_

        Args:
            mocked_request (_type_): _description_
        """
        mocked_response = Mock()
        mocked_response.json.return_value = test_payload
        mocked_get.return_value = mocked_response
        result = utils.get_json(test_url)
        self.assertEqual(result, test_payload)
        mocked_get.assert_called_with(test_url)
        mocked_get.assert_called_once_with(test_url)


if __name__ == '__main__':
    unittest.main()
