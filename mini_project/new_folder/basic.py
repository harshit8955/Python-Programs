name=input("Enter your name: ")
course=input("Enter your course: ")
mobile=input("Enter your mobile number: ")
id=input("Enter your id: ")
email=input("Enter your email: ")
print("|Name   :"   , name     ,"|")
print("-"*30)
print("|Course :"   , course   ,"|")
print("-"*30)
print("|Mobile :"   , mobile   ,"|")
print("-"*30)
print("|ID     :"   , id       ,"|")
print("-"*30)
print("|Email  :"   , email    ,"|")
print("-"*30)

ls=[]
for i in range(0,101, 2):
    ls.append(i)
    print(ls) 
    
    
st="Python"
for i in st:
    print(i)
    st.append(i)
