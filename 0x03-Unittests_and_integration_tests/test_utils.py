#!/usr/bin/env python3
"""Testing utils for the core utils"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test the functionality of the mentioned function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test case for nested map"""
        assert access_nested_map(nested_map, path) == expected

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """this shouldn't be legal"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """test that utils.get_json returns the expected result"""

    def test_get_json(self):
        """We don’t want to make any actual external HTTP calls"""
        pass


class TestMemoize(unittest.TestCase):
    """tests for utils.memoize decorator"""
    def test_memoize(self):
        """only called once using assert_called_once"""
        pass
