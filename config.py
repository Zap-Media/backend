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