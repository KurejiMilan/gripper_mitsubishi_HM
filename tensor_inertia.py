import sys

shape = "" 
ixx = 0.0
iyy = 0.0
izz = 0.0

# mass in kg 
mass = 0.01
radius = 0.039
height = 0.006

width = 0.0
depth = 0.0

def define_usage():
    print(" Incorrect usage.\n")
    print("tensor_inertia.py shape_name mass radius/width height depth.\n")
    print("-----------------\n")
    print("|  shape_name   |\n")
    print("-----------------\n")
    print("|'cylinder' 'c'|\n")
    print("|  'box'    'b'|\n")
    print("-----------------\n")


def check_sys_argv():
    if len(sys.argv)-1 == 0:
        define_usage()
        sys.exit()
    elif len(sys.argv) -1 > 5:
        define_usage()
        sys.exit()
    
    # 
    try:
        float(sys.argv[1])
        print("First argument should specify the shape.\n")
        define_usage()
        sys.exit()
    except ValueError:
        pass

    # List to store the type converted dimesion
    num_arg = []
    global shape, mass, radius, depth, width, height

    # find the geometry shape
    if sys.argv[1] == "cylinder" or sys.argv[1] == "c":
        shape = "cylinder"
        for i in range(2, 5):
            try:
                num_arg.append(float(sys.argv[i]))
            except ValueError:
                print("dimesnions should be in double.\n")
                define_usage()
                sys.exit()
        mass = num_arg[0]
        radius = num_arg[1]
        height = num_arg[2]

    elif  sys.argv[1] == "box" or sys.argv[1] == "b":
        shape = "box"
        for i in range(2, 6):
            try:
                num_arg.append(float(sys.argv[i]))
            except ValueError:
                print("dimesnions should be in double.\n")
                define_usage()
                sys.exit()
        mass = num_arg[0]
        width = num_arg[1]
        height = num_arg[2]
        depth = num_arg[3]
        # print("this is inside=",shape)
        # print("mass=",mass, "width=", width, "height=", height, "depth=", depth,"\n")
    else :
        print("passed geometry shape not defined.\n")
        define_usage


if __name__ == "__main__":
    check_sys_argv()
    # print(shape)
    if shape == "cylinder":
        print("calculating tensor_inertia for solid cylinder.\n")
        ixx = iyy = (mass*(3*pow(radius, 2)+pow(height,2)))/12
        izz = (mass*pow(radius,2))/2

    elif shape == "box":
        print("calculating tensor_inertia for solid box.\n")
        # print("mass=",mass, "width=", width, "height=", height, "depth=", depth,"\n")
        ixx = (mass*(pow(height, 2)+pow(depth,2)))/12
        iyy = (mass*(pow(width, 2)+pow(height,2)))/12
        izz = (mass*(pow(width, 2)+pow(depth,2)))/12

    print('ixx="',ixx,'" ixy="',0.0,'" ixz="',0.0,'" iyy="',iyy,'" iyz="',0.0,'" izz="',izz,'"')
