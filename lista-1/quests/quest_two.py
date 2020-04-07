
import turtle

def draw_poly(t,n,sz):
    extern_angle = (360.0)/n
    
    for _ in range(n):
        t.forward(sz)
        t.left( extern_angle)


draw_poly(turtle,13,50)