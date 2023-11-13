class student:
    def __init__(self,Name,roll_number):
        self.Name=Name
        self.roll_number=roll_number
        self.aeg=None
        self.marks=None

    def display(self):
        print("Name",self.Name)
        print("Roll_number",self.roll_number)
        print("Aeg",self.aeg)
        print("Marks",self.marks)

    def setaeg(self,aeg):
        self.aeg=aeg

    def setmarks(self,marks):
        self.marks=marks

student1=student("John doe","12345")
student1.setaeg(20)
student1.setmarks(75)
student1.display()