password = "SuperSecret123!"
api_key = "API_KEY_ABCDEFG12345"
secret_key = "SECRET_KEY_XYZ98765"

domain1 = "Test.com"
domain2 = "medic-game.com"
game_name = "medic_game"

def connect_to_api():
    print(f"Connecting to API at {domain1} with key {api_key}")

def authenticate():
    print(f"Authenticating with secret key: {secret_key}")

def start_game():
    print(f"Launching {game_name} on {domain2}")

if __name__ == "__main__":
    connect_to_api()
    authenticate()
    start_game()
