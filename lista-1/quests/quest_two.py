
import turtle

def draw_poly(t,n,sz):
    extern_angle = (360.0)/n
    
    for _ in range(n):
        t.forward(sz)
        t.left( extern_angle)

def main():
        draw_poly(turtle,8,50)

if __name__ == "__main__":
        main()