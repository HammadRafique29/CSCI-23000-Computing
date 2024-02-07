import os
from utils import read_csv, write_csv, check_uniqueness
# from user import Admin, Student, Course, Enrollment
import time

class AdminModule:
    def __init__(self):
        self.adminsData = None
        self.studentsData = None
        self.coursesData = None
        self.enrollmentsData = None
        self.LoginAttempts = 0
        self.DataDir = os.path.join(os.getcwd(), "Data")
        self.SETUP()

    def authenticate_admin(self, username=None, password=None):

        while True:
            os.system("cls")
            print(f"\t{'#'*50}\n\t\t\tAdmin Login\n\t{'#'*50}")
        
            username = input("\n\tEnter Admin UserName: ")
            password = input("\tEnter Admin Password: ")
            
            LogedIn = False
            for usr, pwd in self.adminsData:
                if usr == username and pwd == password:
                    LogedIn = [True, username]
            
            if LogedIn: 
                print("\n\tLOGGING YOU IN ...")
                print(f"\tWelcome'{username}'")
                time.sleep(2)
                return True
            else: 
                if self.LoginAttempts <= 5:
                    print("\n\tINCORRECT USERNAME OR PASSWORD ...")
                    print(f"\tPLAEASE TRY AGAIN")
                    self.LoginAttempts += 1
                    time.sleep(1.5)
                else:
                    print("\n\tLOGIN LIMIT EXCEEDED! TRY AGAIN LATER ...")
                    time.sleep(1.5)
                    return False
                                
    def clearScreen(self, title):
        os.system("cls")
        print(f"\t{'#'*50}\n\t\t\t{title}\n\t{'#'*50}")
        
    def add_student(self):
        os.system("cls")
        print(f"\t{'#'*50}\n\t\t\tAdd Student\n\t{'#'*50}")
        
        firstName = input("\n\tEnter Student First Name: ")
        lastName = input("\tEnter Student Last Name: ")
        username = input("\tEnter Student UserName: ")
        password = input("\tEnter Student Password: ")
        
        if write_csv(f"{self.DataDir}/students.csv", [firstName, lastName, username, password]):
            self.studentsData.append([firstName, lastName, username, password])
            print(f"\n\tSTUDENT ADDED SUCCESSFULLY")
            time.sleep(1.5)
            return True
        

    def add_course(self):
        while True:
            os.system("cls")
            print(f"\t{'#'*50}\n\t\t\tAdd Course\n\t{'#'*50}")
            CourseNumber = input("\n\tEnter Unique Course#: ")
            CourseTitle = input("\tEnter Course Title: ")
            
            Unique = False
            
            if len(self.coursesData)>0:
                if CourseNumber in [self.coursesData[x][0] for x in range(0, len(self.coursesData))]:
                    print("\n\tCOURSE ID ALREADY EXISTS IN DATABASE")
                    time.sleep(1.5)
            else:
                self.coursesData.append([CourseNumber, CourseTitle])
                write_csv(f"{self.DataDir}/courses.csv", [CourseNumber, CourseTitle])
                print("\n\tCOURSE ADDED SUCCESSFULLY..")
                time.sleep(1.5)
                break
                
    def add_enrollment(self):
            while True:
                os.system("cls")
                print(f"\t{'#'*50}\n\t\t\tAdd Enrollment\n\t{'#'*50}")

                studentUsername = input("\n\tEnter student username: ")
                courseNumber = input("\tEnter Course Number: ")
                
                if courseNumber in [self.coursesData[x][0] for x in range(0, len(self.coursesData))]:
                    if studentUsername in [self.studentsData[x][2] for x in range(0, len(self.studentsData))]:
                        self.enrollmentsData.append([studentUsername, courseNumber])
                        write_csv(f"{self.DataDir}/enrollments.csv", [studentUsername, courseNumber])
                        print("\n\tENROLLMENT ADDED SUCCESSFULLY..")
                        time.sleep(1.5)
                        break
                    else:
                        print("\n\tERROR! STUDENT WITH THIS USERNAME NOT FOUND")
                        time.sleep(1)
                else:
                    print("\n\tERROR! COURSE NOT FOUND")
                    time.sleep(1)           

    def view_students(self):
        os.system("cls")
        print(f"\t{'#'*50}\n\t\t\tView Student\n\t{'#'*50}")
        
        header = "Student Name".ljust(20) + "Username".ljust(20) + "Password".ljust(20)
        line = '-' * 50 
        print(f"\n\t{line}\n\t{header}\n\t{line}")
        
        for student in self.studentsData:
            print("\t{:<20} {:<20} {:<20}".format(student[0] + ' ' + student[1], student[2], student[3]))

        input("\n\tPress Enter:")

    def view_courses(self):
        os.system("cls")
        print(f"\t{'#'*50}\n\t\t\tView Courses\n\t{'#'*50}")
        
        header = "CourseID".ljust(20) + "Course Title".ljust(20)
        line = '-' * 40 
        print(f"\n\t{line}\n\t{header}\n\t{line}")
        
        for course in self.coursesData:
            if course: print("\t{:<20} {:<20}".format(course[0], course[1]))

        input("\n\tPress Enter:")

    def view_enrollments(self):
        os.system("cls")
        print(f"\t{'#'*50}\n\t\t\tView Enrollment\n\t{'#'*50}")
        
        header = "Student".ljust(20) + "CourseID".ljust(20)
        line = '-' * 40 
        print(f"\n\t{line}\n\t{header}\n\t{line}")
        
        for enrollment in self.enrollmentsData:
            if enrollment: print("\t{:<20} {:<20}".format(enrollment[0], enrollment[1]))

        input("\n\tPress Enter:")
    
    def DashBoard(self):
        while True:
            self.clearScreen("Admin DashBord")
            print("\n\t1: Add New Student")
            print("\t2: Add New Course")
            print("\t3: Add Course Enrollment")
            print("\t4: View All Student")
            print("\t5: View All Cources")
            print("\t6: View All Enrollments")
            print("\t7: Logout")
            
            choice = int(input("\n\tChoice (1-5): "))
            
            match choice:
                case 1:
                    self.add_student()
                case 2:
                    self.add_course()
                case 3:
                    self.add_enrollment()
                case 4:
                    self.view_students()
                case 5:
                    self.view_courses()
                case 6:
                   self.view_enrollments()
                case 7:
                   return True
                    
    def SETUP(self):
        self.adminsData = read_csv(os.path.join(self.DataDir, "admin_credentials.csv"))
        self.studentsData = read_csv(os.path.join(self.DataDir, 'students.csv'))
        self.coursesData = read_csv(os.path.join(self.DataDir, 'courses.csv'))
        self.enrollmentsData = read_csv(os.path.join(self.DataDir, 'enrollments.csv'))
        
        
if __name__ == "__main__":
    admin = AdminModule()