import hashlib
import requests
import time
import xml.etree.ElementTree as ET



def login(user, password):
    """"
    Authenticate using last.fm mobile applications authentication
    :param user: user to update
    :type user: str
    :param password: user's pass
    :type password: str
    :returns: session key if ok else false
    """
    api_sig = hashlib.md5('api_key' + api_key + 'methodauth.getMobileSession'
                          + 'password' + password + 'username' + user
                          + secret).hexdigest()
    post_data = {'method': 'auth.getMobileSession', 'password': password,
                 'username': user, 'api_key': api_key, 'api_sig': api_sig}
    results = requests.post(api_root, data=post_data)
    root = ET.fromstring(results.text)
    status = root.get('status')
    if status == 'ok':
        session_key = root.find("./session/key").text
        return session_key
    else:
        return None


def submit(artist, track, timestamp=None):
    timestamp = str(int(time.time()))
    api_sig = hashlib.md5('api_key' + api_key + 'artist' + artist
                          + 'methodtrack.scrobble' + 'sk' + session_key
                          + 'timestamp' + timestamp + 'track' + track
                          + secret).hexdigest()
    post_data = {'method': 'track.scrobble', 'artist': artist, 'track': track,
                 'timestamp': timestamp, 'api_key': api_key,
                 'api_sig': api_sig, 'sk': session_key}
    results = requests.post(api_root, data=post_data)
    root = ET.fromstring(results.text)
    status = root.get('status')
    if status == 'ok':
        accepted = root.find("scrobbles").get('accepted')
        print accepted
    return status


if __name__ == "__main__":
    api_root = 'https://ws.audioscrobbler.com/2.0/'  # https for mobile

    
    api_key = '7d57a78411fdf10e0409d678d2a950a2'
    secret = '6cfcb085801ad30d7ebc1da06544920e'

    session_key = login('myuser', 'mypassword')
    submit('Arjun', 'MusicLover')