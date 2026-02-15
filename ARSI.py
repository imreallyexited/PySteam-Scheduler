import os
import sys

# Fix for Google Protobuf error
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

# Patching gevent and socket for Steam client
import gevent.monkey
gevent.monkey.patch_socket()
gevent.monkey.patch_ssl()

# Patch for eventemitter module
try:
    import gevent_eventemitter
    sys.modules['eventemitter'] = gevent_eventemitter
except ImportError:
    pass

from steam import guard
from steam.client import SteamClient
from steam.enums import EResult

# --- HELPER FUNCTION: PREVENT WINDOW CLOSING ---
def pause_and_exit():
    print("\n" + "="*40)
    input("Program terminated. Press ENTER to exit...")
    sys.exit()

print("\n" + "="*40)
print("   Auto-Refuse-Steam-Invites (Alpha)")
print("   Github: github.com/imreallyexited/Auto-Refuse-Steam-Invites")
print("="*40 + "\n")

try:
    if not os.path.exists("config.txt"):
        print("ERROR: 'config.txt' not found!")
        print("Please ensure config.txt is in the same folder as the executable.")
        pause_and_exit()

    # Read config lines
    config = open("config.txt", "r+").read().splitlines()
    
    # Check if config has enough lines
    if len(config) < 8:
        print("ERROR: config.txt file is incomplete or corrupted.")
        print("Please check username, password, and secret fields.")
        pause_and_exit()

except Exception as e:
    print(f"ERROR: An issue occurred while reading config:\n{e}")
    pause_and_exit()

try:
    secrets = {'shared_secret': config[5], 'identity_secret': config[7]}
    
    # Check if secrets are empty
    if not config[5] or not config[7]:
        print("WARNING: Shared Secret or Identity Secret appears to be empty.")
        print("Mobile confirmation might be required for login.")
    
    SA = guard.SteamAuthenticator(secrets)
except Exception as e:
    print(f"ERROR: Issue with secret keys:\n{e}")
    pause_and_exit()

client = SteamClient()

@client.on("error")
def handle_error(result):
    print(f"\nSteam Error: {result}")

@client.on("connected")
def handle_connected():
    print(f"SUCCESS: Logged in as '{client.user.name}'")
    print("MODE: Auto-Refuse Invites is ACTIVE.")
    print("-" * 30)
    print("Waiting for invites... (Close window to stop)")

@client.on("reconnect")
def handle_reconnect(delay):
    print(f"\nConnection lost. Reconnecting in {delay} seconds...")

@client.on("disconnected")
def handle_disconnect():
    print("\nDisconnected from Steam.")
    if client.relogin_available:
        print("Attempting to reconnect...")
        client.reconnect(maxdelay=30)

@client.friends.on("friend_invite")
def reject_invite(user):
    # Try to get username, fallback to Steam ID
    try:
        user_id = user.name if user.name else str(user.steam_id)
    except:
        user_id = "Unknown User"

    print(f"\nDETECTED: Invite from {user_id}")
    try:
        client.friends.remove(user)
        print(f"ACTION: Rejected invite from {user_id}")
    except Exception as e:
        print(f"ERROR: Could not reject invite. Reason: {e}")

try:
    print("Connecting to Steam servers...")
    
    # Attempt login
    result = client.login(username=config[1], password=config[3], two_factor_code=SA.get_code())

    if result != EResult.OK:
        print(f"\nLOGIN FAILED! Error Code: {repr(result)}")
        print("Possible causes:")
        print("1. Invalid username or password.")
        print("2. Invalid Shared Secret (Could not generate 2FA code).")
        print("3. Steam servers are down.")
        pause_and_exit()
    
    client.run_forever()

except KeyboardInterrupt:
    print("\nStopped by user.")
    pause_and_exit()
except Exception as GenlError:
    print(f"\nUNEXPECTED ERROR:\n{GenlError}")
    pause_and_exit()
