def searchname():
    infile=open("names.txt","r")
    for s in infile:
        print(s)
def searchname():
    infile=open("names.txt","r")
    for s in infile:
        print(s[:-1])
def search(d):
    infile = open("names.txt", "r")
    for s in infile:
        if(s[0]==d):
            print(s)
def searchage(age):
    infile=open("names.txt","r")
    for s in infile:
        if age in s:
            print (s)

if __name__ == "__main__":
    print("""
        1.Search by name
        2.Search by Age
        """)
    ans =int (input("What would you like to do? "))
    if ans==1:
        s=(str(input("enter the  first charater:"))).upper()
        search(s)
    elif ans==2:
        age=str(input("enter the  age:"))
        searchage(age)
    else:
        print("\n Not Valid Choice Try again")

