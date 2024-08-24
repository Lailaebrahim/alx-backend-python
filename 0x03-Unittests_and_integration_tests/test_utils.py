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
        """
        Test get_json
        
        Args:
            test_url (str): url
            test_payload (dict): payload
            mocked_get (Mock): mocked get
        """
        # create response mock object
        mocked_response = Mock()
        # assign json return value to the response mock object
        mocked_response.json.return_value = test_payload
        # assign the response mock object to the get method
        mocked_get.return_value = mocked_response
        # call the get_json method with the test_url
        result = utils.get_json(test_url)
        # assert the result is equal to the test_payload
        self.assertEqual(result, test_payload)
        # assert the get method was called with the test_url
        mocked_get.assert_called_with(test_url)
        # assert the get method was called once
        mocked_get.assert_called_once_with(test_url)


if __name__ == '__main__':
    unittest.main()
