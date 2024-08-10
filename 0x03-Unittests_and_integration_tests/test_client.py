#!/usr/bin/env python3
"""Testing utils for the client utils"""
import unittest
from unittest.mock import PropertyMock, patch

from parameterized import parameterized, parameterized_class

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test the functionality of the mentioned function"""

    @parameterized.expand(["google", "abc"])
    @patch("client.get_json")
    def test_org(self, org, get_json):
        """test case for different org"""
        get_json.return_value = {}
        c = GithubOrgClient(org)
        self.assertEqual(c.org, {})
        get_json.assert_called_with(f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self):
        """testing with patching"""
        payload = {"repos_url": "hi"}
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
        ) as org:
            org.return_value = payload
            c = GithubOrgClient("org")
            self.assertEqual(c._public_repos_url, payload["repos_url"])
            org.assert_called_with()

    @patch("client.get_json")
    def test_public_repos(self, get_json):
        """Test puplic github repos"""
        payload = [{"name": "repo name"}]
        get_json.return_value = payload
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mocked:
            c = GithubOrgClient("org")
            repos = c.public_repos()
            self.assertEqual(repos, ["repo name"])
            mocked.assert_called_once()
            get_json.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license, expected):
        """Test that a repo has a license"""
        c = GithubOrgClient("org")
        self.assertEqual(c.has_license(repo, license), expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD,
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """integration testing with fixtures"""

    @classmethod
    def setUpClass(cls) -> None:
        """Setup the mocking before all tests"""
        patcher = patch("requests.get")
        cls.get_patcher = patcher
        patching = patcher.start()
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        """What happens after all tests in the class"""
        cls.get_patcher.stop()
        return super().tearDownClass()
