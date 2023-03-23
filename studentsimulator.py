class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        self.health = 100
        self.money = 0
        self.points = 0

    def study(self):
        self.health -= 10
        self.points += 10
        print(f"{self.name} вивчив новий матеріал!")

    def rest(self):
        self.health += 10
        self.money -= 20
        print(f"{self.name} відпочив")

    def work(self):
        self.money += 50
        self.health -= 20
        print(f"{self.name} пішов на роботу")

    def spend_money(self, amount):
        self.money -= amount

    def earn_money(self, amount):
        self.money += amount

    def check_health(self):
        if self.health <= 0:
            print(f"{self.name} дуже погано почувається. Потрібна допомога!")
        elif self.health < 30:
            print(f"{self.name} не почувається добре. Потрібно відпочити.")

    def check_points(self):
        if self.points >= 100:
            print(f"{self.name} закінчив курс!")

    def year_in_college(self):
        return f"{self.name} навчається на {self.course} курсі"