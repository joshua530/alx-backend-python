#!/usr/bin/env python3
"""Unittest for utils.access_nested_map"""

import unittest
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json, memoize

from parameterized import parameterized

""" Parameterized tests allow a developer to run the same test over
and over again using different values. """


class TestAccessNestedMap(unittest.TestCase):
    """tests the function access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_value):
        """tests access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected_value)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Uses the assertRaises context manager
        to assert that a KeyError is raised.
        """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """tests get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Tests:
        1. that the mocked get method was called exactly once
        (per input) with test_url as argument.
        2. that the output of get_json is equal to test_payload.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """tests memoize function"""

    def test_memoise(self):
        """
        Test that when calling a_property twice:
        1. the correct result is returned
        2. a_method is only called once.
        """

        class TestClass:

            @memoize
            def a_property(self):
                return self.a_method()

            def a_method(self):
                return 42

        with patch.object(TestClass, 'a_method') as mocked:
            test = TestClass()
            test.a_property
            test.a_property
            mocked.asset_called_once()


if __name__ == '__main__':
    unittest.main()
