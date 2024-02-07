from utils import read_csv
import os
import time
# from user import Student

class StudentModule:
    def __init__(self):
        self.LoginAttempts = 0
        self.DataDir = os.path.join(os.getcwd(), "Data")
        self.SETUP()

    def authenticate_student(self):
        os.system("cls")
        print(f"\t{'#'*50}\n\t\t\tStudent Login\n\t{'#'*50}")
        while True:
            username = input("\n\tEnter your username: ")
            password = input("\tEnter your password: ")
            
            LogedIn = False
            for first, last, usr, pwd in self.studentsData:
                if usr == username and pwd == password:
                    LogedIn = [True, username]
            
            if LogedIn: 
                print("\n\tLOGGING YOU IN ...")
                print(f"\tWelcome'{username}'")
                time.sleep(1.5)
                return [username]
            else: 
                if self.LoginAttempts <= 5:
                    print("\n\tINCORRECT USERNAME OR PASSWORD ...")
                    print(f"\tPLAEASE TRY AGAIN")
                    self.LoginAttempts += 1
                    time.sleep(0.5)
                    os.system("cls")
                    print(f"\t{'#'*50}\n\t\t\tStudent Login\n\t{'#'*50}")
                else:
                    print("\n\tLOGIN LIMIT EXCEEDED! TRY AGAIN LATER ...")
                    time.sleep(0.5)
                    return False

    def view_enrolled_courses(self, user):
        os.system("cls")
        print(f"\t{'#'*50}\n\t\t\tStudent Login\n\t{'#'*50}")
        courses = []
        for student, course  in self.enrollmentsData:
            if student == user[0]:
                courses.append(course)
        
        header = "Student Id".ljust(20) + "Course Title".ljust(40)
        line = '-' * 40 
        print(f"\n\t{line}\n\t{header}\n\t{line}")
        
        for course in courses:
            print("\t{:<20}\t{:<40}".format(user[0], course))
        
        input("\n\tPress Enter")
    
    def DashBoard(self, user):
        while True:
            os.system("cls")
            print(f"\t{'#'*50}\n\t\t\tStudent DashBord\n\t{'#'*50}") 
            print("\n\t1: View Enrolled Courses")
            print("\t2: Logout")
            
            choice = int(input("\n\tChoice (1-2): "))
            
            match choice:
                case 1:
                    self.view_enrolled_courses(user)
                case 2:
                    return True
    
    def SETUP(self):
        self.studentsData = read_csv(os.path.join(self.DataDir, 'students.csv'))
        self.enrollmentsData = read_csv(os.path.join(self.DataDir, 'enrollments.csv'))
    
    
    
    

