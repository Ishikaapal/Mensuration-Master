import math

# --- 2D Shape Functions ---
def sq_area(a):
    return a * a

def sq_pari(a):
    return 4 * a

def rect_area(l, b):
    return l * b

def rect_peri(l, b):
    return 2 * (l + b)

def cir_area(r):
    return math.pi * r * r

def cir_peri(r):
    return 2 * math.pi * r

def tri_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def tri_peri(a, b, c):
    return a + b + c

# --- 3D Shape Functions ---
def cube_area(a):
    return 6 * a * a

def cube_vol(a):
    return a ** 3

def cuboid_area(l, b, h):
    return 2 * (l*b + b*h + h*l)

def cuboid_vol(l, b, h):
    return l * b * h

def sp_area(r):
    return 4 * math.pi * r * r

def sp_vol(r):
    return (4/3) * math.pi * r ** 3

def cy_area(r, h):
    return 2 * math.pi * r * (r + h)

def cy_vol(r, h):
    return math.pi * r * r * h

def co_area(r, h):
    l = math.sqrt(r*r + h*h)
    return math.pi * r * (r + l)

def co_vol(r, h):
    return (1/3) * math.pi * r * r * h

def hemi_area(r):
    return 3 * math.pi * r * r

def hemi_vol(r):
    return (2/3) * math.pi * r ** 3

# --- 2D Menu ---
def shape_2D_menu():
    print("\nSelect a 2D shape ✍️:")
    print("1. Square ◼️")
    print("2. Rectangle ▭")
    print("3. Circle ⚪")
    print("4. Triangle 🔺")
    shape = int(input("Enter your choice: "))

    if shape == 1:
        a = float(input("Enter side: "))
        print(f"Area of Square: {sq_area(a)} sq units ✅")
        print(f"Perimeter of Square: {sq_pari(a)} units 📏")

    elif shape == 2:
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        print(f"Area of Rectangle: {rect_area(l, b)} sq units ✅")
        print(f"Perimeter of Rectangle: {rect_peri(l, b)} units 📏")

    elif shape == 3:
        r = float(input("Enter radius: "))
        print(f"Area of Circle: {cir_area(r):.2f} sq units ✅")
        print(f"Circumference of Circle: {cir_peri(r):.2f} units 📏")

    elif shape == 4:
        a = float(input("Enter side 1: "))
        b = float(input("Enter side 2: "))
        c = float(input("Enter side 3: "))
        print(f"Area of Triangle: {tri_area(a, b, c):.2f} sq units ✅")
        print(f"Perimeter of Triangle: {tri_peri(a, b, c)} units 📏")

    else:
        print("❌ Invalid choice. Please try again.")

# --- 3D Menu ---
def shape_3D_menu():
    print("\nSelect a 3D shape 🧠:")
    print("1. Cube 🧊")
    print("2. Cuboid 📦")
    print("3. Sphere 🟠")
    print("4. Cylinder 🧯")
    print("5. Cone 🍦")
    print("6. Hemisphere 🌗")
    shape = int(input("Enter your choice: "))

    if shape == 1:
        a = float(input("Enter side: "))
        print(f"Surface Area of Cube: {cube_area(a)} sq units ✅")
        print(f"Volume of Cube: {cube_vol(a)} cubic units 📦")

    elif shape == 2:
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        h = float(input("Enter height: "))
        print(f"Surface Area of Cuboid: {cuboid_area(l, b, h)} sq units ✅")
        print(f"Volume of Cuboid: {cuboid_vol(l, b, h)} cubic units 📦")

    elif shape == 3:
        r = float(input("Enter radius: "))
        print(f"Surface Area of Sphere: {sp_area(r):.2f} sq units ✅")
        print(f"Volume of Sphere: {sp_vol(r):.2f} cubic units 🟠")

    elif shape == 4:
        r = float(input("Enter radius: "))
        h = float(input("Enter height: "))
        print(f"Surface Area of Cylinder: {cy_area(r, h):.2f} sq units ✅")
        print(f"Volume of Cylinder: {cy_vol(r, h):.2f} cubic units 🧯")

    elif shape == 5:
        r = float(input("Enter radius: "))
        h = float(input("Enter height: "))
        print(f"Surface Area of Cone: {co_area(r, h):.2f} sq units ✅")
        print(f"Volume of Cone: {co_vol(r, h):.2f} cubic units 🍦")

    elif shape == 6:
        r = float(input("Enter radius: "))
        print(f"Surface Area of Hemisphere: {hemi_area(r):.2f} sq units ✅")
        print(f"Volume of Hemisphere: {hemi_vol(r):.2f} cubic units 🌗")

    else:
        print("❌ Invalid choice. Please try again.")

# --- Main Program ---
def main():
    while True:
        print("\n----------------------------------")
        print("  Welcome to Mensuration Master 📐📏")
        print("----------------------------------")
        print("How can we help you? 🤔")
        print("1. 2D Shapes 🟦")
        print("2. 3D Shapes 🧊")
        print("3. Exit 🚪")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                shape_2D_menu()
            elif choice == 2:
                shape_3D_menu()
            elif choice == 3:
                print("Exiting the program... Thanks for using Mensuration Master! 🙏✨")
                break
            else:
                print("❌ Invalid input. Please choose 1, 2, or 3.")
        except ValueError:
            print("⚠️ Please enter a valid number (1-3).")


main()
