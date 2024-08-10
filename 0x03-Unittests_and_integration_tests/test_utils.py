#!/usr/bin/env python3
"""Testing utils for the core utils"""

import unittest
from unittest import mock

from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test the functionality of the mentioned function"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """test case for nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        """this shouldn't be legal"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """test that utils.get_json returns the expected result"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url, test_payload):
        """We don’t want to make any actual external HTTP calls"""
        with mock.patch("requests.get") as get:
            get.return_value.json.return_value = test_payload
            result = get_json(test_url)
            get.assert_called_once()
            get.assert_called_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """tests for utils.memoize decorator"""

    def test_memoize(self):
        """only called once using assert_called_once"""

        class TestClass:
            """Test class for memoize decorator"""

            def a_method(self):
                """just a simple method"""
                return 42

            @memoize
            def a_property(self):
                """get a property"""
                return self.a_method()

        with mock.patch.object(TestClass, "a_method") as method:
            method.return_value = 40
            obj = TestClass()
            self.assertEqual(obj.a_property, 40)
            self.assertEqual(obj.a_property, 40)
            method.assert_called_once()
