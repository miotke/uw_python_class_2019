""" Database setup scripts """

from datetime import datetime
from model import db, User, Task
from passlib.hash import pbkdf2_sha256

# Create the database tables from our model
db.connect()
db.drop_tables([User, Task])
db.create_tables([User, Task])

Task(name="Do the laundry").save()
Task(name="Do the dishes", performed=datetime.now()).save()
User(name="admin", password=pbkdf2_sha256.hash("password")).save()
User(name="Gus", password=pbkdf2_sha256.hash("gusgus")).save()
