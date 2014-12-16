import mock
import unittest

import pylast

from mopidy import models


def test_on_start_creates_lastfm_network(self, pylast_mock):
        pylast_mock.md5.return_value = mock.sentinel.password_hash

        self.frontend.on_start()

        pylast_mock.LastFMNetwork.assert_called_with(
            api_key=frontend_lib.API_KEY,
            api_secret=frontend_lib.API_SECRET,
            username='alice',
            password_hash=mock.sentinel.password_hash)