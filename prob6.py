import math

lamb = 1/10
mu = 1/15
c = 3
rho = 0
p0 = 0
P = 0
L_Q = 0
L = 0
w = 0
w_Q = 0

def calculate_p0():
    global p0, c, rho

    sum = 0
    for n in range(c):
        value = (c*rho)**n / math.factorial(n)
        sum = sum + value

    value1 = (c*rho)**c
    value2 = 1/math.factorial(c)
    value3 = 1/(1-rho)
   
    sum = sum + (value1*value2*value3)
    p0 = 1/sum

def calculate_P():
    global rho, c, mu, p0, P

    value1 = (c*rho)**c * p0
    value2 = math.factorial(c) * (1-rho)
    P = value1/value2

def calculate_LQ():
    global L_Q, rho, P

    L_Q = (rho * P) / (1 - rho)

def calculate_L():
    global c, rho, P, L

    value1 = c * rho
    value2 = (rho * P)/(1-rho)

    L = value1 + value2

def calculate_w():
    global L, lamb, w

    w = L / lamb

def calculate_wQ():
    global w, w_Q, mu

    w_Q = w - (1/mu)
    return w_Q 

def main():
    global rho, c, mu, p0, P

    rho = lamb / (c * mu)
    print("rho: ", rho)

    calculate_p0()
    print("p0: ", p0)

    calculate_P()
    print("P(L(inf) >=", c, "): ", P)

    calculate_LQ()
    print("L_Q: ", L_Q)

    calculate_L()
    print("L: ", L)

    calculate_w()
    print("w: ", w)

    print("w_Q: ", calculate_wQ())
    


if __name__ == "__main__":
    main()
