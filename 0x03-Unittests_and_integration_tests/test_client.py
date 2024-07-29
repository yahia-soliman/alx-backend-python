#!/usr/bin/env python3
"""Testing utils for the client utils"""

import unittest
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """Test the functionality of the mentioned function"""

    # @patch get_json called once
    @parameterized.expand([
        ("google",),
        ("abc",)
        ])
    def test_org(self, *_):
        """test case for different org"""
        pass

    # @patch org
    def test_public_repos_url(self):
        """testing with patching"""
        pass

    # @patch get_json
    def test_public_repos(self):
        """Test puplic github repos"""
        pass

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license"),
        ({"license": {"key": "other_license"}}, "my_license"),
    ])
    def test_has_license(self, *_):
        """Test that a repo has a license"""
        pass


@parameterized_class([])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """integration testing with fixtures"""

    @classmethod
    def setUpClass(cls) -> None:
        """Setup the test cases"""
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        """What happens after the test"""
        return super().tearDownClass()
