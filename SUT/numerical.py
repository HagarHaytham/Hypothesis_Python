#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 18:49:30 2018

@author: Haneen
"""

import kivy
kivy.require('1.10.1')
#kivy imports
#from kivy.app import App
#from kivy.uix.screenmanager import ScreenManager, Screen
#from kivy.lang import Builder
#
#from kivy.config import Config
#Config.set('graphics', 'width', '800')
#Config.set('graphics', 'height', '1100')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.textinput import TextInput
#from kivy.uix.recycleview import RecycleView

#our imports
import numpy as np
from math import pi
#from kivy.core.text import LabelBase
#import emoji

#LabelBase.register(name = "Bigfish", fn_regular = "Bigfish.ttf")

#codes import
from eigen import powerMethod, deflate
from linear import SolveGaussSeidel, SolveSOR
from nonlinear import NonLinearSolver
from SODE import SolveODE
from curve import curve_fitting
#from intrp import interpolateNewton, interpolationLagrange
from interpolation import interpolateNewton, interpolationLagrange
from gInteg import Integration_GaussLegendre
from integ import trapezoidal,simpson_3_8,simpson_1_3
from rungeODE import Runge_kutte_ODE
from pdODE import PredictorCorrector
from euler import Euler, heun
#from richard import Rich
from Richardson import Rich
from interpThenDiff import newtonGeneral
#from 
#from heunODE import     ESRAAA



def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def RepresentsFloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

def RepresentsArr(s):
    for i in range(len(s)):
        try:
            float(s[i])
            return True
        except ValueError:
            return False
        
        
class MainScreen(Screen):
    print(pi)
    
class InPDSScreen(Screen):
    pass

class InEulerScreen(Screen):
    def okEButton(self):
        if not RepresentsFloat(self.ids.xnod.text) or not RepresentsFloat(self.ids.ynod.text) or not RepresentsFloat(self.ids.xf.text)\
        or not RepresentsInt(self.ids.n.text):
            raise TypeError("Input Error")
        Euler(self.ids.calc.ids.entry.text, float(self.ids.xnod.text), float(self.ids.ynod.text), float(self.ids.xf.text), int(self.ids.n.text))
        print(self.ids.calc.ids.entry.text, type(self.ids.calc.ids.entry.text), float(self.ids.xnod.text))
    def okHButton(self):
        if not RepresentsFloat(self.ids.xnod.text) or not RepresentsFloat(self.ids.ynod.text) or not RepresentsFloat(self.ids.h.text):
            raise TypeError("Input Error")
        heun(self.ids.calc.ids.entry.text, float(self.ids.xnod.text), float(self.ids.ynod.text), float(self.ids.h.text))
        print(self.ids.calc.ids.entry.text, type(self.ids.calc.ids.entry.text), float(self.ids.xnod.text), float(self.ids.ynod.text), float(self.ids.h.text))

class InPCScreen(Screen):
    def okButton(self):
        if not RepresentsArr(self.ids.xs.text) or not RepresentsArr(self.ids.ys.text) or not RepresentsArr(self.ids.xsolv.text)\
        or not RepresentsFloat(self.ids.err.text):
            print(RepresentsArr(self.ids.xs.text), RepresentsArr(self.ids.ys.text), RepresentsArr(self.ids.xsolv.text), RepresentsFloat(self.ids.err.text))
#            raise TypeError("Input Error")
        xs = self.ids.xs.text
        xs = xs.split()
        ys = self.ids.ys.text
        ys = ys.split()
        self.xlist = list()
        self.ylist = list()
        for i in range(len(xs)):
            self.xlist.append(float(xs[i]))
            self.ylist.append(float(ys[i]))
        xsolv = self.ids.xsolv.text
        xsolv = xsolv.split()
        self.xslist = list()
        for i in range(len(xsolv)):
            self.xslist.append(xsolv[i])
    
    def okMButton(self):
        self.okButton()
        self.string = "Milne's"
        self.solve()
    
    def okABButton(self):
        self.okButton()
        self.string = "AdamsBashforth"
        self.solve()
    
    def okAMButton(self):
        self.okButton()
        self.string = "AdamsMoulton"
        self.solve()
    
    def okAButton(self):
        self.okButton()
        self.string = "Adams"
        self.solve()
        
    def solve(self):
        ans = PredictorCorrector(self.xlist, self.ylist, self.ids.calc.ids.entry.text, self.string, self.xslist, float(self.ids.err.text))
        self.ids.ysolv.text = str(ans[0])
        self.ids.yerr.text = str(ans[1])
        self.ids.apperr.text = str(ans[2])

class InEigScreen(Screen):
    A = np.zeros((1,1))
    init = np.zeros((1,1))
    err = float()
    def okButton(self):
        if not RepresentsInt(self.ids.matn.text) or not RepresentsArr(self.ids.initial_vec.text) or \
        not RepresentsArr(self.ids.mat.text):
            raise TypeError("Input Error")
        n = int(self.ids.matn.text)
        mat = self.ids.mat.text
        mat = mat.split()
        if len(mat) != n*n:
            raise TypeError("Mat Size Error")
        self.A = np.zeros((n,n))
        for i in range(n):
            for j in range(n):
                self.A[i][j] = float(mat[i*n+j])
        vals = self.ids.initial_vec.text
        vals = vals.split()
        self.init = np.zeros(int(self.ids.matn.text))
        for i in range(int(self.ids.matn.text)):
            self.init[i] = vals[i]
        if self.ids.iter.text == "" or not RepresentsInt(self.ids.iter.text):
            self.ids.iter.text = "100"
        if self.ids.err.text == "":
            self.err = 0
        else:
            self.err = float(self.ids.err.text)
                
    def lamdaMinButton(self):
        self.okButton()
        ans = powerMethod(self.A, self.init, None, int(self.ids.iter.text), True)
        print(ans)
        self.ids.lmin.text = str(ans[0])
        self.ids.vecmin.text = str(ans[1])
        self.ids.errmin.text = str(ans[2])
        
    def lamdaMaxButton(self):
        self.okButton()
        ans = powerMethod(self.A, self.init, None, int(self.ids.iter.text), False)
        print(ans)
        self.ids.lmax.text = str(ans[0])
        self.ids.vecmax.text = str(ans[1])
        self.ids.errmax.text = str(ans[2])
        
    def defButton(self):
        self.okButton()
        ans = deflate(self.A, self.init, None, int(self.ids.iter.text))
        print(ans)
        self.ids.deflate.text = str(ans[0])
        self.ids.errb.text = str(ans[3])
            
class InCrvScreen(Screen):
    def okButton(self):
        if not RepresentsArr(self.ids.xs.text) or not RepresentsArr(self.ids.ys.text)\
        or (not RepresentsInt(self.ids.deg.text) and self.ids.deg.text != ""):
            raise TypeError("Input Error")
        xs = self.ids.xs.text
        xs = xs.split()
        ys = self.ids.ys.text
        ys = ys.split()
        x = np.zeros(len(xs))
        y = np.zeros(len(xs))
        for i in range(len(x)):
            x[i] = float(xs[i])
            y[i] = float(ys[i])
        if self.ids.deg.text != "":
            deg = int(self.ids.deg.text)
        else:
            deg = 1
        self.ids.coff.text = str(curve_fitting(x, y, deg))
        
class InNonScreen(Screen):
    equ = 0
    equs = list()
    def okButton(self):
        if self.ids.calc.ids.entry.text == "":
            return    
        text = self.ids.calc.ids.entry.text
        self.equs.append(text)
        self.equ += 1
        if RepresentsInt(self.ids.nequ.text) and self.equ == int(self.ids.nequ.text):
            self.solve()    
        self.ids.calc.ids.entry.text = ""
    def solve(self):
        if self.ids.err.text == "":
            err = 0
        elif RepresentsFloat(self.ids.err.text):
            err = float(self.ids.err.text)
        else:
            raise TypeError("Input Error")        
        initvec = self.ids.initval.text
        initvec = initvec.split()   
        print("out cond")
        if self.ids.initval.text == "":
            ans = NonLinearSolver(self.equs, StoppingError = err)
        elif RepresentsArr(initvec) and len(initvec) == self.equ: 
            print("in cond")
            initval = np.zeros(self.equ)
            for i in range(self.equ):
                initval[i] = float(initvec[i])            
            ans = NonLinearSolver(self.equs, initval, err)
            print(ans)
        else:
            raise TypeError("Input Error") 
        self.ids.vals.text = str(ans[0])
        self.ids.errs.text = str(ans[1])

class InIntrpScreen(Screen):
    def okButton(self):
        if not RepresentsArr(self.ids.xs.text) or not RepresentsArr(self.ids.ys.text):
            raise TypeError("Input Error") 
        xs = self.ids.xs.text
        xs = xs.split()
        ys = self.ids.ys.text
        ys = ys.split()
        self.xlist = list()
        self.ylist = list()
        for i in range(len(xs)):
            self.xlist.append(float(xs[i]))
            self.ylist.append(float(ys[i]))
            
    def okLButton(self):
        self.okButton()
        if self.ids.digits.text != "" and RepresentsInt(self.ids.digits.text):
            dig = int(self.ids.digits.text)
        else:
            dig = 4
        if self.ids.xval.text != "" and RepresentsFloat(self.ids.xval.text):
            ans = interpolationLagrange(self.xlist, self.ylist, float(self.ids.xval.text), dig)
        else:
            ans = interpolationLagrange(self.xlist, self.ylist, numDigits = dig)
        self.ids.func.text = str(ans[0])
        if len(ans) > 1:
            self.ids.fval.text = str(ans[1])
        print(ans, type(ans), len(ans))
        
    def okNButton(self):
        self.okButton()
        if self.ids.digits.text != "" and RepresentsInt(self.ids.digits.text):
            dig = int(self.ids.digits.text)
        else:
            dig = 4
        if self.ids.order.text != "" and RepresentsInt(self.ids.order.text):
            order = int(self.ids.order.text)
        else:
            order = 5
        if self.ids.err.text != "" and RepresentsFloat(self.ids.err.text):
            err = float(self.ids.err.text)
        else:
            err = 1e-8
        if self.ids.xval.text != "" and RepresentsFloat(self.ids.xval.text):
            ans = interpolateNewton(self.xlist, self.ylist, order, float(self.ids.xval.text), err, dig)
        else:
            ans = interpolateNewton(self.xlist, self.ylist, order, appError = err, numDigits = dig)
        self.ids.func.text = str(ans[0])
        if len(ans) > 1:
            self.ids.fval.text = str(ans[1])
        if len(ans) > 2:
            self.ids.errn.text = str(ans[2])
        print(ans, type(ans), len(ans))
            
class InIntegScreen(Screen):
    def okButton(self):
        if(self.ids.table.text != "" and self.ids.calc.ids.entry.text != ""):
           raise TypeError("please choose one method for entering Input") 
        elif(self.ids.table.text != ""):
            table=self.ids.table.text
            table=table.split()
            if( RepresentsArr(table)):
                f=np.zeros(len(table))
                for i in range (len(table)):
                    f[i]=float(table[i])
            else:
                self.ids.ans.text="Input Error"
        elif(self.ids.calc.ids.entry.text != ""):
            f=self.ids.calc.ids.entry.text
        else:
            self.ids.ans.text="Input Error"
        if RepresentsFloat(self.ids.fLimit.text) and RepresentsFloat(self.ids.sLimit.text)\
        and RepresentsInt(self.ids.nPoints.text):
            n=int(self.ids.nPoints.text)
            flimit=float(self.ids.fLimit.text)
            slimit=float(self.ids.sLimit.text)
        else:
            self.ids.ans.text="Input Error"
        return f,flimit,slimit,n
    
    def okTButton(self):
        arr=self.okButton()
        ans=trapezoidal(arr[0],arr[1],arr[2],arr[3])
        self.ids.ans.text=str(ans[0])
        self.ids.err.text=str(ans[1])
        return
    def okOTSButton(self):
        arr=self.okButton()
        ans=simpson_1_3(arr[0],arr[1],arr[2],arr[3])
        self.ids.ans.text=str(ans[0])
        self.ids.err.text=str(ans[1])
        return
    
    def okTESButton(self):
        arr=self.okButton()
        ans=simpson_3_8(arr[0],arr[1],arr[2],arr[3])
        self.ids.ans.text=str(ans[0])
        self.ids.err.text=str(ans[1])
        return

    
class InRungScreen(Screen):
    calls = 0
    def okButton(self):
        if self.calls == 0:
            self.func = self.ids.calc.ids.entry.text
            self.ids.func.text = self.ids.calc.ids.entry.text
            self.ids.calc.ids.entry.text = ""
            self.calls = 1
        else:
            self.equ = self.ids.calc.ids.entry.text
            self.ids.equ.text = self.equ
            self.ids.calc.ids.entry.text = ""
            self.okRButton()
            self.calls = 0
        
    def okRButton(self):
        if not RepresentsFloat(self.ids.xnodval.text) or not RepresentsFloat(self.ids.ynodval.text) or not RepresentsFloat(self.ids.xval.text)\
        or not RepresentsFloat(self.ids.hval.text):
            raise TypeError("Input Error")
        ans = Runge_kutte_ODE(float(self.ids.xnodval.text), float(self.ids.ynodval.text), float(self.ids.xval.text), float(self.ids.hval.text), self.func, self.equ)
        self.ids.yapp.text = str(ans.ya)
        self.ids.err.text = str(ans.error)       
        
class InGausseIntegScreen(Screen):
    def okButton(self):
        if RepresentsFloat(self.ids.fLimit.text) and RepresentsFloat(self.ids.sLimit.text)\
        and RepresentsInt(self.ids.nPoints.text) and self.ids.calc.ids.entry.text !="":
            equ=self.ids.calc.ids.entry.text
            n=int(self.ids.nPoints.text)
            flimit=float(self.ids.fLimit.text)
            slimit=float(self.ids.sLimit.text)
            self.ids.ans.text = str(Integration_GaussLegendre(equ,n,flimit,slimit))
        else:
            self.ids.ans.text="Input Error"
            
class InODESHScreen(Screen):
    equ = 0
    equs = list()
    def okButton(self):
        if self.ids.calc.ids.entry.text == "":
            return
        text = self.ids.calc.ids.entry.text
        print(text)
        self.equs.append(text)
        self.equ += 1
        if RepresentsInt(self.ids.nequ.text) and self.equ == int(self.ids.nequ.text):
            self.solve()
        self.ids.calc.ids.entry.text = ""
        
    def solve(self):
        if self.ids.err.text == "":
            self.ids.err.text = "0.1"
        if self.ids.iter.text == "":
            self.ids.iter.text = "5"
        vals = self.ids.initvec.text
        vals = vals.split()
        if not RepresentsInt(self.ids.nequ.text) or not RepresentsFloat(self.ids.err.text) or not RepresentsInt(self.ids.iter.text)\
        or not RepresentsFloat(self.ids.step.text) or not RepresentsArr(vals) or len(vals) != self.equ+1:
            raise TypeError("Input Error")
        init = list()  
        for i in range(self.equ+1):
            init.append(float(vals[i]))   
        print(self.equs, init, float(self.ids.step.text), float(self.ids.err.text), 1, int(self.ids.iter.text))
        ans = SolveODE(self.equs, init, float(self.ids.step.text), float(self.ids.err.text), 1, int(self.ids.iter.text))
        print(ans)
        self.ids.sol.text = str(ans)
                
class InODESRScreen(Screen):
    equ = 0
    equs = list()
    
    def okButton(self):
        if self.ids.calc.ids.entry.text == "":
            return
        text = self.ids.calc.ids.entry.text
        print(text)
        self.equs.append(text)
        self.equ += 1
        if RepresentsInt(self.ids.nequ.text) and self.equ == int(self.ids.nequ.text):
            self.solve()
        self.ids.calc.ids.entry.text = ""
        
    def solve(self):
        if self.ids.err.text == "":
            self.ids.err.text = "0.1"
        if self.ids.iter.text == "":
            self.ids.iter.text = "5"
        vals = self.ids.initvec.text
        vals = vals.split()
        if not RepresentsInt(self.ids.nequ.text) or not RepresentsFloat(self.ids.err.text) or not RepresentsInt(self.ids.iter.text)\
        or not RepresentsFloat(self.ids.step.text) or not RepresentsArr(vals) or len(vals) != self.equ+1:
            raise TypeError("Input Error")
        init = list()  
        for i in range(self.equ+1):
            init.append(float(vals[i]))   
        print(self.equs, init, float(self.ids.step.text), float(self.ids.err.text), 2, int(self.ids.iter.text))
        ans = SolveODE(self.equs, init, float(self.ids.step.text), float(self.ids.err.text), 2, int(self.ids.iter.text))
        print(ans)
        self.ids.sol.text = str(ans)
        
class InLinScreen(Screen):
    
    def okButton(self):
        mat = self.ids.mat.text
        mat = mat.split()
        vecb = self.ids.vecb.text
        vecb = vecb.split()
        initvec = self.ids.initvec.text
        initvec = initvec.split()
        #Must provide an input error
        if RepresentsFloat(self.ids.err.text) and RepresentsArr(mat) and RepresentsArr(vecb)\
        and RepresentsArr(initvec) and len(mat) == 9 and len(vecb) == 3 and len(initvec) == 3:
            A = np.zeros((3,3))
            bvec = np.zeros((3,1))
            vecinit = np.zeros((3,1))
            for i in range(3):
                for j in range(3):
                    A[i][j] = float(mat[i*3+j])            
                bvec[i] = float(vecb[i])
                vecinit[i] = float(initvec[i])    
            err = float(self.ids.err.text)
            return A, bvec, vecinit, err
        else:
            raise TypeError("Input Error")
        
    def okGButton(self):
        arr = self.okButton()
        ans = SolveGaussSeidel(arr[0], arr[1], arr[2], arr[3])
        self.ids.ans.text=str(ans[0])
        self.ids.errAns.text=str(ans[1])
        print(ans, type(ans))
            
    def okSButton(self):
        if RepresentsFloat(self.ids.omega.text):
            arr = self.okButton()
            omega = float(self.ids.omega.text)
            ans = SolveSOR(arr[0], arr[1], arr[2], omega, arr[3])
            self.ids.ans.text=str(ans[0])
            self.ids.errAns.text=str(ans[1])
            print(ans, type(ans))
        else:
            raise TypeError("Input Error")
        
class InRichScreen(Screen):
    def okTButton(self):
        X = self.ids.X.text
        X = X.split()
        Y = self.ids.Y.text
        Y = Y.split()
        n = int(self.ids.n.text)
        if RepresentsInt(self.ids.order.text) and RepresentsFloat(self.ids.atX.text) and RepresentsArr(X) and RepresentsInt(n)\
        and RepresentsArr(Y) and len(X) == n and len(Y) == n :
            order = int(self.ids.order.text)
            atX = float(self.ids.atX.text)
            Axy = np.zeros((2,n))
            #Ay = np.zeros((1,n))
            for i in range(n):
                Axy[0][i] = float(X[i])    
            for j in range(n):
                Axy[1][j] = float(Y[j])
            ans = Rich(atX,Axy,order)
            self.ids.ans.text=str((ans[1]))
        else:
            self.ids.ans.text="Input Error"
            
    def okFuncButton(self):
        if RepresentsFloat(self.ids.h.text) and RepresentsInt(self.ids.order.text) and self.ids.calc.ids.entry.text != "":
            step = float(self.ids.h.text)
            atX = float(self.ids.atX.text)
            order=int(self.ids.order.text)
            func=self.ids.calc.ids.entry.text
            ans = Rich(atX,errorOrder=order,f=func,h=step)
            self.ids.ans.text=str((ans[1]))
        else:
            self.ids.ans.text="Input Error"
            
class InIpDiffScreen(Screen):
    def okButton(self):
        if self.ids.err.text == "":
            self.ids.err.text = "1e-8"
        if RepresentsFloat(float(self.ids.err.text)) and RepresentsInt(self.ids.app.text) and RepresentsFloat(self.ids.x.text)\
        and RepresentsArr(self.ids.xs.text) and RepresentsArr(self.ids.ys.text):
            xl = self.ids.xs.text
            xl = xl.split()
            yl = self.ids.ys.text
            yl = yl.split()
            xs = list()
            ys = list()
            for i in range(len(xl)):
                xs.append(float(xl[i]))
                ys.append(float(yl[i]))
            ans = newtonGeneral(xs, ys, float(self.ids.x.text), int( self.ids.app.text),float(self.ids.err.text))
            self.ids.ans.text=str(ans[0])
            self.ids.errAns.text=str(ans[1])
            print(ans)
        else:
            self.ids.ans.text="Input Error"
            
class ScreenManage(ScreenManager):
    pass
# The ScreenManager controls moving between screens
screen_manager = Builder.load_file("numerical.kv")

class NumericalApp(App):
    
    def build(self):
        return screen_manager
    
num = NumericalApp()
num.run()
