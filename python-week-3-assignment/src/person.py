from abc import ABC, abstractmethod


class Person(ABC):
    """Abstract base class representing a person."""

    @abstractmethod
    def get_gender(self) -> str:
        """Return the person's gender."""
        ...


class Male(Person):
    """Represent a male person."""

    def get_gender(self) -> str:
        return "Male"


class Female(Person):
    """Represent a female person."""

    def get_gender(self) -> str:
        return "Female"


if __name__ == "__main__":
    male = Male()
    print(male.get_gender())

    female = Female()
    print(female.get_gender())

    # person = Person()
    # print(person.get_gender())
