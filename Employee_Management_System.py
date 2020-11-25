# Project code
print("***************Enquiry System***************")

l=[]
def view_list():
    for i in l:
        print(f"\nname-->{i[0]} DOB-->{i[1]} Gmail-->{i[2]}")

def add_data():
    while True:
        x=input("\nenter your Name,DOB,Gmail : ").split(",")
        l.append(x)
        y=input("anymore yes/no : ")
        if y=='yes':
            pass
        else:
            break
def search_data():
    name=input("\n enter the name to search ")
    for i in l:
        if name==i[0]:
            print("Name Found!!!!")
            print(f"\nname-->{i[0]} DOB-->{i[1]} Gmail-->{i[2]}")
            break
    else:
        print("not found")

def end():
    print("\n please enter key to exit")
    exit()


while True:
    print("----------------------------------------------")
    print('                        ')
    print("Options are given please choose any:")
    print("\n1. Add data")
    print("2. View data")
    print("3. Search data")
    print("4. exit")
    ch=input("\nenter the option: ")
    if ch=='1':
        add_data()
    elif ch=='2':
        view_list()
    elif ch=='3':
        search_data()
    elif ch=='4':
        end()
    else:
        print("Wrong Input")


