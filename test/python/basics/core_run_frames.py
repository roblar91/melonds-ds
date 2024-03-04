from sys import argv
from libretro import default_session

with default_session(argv[1]) as session:
    for i in range(300):
        session.core.run()
