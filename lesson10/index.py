import learning
def main():
    p1=learning.getperson(name="徐國堂")
    print(p1.bmi_print())
    print("==========")
    p2=learning.Person.getperson(name="robert")
    print(p2.bmi_print())
    print("==========")
    p3=learning.Person.getperson1(name="Alice")
    print(p3.bmi_print())
if __name__ == '__main__':
    main()