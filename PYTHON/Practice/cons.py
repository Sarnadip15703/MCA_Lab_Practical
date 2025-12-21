class student:
    def __init__ (self,roll_no,name,stream):
        self.roll_no=roll_no
        self.name=name
        self.stream=stream
        self.marks=[]

    def set_marks(self):
        print("Enter marks for 5 subject")
        for i in range (5):
            m=int(input())
            self.marks.append(m)
    def get_stream(self):
        print(self.stream)
    def percentage(self):
        total=sum(self.marks)
        percent=total/5
        return percent
    def grade(self):
        print("Grades")
        for m in self.marks:
            if m>=90:
                print("O")
            elif m>=80:
                print("E")
            elif m>=70:
                print("A")
            elif m>=60:
                print("B")
            elif m>=50:
                print("C")
            elif m>=40:
                print("D")
            else:
                print("F")
    def division(self):
        p=self.percentage()
        if p>=60:
            print("First Division")
        elif p>=50:
            print("Second Division")
        elif p>=40:
            print("Third Division")
        else:
            print("Fail")
            
s1=student(100,"sarna","Arts")
s1.get_stream()
s1.set_marks()
per=s1.percentage()
print("percent:",per)

s1.grade()
s1.division()