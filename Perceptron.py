"""------------------------------- PERCEPTRON MODEL -----------------------"""
def computeResult(v):
    if v>=0:
        return 1
    else: return 0



def Not(x,weight, bias):
    v = weight*x + bias
    result = computeResult(v)
    return result

def implementLogicGate(x,y,w1,w2,bias):
    temp= w1*x + w2*y + bias
    result = computeResult(temp)
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
        weight =  -1
        bias = 0.5
    elif ch==2:
        print("---------OR GATE---------")
        w1 =  1
        w2 =  1
        bias = -0.5
    elif ch==3:
        print("---------AND GATE---------")
        w1 =  1
        w2 = 1
        bias =  -1.5
    elif ch==4:
        print("---------NAND GATE---------")
        w1 =  -1
        w2 = -1
        bias = 1
    elif ch==5:
        print("---------NOR GATE---------")
        w1 =  -1
        w2 = -1
        bias = 0.5

    temp=-1
    
    if ch==1:
        print("(0)=",Not(0,weight,bias))
        print("(1)=",Not(1,weight,bias))
        
    else:
        for x,y in zip(X,Y):
            res=implementLogicGate(x,y,w1,w2,bias)
            print("(",x,y,")= ",res)
    return 0
    
if __name__ == "__main__":
    main()
