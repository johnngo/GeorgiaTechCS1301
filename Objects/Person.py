class Person:
    def __init__(self, name, age, father=None, mother=None):
        self.name = name
        self.age = age
        self.father = father
        self.mother = mother

#There are two slightly different ways we could approach this.
#First, the more obvious way is to create all three instances
#first, then link them up. So, first we create each instance:

george_p = Person("George P. Burdell", 25)
the_mother = Person("Mrs. Burdell", 53)
the_father = Person("Mr. Burdell", 53)

#Then, we declare that george_p's mother and father are
#the_mother and the_father:

george_p.mother = the_mother
george_p.father = the_father

#There is a slightly simpler way to do this, though: check out
#sample_answer_2.py to see!



print(george_p.name)
print(george_p.mother.name)
print(george_p.father.name)