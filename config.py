import os

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
        'github': {
            'client_id': os.environ.get('GITHUB_CLIENT_ID'),
            'client_secret': os.environ.get('GITHUB_CLIENT_SECRET'),
            'authorize_url': 'https://github.com/login/oauth/authorize',
            'token_url': 'https://github.com/login/oauth/access_token',
            'userinfo': {
                'url': 'https://api.github.com/user/emails',
                'email': lambda data: next((x['email'] for x in data if x['primary'] == True), None),
            },
            'scopes': ['user:email'],
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