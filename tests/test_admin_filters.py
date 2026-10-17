"""Unit tests for administrative access checks."""

import unittest
from types import SimpleNamespace

from filters.admin import IsAdminFilter
from handlers.admin.menu import _AdminFlagFilter


class AdminFilterTests(unittest.IsolatedAsyncioTestCase):
    async def test_allowlisted_user_is_admin(self):
        event = SimpleNamespace(from_user=SimpleNamespace(id=123))
        self.assertTrue(await IsAdminFilter(frozenset({123}))(event))

    async def test_unlisted_user_is_denied(self):
        event = SimpleNamespace(from_user=SimpleNamespace(id=456))
        self.assertFalse(await IsAdminFilter(frozenset({123}))(event))

    async def test_missing_user_is_denied(self):
        self.assertFalse(await IsAdminFilter(frozenset({123}))(SimpleNamespace(from_user=None)))

    async def test_menu_flag_accepts_injected_keyword(self):
        event = SimpleNamespace()
        guard = _AdminFlagFilter()
        self.assertTrue(await guard(event, is_admin=True))
        self.assertFalse(await guard(event, is_admin=False))
        self.assertFalse(await guard(event))


if __name__ == "__main__":
    unittest.main()
