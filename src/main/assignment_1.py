import math;

# Approximation Algorithm 
def ApproximationAlgorithm():
    x0=float(input("Enter starting point.\n"));
    tol=float(input("Enter tolerance value.\n"));

    iter=0;
    diff=x0;
    x=x0;

    print(str(iter)+" : "+str(x)+"\n");

    while(diff >= tol):
        iter=iter+1;
        y=x;

        x= (x/2)+(1/x);
        print(str(iter)+" : "+str(x));

        diff=math.fabs(x-y);

    print("\nConvergence after "+str(iter)+" iterations.\n");
approx=ApproximationAlgorithm();


# The bisection Method
def BisectionMethod():
    i=0;
    tol=float(input("Enter desired error tolerance.\n"));
    left=float(input("Enter left starting endpoint.\n"));
    right=float(input("Enter right starting endpoint.\n"));
    max=int(input("Enter maximum number of iterations.\n"));
    while (math.fabs(right-left)>tol and i<max):
        i=i+1;
        p=(left+right)/2

        if((f(left)<0 and f(p)>0) or (f(left)>0 and f(p)<0)):
            right=p;
        else:
            left=p;
# Example of f function (can be any function)
def f(x):
    return x**2 - 2;
root = BisectionMethod();
print("Approximated root: "+str(root)+"\n");


# The fixed-point Iteration 
def FixedPoint():
    p0=float(input("Enter your initial approximation.\n"));
    tol=float(input("Enter your error tolerance.\n"));
    n0=float(input("Enter your maximum number of iterations.\n"));

    i=1;
    while(i<=n0):
        p=g(p0);
        if(math.fabs(p-p0)<tol):
            print(str(p)+"SUCCESS");
            return;
        i=i+1;
        p0=p;
    print("FAILURE");
    return;
# Example of g function (can be any function)
def g(x):
    return x*x*x+4*x*x-10;
point=FixedPoint();
print("Fixed point: "+str(point)+"\n");
    

# The Newton-Raphson method 
def NewtonRaphson() :
    p_prev=float(input("Enter your initial approximation.\n"));
    tol=float(input("Enter your desired tolerance.\n"));
    n0=int(input("Enter our maximum number of iterations.\n"));

    i=1;
    while(i<=n0):
        if(f_deriv(p_prev)!=0):
            p_next=p_prev-f(p_prev)/f_deriv(p_prev);
            if(math.fabs(p_next-p_prev)<tol):
                print("SUCCESS\n"+str(p_next));
                return;
            i=i+1;
            p_prev=p_next;
        else:
            print("FAILURE (derivative is 0)");
            return;
    print("Unsuccessful (max iterations performed)");
    return;
#Examples of f and f' functions (can be replaced with any function)
def f(x):
    return math.cos(x)-x;
def f_deriv(x):
    return -math.sin(x)-1;
newton=NewtonRaphson();
