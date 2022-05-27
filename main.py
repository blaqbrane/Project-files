class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        #pass


Bob = Student(name=input("Enter your name"), age=input("Enter age"), tracks=input("Enter track"), score=41.50)
print("Student details:")
print("His name is ", Bob.name)
print("age:", Bob.age)
print("track:", Bob.tracks )
print("score:", Bob.score)

# Expected methods
#Bob.change_name("Peter")
#Bob.change_age(34)
#Bob.add_track("UI/UX")
#Bob.get_score()
def get_score(self):
    print("Bob score is", self.score)
    return self.score
