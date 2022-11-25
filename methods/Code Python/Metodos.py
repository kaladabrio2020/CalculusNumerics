from   sympy import *
import math as m

def method_falseposicao(f ,a , b,eps,maxit=1_000):
    pontos = []
    iter = 1    
    a = a ;b = b
    xtol = ftol = eps  

    while (True):

        x = ( ((a*f(b)) - (b*f(a)) )/(f(b) - f(a))  )
        
        intervalx = abs(b-a)
        if ( f(a) * f(x) > 0 ):  a = x
        else                  :  b = x
        if ( iter == maxit ):    break
        if ( abs(b-a)  < xtol ): break
        if ( abs(f(x)) < ftol ): break
        pontos.append(x);iter+=1
    
    return x, a, b ,iter , intervalx,pontos

#==================================================
def iteracoes(e, x, y):
    aux = e/(y-x)
    return m.ceil(-1*(m.log(aux, 2)))



def Bissecao2(f,x1,x2,e):
    k=1
    pontos=[]
    maxiter = iteracoes(e,x1,x2)
    
    #if(f(x1)*f(x2)>0):  return (0,0,0,0,0)
    if (abs(x2-x1)<e):  return (0,0,0,0,0)
    
    while(True):
        x = round((x2+x1)/2,6)
        
        if(f(x)*f(x1)<0): x2 = x
        if(f(x)*f(x2)<0): x1 = x
        
        intervaloX = abs(x2-x1)
        if intervaloX < e: break
        if(k==maxiter):    break
        pontos.append(x);k = k+1

    return x,x1,x2,k,f'{intervaloX:.10f}',pontos  




#-----------------------------------------------------
def Newton(f , df, a , eps , maxiter = 100):
    pontos=[]
    iter = 1 
    intervalx=None
    while True:
        
        xi = float(a - (f(a)/df(a)))
        intervalx = abs(xi-a)
        if ( iter == maxiter ):        break
        if ( abs(f(xi)) <= eps ):      break 
        if ( abs(xi - a)     <= eps ): break 
        pontos.append(xi);a = xi ; iter+=1  
        
    return xi,a,iter,f'{intervalx:.10f}',pontos



#=======================================================================
def Cx(f,x): return x[1] - ( ( f(x[1])/(f(x[1]) - f(x[0]) ) ) * (x[1] - x[0]) ) 

def Secant( f , a , b , eps , maxit = 1_000):
    iter  = 1
    xtol  = ftol = eps 
    pontos = []
    
    while True:
        x =  Cx(f,[a,b])
        if (iter == maxit):         break 
        if ( abs(b - a)  <= xtol ): break 
        if ( abs( f(x) ) <= ftol ): break 
        pontos.append(x)
        a , b = b , x
        iter += 1

    return x, a , b , iter , f'{abs(b-a):.10f}' , pontos

