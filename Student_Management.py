import sqlite3 # /// Student Management ///
try:
    db = sqlite3.connect("Student.db")

    db.execute('''create table IF NOT EXISTS Student(
            name varchar(50),
            id int primary key,
            age int,
            course varchar(10),
            marks int) ''')
except Exception as e:
            print(e)

def Ask_user():    #returns ch
    print()
    print(f"Welcome to Management System\n{'-'*30}")
    ch = int(input("1.Add New Student\n2.Search Student\n3.Update Student Details\n4.Delete Student Details\n5.Show top marks Students\n6.Exit\nEnter Your choice : "))
    return ch

def add_student():
    name = input("Enter Student Name :")
    id = int(input("Enter Student ID :"))
    age  = int(input("Enter Student Age :"))
    course = input("Enter Student Course Name :")   
    marks = int(input("Enter Student Marks :"))

    try:
        db.execute("insert into student (name,id,age,course,marks) values (?,?,?,?,?)",(name,id,age,course,marks))
        db.commit()
        print("Student Data Added Successfully...")
    except Exception as e:
            print(e)

def search_student():
    try:
        def print_as_table(data):
            if not data:
                print("No data found!")
                return
    
            print("-"*66)
            print(f"|{'Name':^12}|{'ID':^12}|{'Age':^12}|{'Course':^12}|{'Marks':^12}|")
            print("-"*66)
            for i in data:
                print(f"|{i[0]:^12}|{i[1]:^12}|{i[2]:^12}|{i[3]:^12}|{i[4]:^12}|")
            print("-"*66)
            print()

        def by_name():
            name = input("Enter Student Name :")
            data = db.execute('select * from student where name = ?',(name,))
            print_as_table(data)
        
        def by_id():
            id = input("Enter Student ID :")
            data = db.execute('select * from student where id = ?',(id,))
            print_as_table(data)

        def by_age():
            age = input("Enter Student Age :")
            data = db.execute('select * from student where age = ?',(age,))
            print_as_table(data)

        def by_course():
            course = input("Enter Student Course :")
            data = db.execute('select * from student where course = ?',(course,))
            print_as_table(data)

        def by_marks():
            marks = input("Enter Student Marks :")
            data = db.execute('select * from student where marks = ?',(marks,))
            print_as_table(data)

        def show_all():
            data = db.execute('select * from student;')
            print_as_table(data)
        while True:
            ch = int(input("1.Search By Name\n2.Search By ID\n3.Search By Age\n4.Search By Course\n5.Search By Marks\n6.Show All Students Data\n7.Go To Main Menu\n8.Exit\nEnter your Choice :"))
            
            match ch:
                case 1:
                    by_name()
                
                case 2:
                    by_id()
                
                case 3:
                    by_age()
                
                case 4:
                    by_course()
                
                case 5:
                    by_marks()
                
                case 6:
                    show_all()

                case 7:
                    return
                
                case 8:
                    db.close()
                    exit("Thank you for using the application!")
                
                case _:
                    print("Invalid Choice !!")
    except Exception as e:
        print(e)

def update():
    try:
     
        id = int(input('Enter Student ID To Update Details :'))
        ch = int(input('1.Change Student Name\n2.Change Student Age\n3.Change Student Course\n4.Change Student Marks\n5.Go To Main Menu\n6.Exit\nEnter Your Choice :'))
        def updata_Function(udata,wdata): # udata => Update_Data ,wdata => Which_Data   
            query = f'''update student
                    set {wdata} = ?
                    where id = ?;'''
            
            db.execute(query,(udata,id))
            db.commit()
            print(f"{wdata} Updated Successfully With {udata}")

        def change_name():
            udata = str(input("Enter New Name :"))
            updata_Function(udata,'name')

        def change_age():
            udata = int(input("Enter New Age :"))
            updata_Function(udata,'age')
        
        def change_course():
            udata = input("Enter New Course Name :")
            updata_Function(udata,'course')

        def change_marks():
            udata = int(input("Enter New Marks :"))
            updata_Function(udata,'marks')

        match ch:
            case 1:
                change_name()
                
            case 2:
                change_age()

            case 3:
                change_course()

            case 4:
                change_marks()

            case 5:
                return
            
            case 6:
                db.close()
                exit("Thank you for using the application!")

            case _:
                print("Invalid Choice !!")

    except Exception as e:
        print(e)

def delete():
    try:
        id = int(input("Enter Student ID To Delete :"))
        confirm = input(f"Are you sure you want to delete Student ID {id}? (yes/no): ").strip().lower()
        if confirm == "yes":
            db.execute("delete from student where id = ?;",(id,))
            db.commit()
            print(f"Student with ID {id} deleted successfully.")
        else:
            print("Deletion cancelled.")
    except Exception as e:
        print(e)

def top_marks():
    try:
        data = db.execute("select id,name,marks from student order by marks desc limit 5;")
        print("-"*40)
        print(f"|{'ID':^12}|{'Name':^12}|{'Marks':^12}|")
        print("-"*40)
        for i in data:
            print(f"|{i[0]:^12}|{i[1]:^12}|{i[2]:^12}|")
        print("-"*40)
    except Exception as e:
        print(e)

def main():
    while True:
        try:
            ch = Ask_user()
            match ch:
                case 1:
                    add_student()
                case 2:
                    search_student()
                case 3:
                    update()
                case 4:
                    delete()
                case 5:
                    top_marks()
                case 6:
                    db.close()
                    exit("Thank you for using the application!")
                case _:
                    print("Invalid Choice !!")
        except Exception as e:
            print(e)   

if __name__ == "__main__":
    main()
    db.close()