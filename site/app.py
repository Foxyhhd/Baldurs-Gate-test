from flask import Flask, render_template, request

class BaldursGateQuizApp:
    def __init__(self):
        self.app = Flask(__name__, template_folder="templates", static_folder="static")
        self.add_routes()

    def add_routes(self):
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/result', 'result', self.result, methods=["POST"])
        self.app.add_url_rule('/tests', 'tests', self.tests)
        self.app.add_url_rule('/about', 'about', self.about)

    def index(self):
        return render_template("index.html")

    def tests(self):
        return render_template("tests.html")

    def result(self):
        answers = request.form
        character = self.determine_character(answers)
        return render_template("result.html", character=character)

    def about(self):
        return render_template("about.html")

    @staticmethod
    def determine_character(answers):
        traits = {
            "brave": "Минск",
            "wise": "Гейл",
            "kind": "Карлах",
            "cunning": "Астарион",
            "strict": "Лаэзель",
            "dark": "Шэдоухарт"
        }
        roles = {
            "leader": "Минск",
            "healer": "Хальсин",
            "fighter": "Карлах",
            "rogue": "Астарион",
            "mage": "Гейл"
        }
        goals = {
            "glory": "Минск",
            "knowledge": "Гейл",
            "protect": "Шэдоухарт",
            "power": "Лаэзель"
        }
        rules = {
            "strict": "Лаэзель",
            "flexible": "Гейл",
            "pragmatic": "Астарион",
            "chaotic": "Шэдоухарт"
        }
        weapons = {
            "sword": "Минск",
            "staff": "Гейл",
            "dagger": "Астарион",
            "mace": "Карлах",
            "bow": "Лаэзель"
        }
        places = {
            "tavern": "Карлах",
            "library": "Гейл",
            "wilderness": "Хальсин",
            "castle": "Лаэзель",
            "dark_alley": "Шэдоухарт"
        }
        mood_fix = {
            "training": "Лаэзель",
            "reading": "Гейл",
            "adventure": "Минск",
            "meditation": "Шэдоухарт",
            "drinking": "Карлах"
        }
        colors = {
            "red": "Карлах",
            "blue": "Гейл",
            "green": "Хальсин",
            "black": "Шэдоухарт",
            "gold": "Лаэзель"
        }

        choices = [
            traits.get(answers.get("question1")),
            roles.get(answers.get("question2")),
            goals.get(answers.get("question3")),
            rules.get(answers.get("question4")),
            weapons.get(answers.get("question5")),
            places.get(answers.get("question6")),
            mood_fix.get(answers.get("question7")),
            colors.get(answers.get("question8"))
        ]
        
        choices = [choice for choice in choices if choice is not None]
        
        if not choices:
            return {"name": "Неизвестно", "image": "unknown.jpg", "description": "Не удалось определить персонажа."}
        
        most_common = max(set(choices), key=choices.count)
        
        characters_info = {
            "Минск": {"name": "Минск", "image": "minsk.jpg", "description": "Герой, идущий напролом с верным хомяком Бу"},
            "Гейл": {"name": "Гейл", "image": "gale.jpg", "description": "Могущественный маг, жаждущий знаний и силы"},
            "Карлах": {"name": "Карлах", "image": "karlach.jpg", "description": "Добрая, но грозная воительница"},
            "Астарион": {"name": "Астарион", "image": "astarion.jpeg", "description": "Хитрый вампир, любящий свободу"},
            "Лаэзель": {"name": "Лаэзель", "image": "laezel.jpg", "description": "Жесткая и бескомпромиссная гитянка-воительница"},
            "Шэдоухарт": {"name": "Шэдоухарт", "image": "shadowheart.jpg", "description": "Таинственная жрица с темным прошлым"},
            "Хальсин": {"name": "Хальсин", "image": "halsin.jpg", "description": "Мудрый друид, защитник природы."}
        }

        return characters_info.get(most_common, {"name": "Неизвестно", "image": "unknown.jpg", "description": "Не удалось определить персонажа."})
    
    def run(self):
        self.app.run(debug=True, host="0.0.0.0", port=5000)

if __name__ == "__main__":
    app_instance = BaldursGateQuizApp()
    app_instance.run()
