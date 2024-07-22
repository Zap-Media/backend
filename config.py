from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY              = os.environ.get('SECRET_KEY')
    MONGO_URL               = os.environ.get('MONGO_URL')

    GOOGLE_CLIENT_ID        = os.environ.get('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET    = os.environ.get('GOOGLE_CLIENT_SECRET')

    DISCORD_CLIENT_ID       = os.environ.get('DISCORD_CLIENT_ID')
    DISCORD_CLIENT_SECRET   = os.environ.get('DISCORD_CLIENT_SECRET')

    GITHUB_CLIENT_ID        = os.environ.get('GITHUB_CLIENT_ID')
    GITHUB_CLIENT_SECRET    = os.environ.get('GITHUB_CLIENT_SECRET')

    ImagekitID              = os.environ.get('ImagekitID')
    JWT_SECRET              = os.environ.get('JWT_SECRET')

    OAUTH2_PROVIDERS        =  {
        'google': {
            'client_id': os.environ.get('GOOGLE_CLIENT_ID'),
            'client_secret': os.environ.get('GOOGLE_CLIENT_SECRET'),
            'authorize_url': 'https://accounts.google.com/o/oauth2/auth',
            'token_url': 'https://accounts.google.com/o/oauth2/token',
            'userinfo': {
                'url': 'https://www.googleapis.com/oauth2/v3/userinfo',
                'email': lambda json: json['email'],
            },
            'scopes': ['https://www.googleapis.com/auth/userinfo.email'],
        },
        'discord': {
            'client_id': os.environ.get('DISCORD_CLIENT_ID'),
            'client_secret': os.environ.get('DISCORD_CLIENT_SECRET'),
            'authorize_url': 'https://discord.com/api/oauth2/authorize',
            'token_url': 'https://discord.com/api/oauth2/token',
            'userinfo': {
                'url': 'https://discord.com/api/users/@me',
                'email': lambda json: json['email'],
            },
            'scopes': ['identify email'],
        },
    }
    ALLOWED_REDIRECTS = [
        "https://zap-social.vercel.app/auth/callback/google",
        "https://zap-social.vercel.app/auth/callback/discord",
        "https://zap-blogs.vercel.app/auth/callback/google",
        "https://zap-blogs.vercel.app/auth/callback/discord",
        "https://zapfolio.vercel.app/auth/callback/google",
        "https://zapfolio.vercel.app/auth/callback/discord",
        "http://127.0.0.1:6969/auth/callback/discord",
        "http://127.0.0.1:6969/auth/callback/google"
    ]

    SERVICES = [
        "zap-social", "zap-blogs", "zapfolio"
    ]

    TOKEN_EXP = {
        "access": 1,
        "refresh": 30
    }