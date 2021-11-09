import math

class Number:

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def input_info(self):
        print(self.n1, self.n2)

    def addition(self):
        print(self.n1 + self.n2)

    def subtract(self):
        print(self.n1 - self.n2)

    def multi(self):
        print(self.n1*self.n2)
    
    def division(self):
        print(self.n1 /self.n2)



class Prime:
    def __init__(self,x):
        self.x = x

    def isPrime(self):
        if (self.x<2): return False
        for i in range (2, int(math.sqrt(self.x))+1):
            if (self.x%i==0): return False
        return True

    def next_prime(self):
        a = self.x+1
        while(True):
            tmp = Prime(a)
            if(tmp.isPrime()==True):
                print(a)
                break
            a+=1
    
class Circle:
    def __init__(self,x,R):
        self.x = x
        self.R = R

    def describe(self):
        print(f"O({self.x[0]},{self.x[1]}) bán kính = {self.R}")

    def get_area(self):
        print(math.pi*math.pi*self.R)

    def get_perimeter(self):
        print(math.pi*2*self.R)
    
    
class CheckNumber(Number):
    def __init__(self, n1, n2):
        super().__init__(n1, n2)
        
    def __init__(self, n1):
        self.n1 = n1

    def parity_check(self):
        if(self.n1 %2 ==0) : print("Chan")
        else: print("le")

    def is_prime(self):
        if(Prime(self.n1).isPrime() == True): print("SNT")
        else: print("Not SNT")

    def is_perfect(self):
        s = 0 
        for i in range (1,self.n1):
            if(self.n1%i==0): s+=i
        if (s==self.n1): print("perfect")
        else: print("Not perfect")
    
    def is_square(self):
        if ((int(math.sqrt(self.n1)))**2 == self.n1 ): print("Square")
        else: print("Not square")


a = CheckNumber(11)
a.parity_check()
a.is_prime()
a.is_perfect()
a.is_square()