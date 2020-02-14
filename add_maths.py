import math

class general:
    def find_x(a,b,c):
        if (b**2-4*c>=0) and a==1:
            x1=-((-b)+(math.sqrt((b**2)-4*c)))/(2)
            x2=-((-b)-(math.sqrt((b**2)-4*c)))/(2)
            if x1==x2:
                return "x={}".format(x1)
            else:
                return "x={} or x={}".format(x1,x2)
        elif (b**2-4*a*c>=0) and a!=1:
            x1=((-b)+(math.sqrt((b**2)-(4*a*c))))/(2*a)
            x2=((-b)-(math.sqrt((b**2)-(4*a*c))))/(2*a)
            if x1==x2:
                return "x={}".format(x1)
            else:
                return "x={} or x={}".format(x1,x2)
        else:
            return "no root"

    def cts(a,b,c):
        if a==1:
            z=(-(b/2)**2)+c
            if z>=0:
                if b/2>=0:
                    end="(x + {})^2 + {}".format(b/2,z)
                else:
                    end="(x - {})^2 + {}".format(-b/2,z)
            else:
                if b/2>=0:
                    end="(x + {})^2 - {}".format(b/2,-z)
                else:
                    end="(x - {})^2 - {}".format(-b/2,-z)
            
            return end

        else:
            z=a*(-(b/a/2)**2+(c/a))
            if z>=0:
                if b/a/2>=0:
                    end="{}(x + {})^2 + {}".format(a,b/a/2,z)
                else:
                    end="{}(x - {})^2 + {}".format(a,-b/a/2,z)
            else:
                if b/a/2>=0:
                    end="{}(x + {})^2 - {}".format(a,b/a/2,-z)
                else:
                    end="{}(x - {})^2 + {}".format(a,-b/a/2,-z)
                    
            #end="{}(x + {})^2 + {}".format(a,b/a/2,z)
            return end

user_input=input("(1) Solve\n(2) Completing the square\n")
while user_input!="q":
    if user_input=="1":
        print("ax^2 + bx + c")
        a=float(input("a: "))
        b=float(input("b: "))
        c=float(input("c: "))
        print(general.find_x(a,b,c),"\n")
    elif user_input=="2":
        print("ax^2 + bx + c")
        a=float(input("a: "))
        b=float(input("b: "))
        c=float(input("c: "))
        print(general.cts(a,b,c),"\n")
    else:
        print("Error: Please enter 1, 2 or q\n")
    user_input=input("(1) Find x\n(2) Completing the square\n")
        
