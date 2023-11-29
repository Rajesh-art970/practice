'''class student:
    
    def __init__(self):
        self.name="rajesh"
        self.add="hyd"       
a1=student()
print(a1.name,a1.add)        '''

class student:
    
    school="high school"
    def __init__(self,telugu,comp,maths):
        self.telugu=telugu
        self.comp=comp
        self.maths=maths
        
    def avg(self):
        return(self.telugu+self.comp+self.maths)/3
            
    def getschool(cls):
        return cls.school  
    def info():
        print("this is student information..........")  
        
        
        
b2=student(35,55,90)
b3=student(25,50,45)
print(b2.avg()) 
print(b3.avg())
print(student.getschool(b2))  
print(student.getschool(b3)) 
student.info()           