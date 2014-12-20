from AVScrobbler import avlogic
import scrobbler


if __name__ == "__main__":
    api_root = 'https://ws.audioscrobbler.com/2.0/'  # https for mobile
    #apikey of your last fm account
    #secret key of your last account
    api_key = '7d57a78411fdf10e0409d678d2a950a2' 
    secret = '6cfcb085801ad30d7ebc1da06544920e'
    #write username and password of lastfm account
    session_key = login('myuser', 'mypassword')
    submit('Arjun', 'Verma')