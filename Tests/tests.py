#!/usr/bin/python
import mock
import unittest
import pylast
from frontend import frontend_lib
import models
import AVSrobbler.avlogic


"""Tests for functionality of scrobbler
    
    AVScrobbler version 1.0
    --------------
    Passed: 3
   
"""


def init(self):
        self.config = {
            'AVScrobbler': {
                'username': 'domingo__chavez',
                'password': 'secret',
            }
        }
        self.frontend = frontend_lib.ScrobblerFrontend(
            self.config, mock.sentinel.core)


def test_on_start_creates_lastfm_network(self, pylast_mock):
        pylast_mock.md5.return_value = mock.sentinel.password_hash

        self.frontend.on_start()

        pylast_mock.LastFMNetwork.assert_called_with(
            api_key=frontend_lib.API_KEY,
            api_secret=frontend_lib.API_SECRET,
            username='alice',
            password_hash=mock.sentinel.password_hash)
            
 #test for scrobble if music played for 240sec           
 def test_does_scrobble_if_played_not_half_but_240_sec(self, pylast_mock):
        self.frontend.lastfm = mock.Mock(spec=pylast.LastFMNetwork)
        track = models.Track(length=880432)
        tl_track = models.TlTrack(track=track, tlid=17)
        #track playback ended.
        self.frontend.track_playback_ended(tl_track, 241432)
        #Check for scrobble count.
        self.assertEqual(self.frontend.lastfm.scrobble.call_count, 1) 
            
            
#test for scrobble if music played less than 30 seconds
def test_does_not_scrobble_tracks_shorter_than_30_sec(self, pylast_mock):
        self.frontend.lastfm = mock.Mock(spec=pylast.LastFMNetwork)
        track = models.Track(length=20432)
        
        tl_track = models.TlTrack(track=track, tlid=17)
        self.frontend.track_playback_ended(tl_track, 20432)
        self.assertEqual(self.frontend.lastfm.scrobble.call_count, 0)
        
        
        
  def test_does_not_scrobble_if_played_less_than_half(self, pylast_mock):
        self.frontend.lastfm = mock.Mock(spec=pylast.LastFMNetwork)
        track = models.Track(length=180432)
        tl_track = models.TlTrack(track=track, tlid=17)

        self.frontend.track_playback_ended(tl_track, 60432)

        self.assertEqual(self.frontend.lastfm.scrobble.call_count, 0)
        
        
        