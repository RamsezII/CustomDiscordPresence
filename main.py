import sys
from pypresence import Presence
import time


def update_discord_presence(state):
    client_id = '1201978243046178867'

    RPC = Presence(client_id)
    RPC.connect()

    try:
        RPC.update(state=state)
        while True:
            time.sleep(15)
    except KeyboardInterrupt:
        RPC.close()


def main():
    state = sys.argv[1]

    update_discord_presence(state)


if __name__ == '__main__':
    main()
    print(" --- END --- ")
