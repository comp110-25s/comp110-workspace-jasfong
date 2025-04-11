"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        alive_fish = []
        for fish in self.fish:
            if fish.age <= 3:
                alive_fish.append(fish)
        self.fish = alive_fish

        alive_bears = []
        for bears in self.bears:
            if bears.age <= 5:
                alive_bears.append(bears)
        self.bear = alive_bears
        return None

    def remove_fish(self, amount: int):
        self.fish = self.fish[amount:]

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        alive_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                alive_bears.append(bear)
        self.bears = alive_bears
        return None

    def repopulate_fish(self):
        n_fish = (len(self.fish) // 2) * 4
        while n_fish > 0:
            self.fish.append(Fish())
            n_fish -= 1
        return None

    def repopulate_bears(self):
        n_bears = len(self.bears) // 2
        while n_bears > 0:
            self.bears.append(Bear())
            n_bears -= 1
        return None

    def view_river(self):
        print("~~~ Day " + (str(self.day)) + ": ~~~")
        print("Fish population: " + (str(len(self.fish))))
        print("Bear population: " + (str(len(self.bears))))
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        i: int = 0
        while i < 7:
            self.one_river_day()
            i += 1
        return None
