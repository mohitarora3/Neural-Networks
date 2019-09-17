"""------------------------------- MCP Model -----------------------"""
def computeResultMCP(v,theta):
    if v>=theta:
        return 1
    else: 
        return 0



def NOT(x):
    if(x==0):
        result = computeResultMCP(x,0)
    else:
        result = computeResultMCP(x,2)
    return result

def AND(x,y):
    Sum= x + y 
    result = computeResultMCP(Sum,2)
    return result

def OR(x,y):
    Sum= x + y 
    result = computeResultMCP(Sum,1)
    return result

def NAND(x,y):
    result = NOT(AND(x,y))
    return result

def NOR(x,y):
    result=NOT(OR(x,y))
    return result




def main():
    print("--------Perceptron Model---------")
    X = (0,0,1,1)
    Y = (0,1,0,1)
    
    print(" 1.NOT \n 2.OR \n 3.AND \n 4.NAND \n 5.NOR")
    ch = input("Please enter your choice: ")
    ch = int(ch)
   
    if ch==1:
        print("---------NOT GATE---------")
        print("(0)=",Not(0))
        print("(1)=",Not(1))
 
    elif ch==2:
        print("---------OR GATE---------")
        for x,y in zip(X,Y):
            res=OR(x,y)
            print("(",x,y,")= ",res)
    
    elif ch==3:
        print("---------AND GATE---------")
        for x,y in zip(X,Y):
            res=AND(x,y)
            print("(",x,y,")= ",res)
    elif ch==4:
        print("---------NAND GATE---------")
        for x,y in zip(X,Y):
            res=NAND(x,y)
            print("(",x,y,")= ",res)
        
    elif ch==5:
        print("---------NOR GATE---------")
        for x,y in zip(X,Y):
            res=NOR(x,y)
            print("(",x,y,")= ",res)
    else:
        print("\nInvalid Input!!")
    
if __name__ == "__main__":
    main()
