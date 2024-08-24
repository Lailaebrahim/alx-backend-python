#!/usr/bin/env python3
""""
Test utils
"""
import unittest
import requests
import utils
from unittest.mock import Mock, patch


class TestGetJson(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    @patch('requests.get')
    def test_get_json(self, mocked_request):
        """_summary_

        Args:
            mocked_request (_type_): _description_
        """
        mocked_url = "http://test.com"
        mocked_response = Mock()
        mocked_response.json.return_value = {"payload": True}
        mocked_request.return_value = mocked_response
        self.assertEqual(
            utils.get_json(mocked_url).get("payload"), True)
        mocked_request.assert_called_with(mocked_url)
            

if __name__ == '__main__':
    unittest.main()
    