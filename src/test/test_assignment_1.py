import math;

# Original main requires input, which can also be used for testing cases
# Approximation Algorithm 
def ApproximationAlgorithm(x0, tol):
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
approx=ApproximationAlgorithm(1.5, 0.001);
approx2=ApproximationAlgorithm(7, 0.000001);
approx3=ApproximationAlgorithm(3, 0.01);


# The bisection Method
def BisectionMethod(tol, left, right, max):
    i=0;
    while (math.fabs(right-left)>tol and i<max):
        i=i+1;
        p=(left+right)/2

        if((f(left)<0 and f(p)>0) or (f(left)>0 and f(p)<0)):
            right=p;
        else:
            left=p;
    return p;
# Example of f function (can be any function)
def f(x):
    return x**2 - 2;
root = BisectionMethod(0.001, 1, 2, 20);
print("Approximated root: "+str(root)+"\n");
root2 = BisectionMethod(0.000001, 3, 7, 45);
print("Approximated root: "+str(root2)+"\n");
root3 = BisectionMethod(0.01, 0, 12, 100);
print("Approximated root: "+str(root3)+"\n");


# The fixed-point Iteration 
def FixedPoint(p0, tol, n0):
    i=1;
    while(i<=n0):
        p=g(p0);
        if(math.fabs(p-p0)<tol):
            print(str(p)+"\nSUCCESS\n");
            return;
        i=i+1;
        p0=p;
    print("\nFAILURE\n");
    return;
# Example of g function (can be any function)
def g(x):
    return (x+7)/4;
point=FixedPoint(0.9, 0.1, 100);
point2=FixedPoint(0.8, 0.1, 100);
point3=FixedPoint(0.7, 0.1, 100);
    

# The Newton-Raphson method 
def NewtonRaphson(p_prev, tol, n0) :
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
newton=NewtonRaphson(0.789, 0.000001, 20);
newton2=NewtonRaphson(1.5, 0.01, 20);
newton3=NewtonRaphson(0.9, 0.001, 15);
