from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/crew.db")
    db_sess = db_session.create_session()
    surnames = ["Scott", "Smith", "Roy", "Rodriguez"]
    names = ["Ridley", "James", "Mary", "Thomas"]
    ages = [26, 32, 25, 21]
    positions = ["captain", "crewmate", "crewmate", "crewmate"]
    specialities = ["research engineer", "engineer", "general doctor", "astronaut"]
    address = "module_1"
    emails = ["scott_chief", "smith_engi", "roy_doc", "rodriguez_astronaut"]
    for i in range(4):
        new_crewmate = User()
        new_crewmate.surname = surnames[i]
        new_crewmate.name = names[i]
        new_crewmate.age = ages[i]
        new_crewmate.position = positions[i]
        new_crewmate.speciality = specialities[i]
        new_crewmate.address = address
        new_crewmate.email = f"{emails[i]}@mars.org"
        db_sess.add(new_crewmate)
    db_sess.commit()
    app.run()


if __name__ == '__main__':
    main()
