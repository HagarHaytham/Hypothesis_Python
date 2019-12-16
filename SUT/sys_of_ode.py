import numpy as np
import matplotlib.pyplot as plt
from sympy import integrate,Symbol
from math import *

round_list = lambda some_list,digits : [round(elem,digits) for elem in some_list]

def read_input(method):
    n = int(input("Enter number of equations: "))
    print("Enter equations as python format ex: -2*x**3 + exp(x)-20*x + 8.5")
    print("Note That y0 is the name of variable. two equations ex:\n 1-> dy0/dx = 3*x*y1 + 2*y0\n 2-> dy1/dx = x + y1 + y0\n")
    eqs = [input("eq{0}: dy{0}/dx = ".format(i)) for i in range(n)]
    print("\nIntial values for variables")
    xi = float(input("x_initial = "))
    xf = float(input("x_final = "))  
    h = float(input("calculation step size h = "))
    if(method=='0'): #euler
        ys = {} # Intial values for variables
        for i in range(n):
            try:
                ys['y{0}'.format(i)] = float(input("y{0}_intial = ".format(i)))
            except: pass
        test_equations(eqs,ys.copy()) # testing input of equations
        xout = input("show output every step (for default = h press Enter) = ")
        xout = float(xout) if xout != '' else h
        return eqs,ys,xi,xf,h,xout
    else:#miline
        xs = [xi+i*h for i in range(5)]
        ys = []
        for j in range(4):
            tmp={}
            for i in range(n):
                try:
                    tmp['y'+str(i)] = float(input("y{0} at x = {1} = ".format(i,round(xs[j],3))))
                except: pass
            ys.append(tmp.copy())
        test_equations(eqs,ys[0].copy()) # testing input of equations
        its = input("num of iterations for correction (if not defined press Enter) = ")
        its = int(its) if its != '' else -1
        stopping_err = input("Presantage of relative stopping error (if not defined press Enter) = ")
        stopping_err = float(stopping_err) if stopping_err != '' else -1
        if(its==-1 and stopping_err==-1):
            print("No stopping criteria defined Set iterations to default 10")
            its = 10
        return eqs,ys,xs,h,xf,its,stopping_err 

def test_equations(eqs,variables):
    variables['x']=1
    try:
        for eq in eqs:
            eval(eq,globals(),variables)
    except:
        print("wrong equations or intial variables")
        exit()

#--------------------------------
def predictor(ys,h,xs,eqs):
    predictions = []
    for i in range(len(eqs)):
        y_3 = ys[0]['y'+str(i)]
        ys[1]['x'] = xs[1]
        diff_y_2 = eval(eqs[i],globals(),ys[1])
        ys[2]['x'] = xs[2]
        diff_y_1 = eval(eqs[i],globals(),ys[2])
        ys[3]['x'] = xs[3]
        diff_y_0 = eval(eqs[i],globals(),ys[3])
        predictions.append(y_3 + 4/3*h*(2*diff_y_0 - diff_y_1 + 2*diff_y_2))
    print("Predictions")
    print(round_list(predictions,5))
    return predictions

def corrector(predictions,ys,h,xs,eqs,its,stopping_err):
    print("Corrections and maximum approximate error %")
    result = []
    tmp={}
    for i in range(len(predictions)):
        tmp['y'+str(i)] = predictions[i]
    ys.append(tmp)
    approx_errs = [100.]*len(predictions)
    it=0
    while((it<its or its==-1) and (max(approx_errs)>stopping_err or stopping_err==-1)):
        for i in range(len(eqs)):
            y_1 = ys[2]['y'+str(i)]
            ys[2]['x'] = xs[2]
            diff_y_1 = eval(eqs[i],globals(),ys[2])
            ys[3]['x'] = xs[3]
            diff_y_0 = eval(eqs[i],globals(),ys[3])
            ys[4]['x'] = xs[4]
            diff_y_plus1 = eval(eqs[i],globals(),ys[4])
            new_y =  y_1 +1./3*h*(diff_y_1+4*diff_y_0+diff_y_plus1)
            approx_errs[i]=(new_y-predictions[i])/new_y*100
            predictions[i] = new_y
            ys[4]['y'+str(i)] = predictions[i]
        it+=1
        print(round_list(predictions + [max(approx_errs)],5))

        result.append(predictions + [max(approx_errs)])
    return result

def solve_miline(eqs,ys,xs,h,xf,its,stopping_err):
    points=[]
    for i in range(4):
        points.append(round_list([xs[i]] + [ys[i]['y'+str(j)] for j in range(len(eqs))],5))
    while(xs[-1]<=xf):
        print("\nSolve at x = {0}".format(xs[-1]))
        predictions = predictor(ys,h,xs,eqs)
        result = corrector(predictions,ys,h,xs,eqs,its,stopping_err)
        points.append(round_list([xs[-1]] + result[-1][:-1],5))
        #shifting problem one step
        xs.append(xs[-1]+h)
        xs.pop(0)
        tmp={}
        for i in range(len(eqs)):
            tmp['y'+str(i)] = predictions[i]
        ys.append(tmp)
        ys.pop(0)
        print('')

    print("All points x ,y0 ,y1 ...")
    points=np.array(points)
    print(points)
    return points

#-----------------------------------------------------------------------------------
dict_to_list = lambda some_dict:[ some_dict[key] for key in sorted(some_dict.keys())]
euler = lambda y,vars,h,eq : y + eval(eq,globals(),vars.copy())*h

def integrator(x,ys,h,xend,eqs):
    while(1):
        if(xend -x <h):
            h = xend -x
        new_ys = ys.copy()
        for i in range(len(eqs)):
            variables = ys.copy();variables['x'] =x #use the prev x not the curr one
            new_y = euler(ys['y{0}'.format(i)],variables,h,eqs[i])
            new_ys['y{0}'.format(i)] = new_y
        ys.update(new_ys) 
        x=x+h    
        if(x>= xend):
            return x


def plot_points(points):
    legends = []
    for i in range(len(points[0])-1):
        plt.scatter(points[:,0],points[:,i+1])
        legends.append('y'+str(i))
    plt.legend(legends, loc='upper left')
    plt.show()

def solve_euler(eqs,ysi,xi,xf,h,xout):
    result_table = [xi] + dict_to_list(ysi)
    points = []
    points.append(round_list([xi] + [ ysi['y'+str(j)] for j in range(len(eqs))],5))
    while(1):
        xend = xi + xout
        if(xend > xf):
            xend = xf
        xi = integrator(xi,ysi,h,xend,eqs) # ysi dictionary is passed by ref
        new_row = round_list( [xi] + dict_to_list(ysi),5)
        points.append(new_row)
        if(xi>=xf):
            break

    points=np.array(points)
    print(points)
    return points

def main():
    method = input("Enter method euler =0 miline =1 : ")
    points = None
    if(method=='0'):
        eqs,ysi,xi,xf,h,xout = read_input('0') # i for initial and f for final and out for output_interval
        points = solve_euler(eqs,ysi,xi,xf,h,xout); #points holds x,ys,approximate error
    elif(method=='1'):
        eqs,ys,xs,h,xf,its,stopping_err = read_input('1') # i for initial and f for final and out for output_interval
        points = solve_miline(eqs,ys,xs,h,xf,its,stopping_err);#points holds x,ys,approximate error
    
    plot_points(points);#no need for this graph

if __name__ == "__main__":
    main()




'''
Program starts to know which method 0 for euler 1 for miline
both method will use same function read_input based on method (input differs a little bit)
in both methods user should enter number of equations n

0 euler
euler input explanation
    1- eqs -> equations writtien as string in python format
        two equations input example:
            1-> dy0/dx = 3*x*y1 + 2*y0
            2-> dy1/dx = x + y1 + y0
        note that y0 is x y1 are names of variable dy0/dx means derivative of y0 w.r.t x and y0 is the exact value
    2- h -> step size in euler this is increments on x intial to start new value for each equation for each x till xf(final x)
    3- xi -> x intial this is where user write intial values for (y0,y1,..yn) then start solving till xf (geting y0 ,y1,..yn at each x from xi+h to xf increments by h)
    4- xf -> last x to solve equations at (get y0 ,y1,..yn at each x from xi+h to xf increments by h) 
    #then user start intial values for each y (y0,y1,..yn) at xi
    5- xout -> (defualt = h) this to determine eother to show ouput every h 
        or evry bigger step size equals to xout(this useful when h is too small)
        this output is not necessary can be left to empty string

1 miline's method
miline's method input explanation
    1- eqs -> same as euler
    2- h -> step size in miline's method indicates number of points to solve equations at from 5th x after xi to xf
    3- xi -> note that for first 4 xs user should enter intial values for intial (y0,y1,...yn) xi is the first one of 4 xs (increments with h step size)
    4- xf -> last x to solve equations at (get y0 ,y1,..yn at each x from xi+3h to xf increments by h) 
    #then user start intial values for each y (y0,y1,..yn) for first 4 xs form xi to xi+3h
    5- its -> number of iterations in corrector
    6- stopping_errr -> relative stopping error in percentage
    #for each point to calc (y0,y1,..yn)  at corrector stops after its iterations or till reaching stopping error

'''

'''
def read_input_miline():
    n = int(input("Enter number of equations: "))
    print("Enter equations as python format ex: -2*x**3 + exp(x)-20*x + 8.5")
    print("Note That y0 is the name of variable 2 equations ex:\n 1-> dy0/dx = 3*x*y1 + 2*y0\n 2-> dy1/dx = x + y1 + y0\n")
    eqs = [input("eq{0}: dy{0}/dx = ".format(i)) for i in range(n)]
    print("\nIntial values for variables")
    h = float(input("step size h = "))
    xi = float(input("start form x = "))
    xf = float(input("till reach x = "))
    xs = [xi+i*h for i in range(5)]
    ys = []
    for j in range(4):
        tmp={}
        for i in range(n):
            try:
                tmp['y'+str(i)] = float(input("y{0} at x = {1} = ".format(i,round(xs[j],3))))
            except: pass
        ys.append(tmp.copy())
    test_equations(eqs,ys[0].copy()) # testing input of equations
    its = input("num of iterations for correction (if not defined press Enter) = ")
    its = int(its) if its != '' else -1
    stopping_err = input("Presantage of relative stopping error (if not defined press Enter) = ")
    stopping_err = float(stopping_err) if stopping_err != '' else -1
    if(its==-1 and stopping_err==-1):
        print("No stopping criteria defined Set iterations to default 10")
        its = 10
    return eqs,ys,xs,h,xf,its,stopping_err


def read_input_euler():
    n = int(input("Enter number of equations: "))
    print("Enter equations as python format ex: -2*x**3 + exp(x)-20*x + 8.5")
    print("Note That y0 is the name of variable 2 equations ex:\n 1-> dy0/dx = 3*x*y1 + 2*y0\n 2-> dy1/dx = x + y1 + y0\n")
    eqs = [input("eq{0}: dy{0}/dx = ".format(i)) for i in range(n)]
    print("\nIntial values for variables")
    ys = {} # Intial values for variables
    for i in range(n):
        try:
            ys['y{0}'.format(i)] = float(input("y{0}_intial = ".format(i)))
        except: pass
    test_equations(eqs,ys.copy()) # testing input of equations
    xi = float(input("x_initial = "))
    xf = float(input("x_final = "))
    dx = float(input("calculation step size h = "))
    xout = input("show output every step (for default = h press Enter) = ")
    xout = float(xout) if xout != '' else dx
    intial_conditions=ys.copy();intial_conditions['x']=xi
    return eqs,ys,xi,xf,dx,xout
'''
#miline
'''
Test Case 
2
y1-x*y0
1/3*(1+x**2-2*y0)
0
.7
.1
1
2
1.56
2.39
3.06
1.332
y1-x*y0
1/3*(1+x**2-2*y0)
0
.7
.1
1
2
1.56
2.39
3.06
1.33
2.42
.86
10
2.42
.86
10
output
3.09556 1.050099
'''

#-----------------------------------------------------
#Euler
'''
Test Case one equation
1
-2*x**3+12*x**2-20*x+8.5
0
4
.5
1
'''

'''
Test Case two equation
2
-.5*y0
4-.3*y1-.1*y0
0
2
.5
4
6
'''
