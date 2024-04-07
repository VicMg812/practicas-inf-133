from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import random

class Player:
    _instance = None

    def __new__(cls, name):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.name = name
            cls._instance.health = 100
        return cls._instance
    
    def to_dict(self):
        return {"name": self.name, "health": self.health}
    
    def take_damage(self, damage):
        self.health -= damage

class Game:
    def __init__(self):
        self.games = {}
        self.game_id_counter = 1

    def play(self, player_element):
        server_element = random.choice(["piedra", "papel", "tijera"])
        if player_element == server_element:
            result = "empató"
        elif (player_element == "piedra" and server_element == "tijera") or \
             (player_element == "tijera" and server_element == "papel") or \
             (player_element == "papel" and server_element == "piedra"):
            result = "ganó"
        else:
            result = "perdió"
        game_data = {
            "id": self.game_id_counter,
            "elemento_jugador": player_element,
            "elemento_servidor": server_element,
            "resultado": result
        }
        self.games[self.game_id_counter] = game_data
        self.game_id_counter += 1
        return game_data

class GameHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/partidas":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            player_element = json.loads(post_data.decode("utf-8"))["elemento"]
            game_data = game.play(player_element)
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(game_data).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        if self.path == "/partidas":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            game_data = json.dumps(game.games)
            self.wfile.write(game_data.encode("utf-8"))
        elif self.path.startswith("/partidas?resultado="):
            result = self.path.split("=")[-1]
            filtered_games = {game_id: game_data for game_id, game_data in game.games.items() if game_data["resultado"] == result}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            game_data = json.dumps(filtered_games)
            self.wfile.write(game_data.encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

def main():
    global game
    game = Game()

    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, GameHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()

if __name__ == "__main__":
    main()