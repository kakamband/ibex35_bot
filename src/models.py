from peewee import *
from playhouse.db_url import connect
from os import environ

db = connect(environ['DATABASE_URL'])


class Mention(Model):
    tweet_id = BigIntegerField()

    class Meta:
        database = db
        table_name = 'mentions'


def main():
    db.create_tables([Mention])


if __name__ == "__main__":
    main()
