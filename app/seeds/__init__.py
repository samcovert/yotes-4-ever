from flask.cli import AppGroup
from .users import seed_users, undo_users
from .comments import seed_comments, undo_comments
from .images import seed_images, undo_images
from .memories import seed_memories, undo_memories
from .merchandise import seed_merch, undo_merch
from .news import seed_news, undo_news
from .players import seed_players, undo_players
from .teams import seed_teams, undo_teams

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_users()
        undo_teams()
        undo_comments()
        undo_images()
        undo_memories()
        undo_merch()
        undo_news()
        undo_players()
    seed_users()
    seed_memories()
    seed_news()
    seed_merch()
    seed_teams()
    seed_players()
    seed_images()
    seed_comments()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_memories()
    undo_merch()
    undo_news()
    undo_teams()
    undo_players()
    undo_comments()
    undo_images()
    # Add other undo functions here
