"""Throwing a Tea Party"""

__author__ = "730719749"


def main_planner(guests: int) -> None:
    """Number of guests attending"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Returns number of tea bags for guests"""
    return people * 2


def treats(people: int) -> int:
    """Returns number of treats per guest"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Cost of teabags and treats"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
