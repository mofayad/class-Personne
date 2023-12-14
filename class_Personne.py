class Personne:
    def __init__(self, code, nom, prenom, age):
        self._code = code
        self._nom = nom
        self._prenom = prenom
        self._age = age

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, value):
        self._prenom = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    def __str__(self):
        return f"Code: {self._code}, Nom: {self._nom}, Prénom: {self._prenom}, Âge: {self._age}"

    def __eq__(self, other):
        if not isinstance(other, Personne):
            return False
        return self._code == other._code


class Employe(Personne):
    def __init__(self, code, nom, prenom, age, grade):
        super().__init__(code, nom, prenom, age)
        self._grade = grade
        PersonneCompteur.incrementer_employe()

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value

    def __str__(self):
        return f"{super().__str__()}, Grade: {self._grade}"


class Eleve(Personne):
    def __init__(self, code, nom, prenom, age, niveau, moyenne):
        super().__init__(code, nom, prenom, age)
        self._niveau = niveau
        self._moyenne = moyenne
        PersonneCompteur.incrementer_eleve()

    @property
    def niveau(self):
        return self._niveau

    @niveau.setter
    def niveau(self, value):
        self._niveau = value

    @property
    def moyenne(self):
        return self._moyenne

    @moyenne.setter
    def moyenne(self, value):
        self._moyenne = value

    def __str__(self):
        return f"{super().__str__()}, Niveau: {self._niveau}, Moyenne: {self._moyenne}"


class PersonneCompteur:
    nombre_objets_employe = 0
    nombre_objets_eleve = 0

    @staticmethod
    def incrementer_employe():
        PersonneCompteur.nombre_objets_employe += 1

    @staticmethod
    def incrementer_eleve():
        PersonneCompteur.nombre_objets_eleve += 1


class TestClasse:
    @staticmethod
    def run():
        # Créer trois objets de type Employe
        employe1 = Employe(1, "Dupont", "Jean", 30, "Manager")
        employe2 = Employe(2, "Martin", "Sophie", 25, "Ingénieur")
        employe3 = Employe(3, "Lefevre", "Pierre", 35, "Technicien")

        # Créer trois objets de type Eleve
        eleve1 = Eleve(101, "Tremblay", "Julie", 18, "Secondaire", 75.5)
        eleve2 = Eleve(102, "Gagnon", "Marc", 17, "Secondaire", 82.0)
        eleve3 = Eleve(103, "Leblanc", "Isabelle", 16, "Primaire", 90.3)

        # Afficher les informations de tous les objets
        print(employe1)
        print(employe2)
        print(employe3)
        print(eleve1)
        print(eleve2)
        print(eleve3)

        # Tester la méthode Equals
        print(f"employe1 Equals employe2: {employe1 == employe2}")
        print(f"eleve1 Equals eleve2: {eleve1 == eleve2}")

        # Afficher le nombre d'objets créés pour chaque classe
        print(f"Nombre d'objets Employe créés : {PersonneCompteur.nombre_objets_employe}")
        print(f"Nombre d'objets Eleve créés : {PersonneCompteur.nombre_objets_eleve}")


# Exécuter le test
TestClasse.run()
