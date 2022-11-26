from   sympy import *
import math as m
import pandas as pd
df = pd.DataFrame({
    'iter':[],
    'fx  ':[],
    'a   ':[],
    'b   ':[],
    'intervalo X':[],
    'x' :[]
})

def method_falseposicao(f ,a , b,eps,maxit):
    i = 0
    iter = 1    
    xtol = ftol = eps  

    while (True):
        x = ( ((a*f(b)) - (b*f(a)) )/(f(b) - f(a))  )
        intervalx = abs(b-a)
        df.loc[i] = [iter,f(x),a,b,f'{intervalx:.8f}',x]
        
        if ( f(a) * f(x) > 0 ):  a = x
        else                  :  b = x

        if ( abs(b-a)  < xtol ): break
        if ( abs(f(x)) < ftol ): break
        if ( iter == maxit ):    break
        iter+=1;i+=1
        

    return df

#==================================================
def iteracoes(e, x, y):
    aux = e/(y-x)
    return m.ceil(-1*(m.log(aux, 2)))



def Bissecao(f,x1,x2,eps):
    i = 0
    iter=1
    pontos=[]
    maxiter = iteracoes(eps,x1,x2)
    
    #if(f(x1)*f(x2)>0):  return (0,0,0,0,0)
    if (abs(x2-x1)<eps):  return (0,0,0,0,0)
    
    while(True):
        x = round((x2+x1)/2,6)
        intervalx = abs(x2-x1)
        
        df.loc[i] = [iter,f(x),x1,x2,f'{intervalx:.8f}',x]
        
        if(f(x)*f(x1)<0): x2 = x
        if(f(x)*f(x2)<0): x1 = x
        if intervalx < eps:   break
        if(iter==maxiter):    break
        iter+=1; i+=1

    return df


#-----------------------------------------------------
def Newton(f , dfx, a , eps , maxiter = 100):
    i = 0 
    iter = 1 
    intervalx=None
    while True:
        
        x = float(a - (f(a)/dfx(a)))
        intervalx = abs(x-a)
        df.loc[i] = [iter,f(x),a,0,f'{intervalx:.8f}',x]
        
        if ( iter == maxiter ):       break
        if ( abs(f(x)) <= eps ):      break 
        if ( abs(x - a)     <= eps ): break 
        a = x ; iter+=1 ; i+=1
        
    return df



#=======================================================================
def Cx(f,x): return x[1] - ( ( f(x[1])/(f(x[1]) - f(x[0]) ) ) * (x[1] - x[0]) ) 

def Secant( f , a , b , eps , maxit = 100):
    iter  = 1
    xtol  = ftol = eps 
    i = 0
    

    while True:
        x =  Cx(f,[a,b])
        
        df.loc[i] = [iter,f(x),a,b,f'{abs(b-a):.8f}',x]
        if (iter == maxit):         break 
        if ( abs(b - a)  <= xtol ): break 
        if ( abs( f(x) ) <= ftol ): break 
        a , b = b , x
        iter += 1 ; i+=1

    return df



