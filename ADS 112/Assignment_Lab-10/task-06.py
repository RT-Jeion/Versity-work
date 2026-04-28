# Write a Python class 'Person' with display and voting eligibility methods.

class Person:
    def __init__(self, name: str, voter_id: str, birth_year: int):
        self.name = name
        self.voter_id = voter_id
        self.birth_year = birth_year

    def display(self):
        print("Name:", self.name)
        print("Voter ID:", self.voter_id)
        print("Birth Year:", self.birth_year)
        print()

    def eligibility(self):
        if self.birth_year < 2008:
            return f"{self.name}\nVoter ID: {self.voter_id}\nIs Eligible for Voting.\n"
        else:
            return f"{self.name}\nVoter ID: {self.voter_id}\nIs not Eligible for Voting.\n"


rt = Person("RT Jeion", "007", 2005)
rejuwan = Person("Rejuwan Tasfic", "001", 2006)

rt.display()
rejuwan.display()

print(rt.eligibility())
print(rejuwan.eligibility())