
from admin import *
from student import *

class User:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.LoginAttempts = 0

    def AdminLogin(self):
        print(f"\t{'#'*50}\n\t\t\tAdmin Login\n\t{'#'*50}")
        admin = AdminModule()
        if admin.authenticate_admin():
            admin.DashBoard()
    
    def StudentLogin(self):
        student = StudentModule()
        result = student.authenticate_student()
        print(result)
        student.DashBoard(result)


if __name__ == "__main__":
    
    User = User()
    
    
    while True:
        os.system("cls")
        print(f"\t{'#'*50}\n\t\t\tStudent DashBord\n\t{'#'*50}") 
        print("\n\t1: Admin Login")
        print("\t2: Student Login")
        print("\t3: Exit")
        
        choice = int(input("\n\tChoice (1-2): "))
        
        match choice:
            case 1:
                User.AdminLogin()
            case 2:
                User.StudentLogin()
            case 3:
                print("\n\tGOOD BYE!")
                time.sleep(1)
                os.system("cls")
                break

