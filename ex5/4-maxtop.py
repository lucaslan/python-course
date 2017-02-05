def maximo(x,y,z):
    c_x=int(x)
    c_y=int(y)
    c_z=int(z)

    if c_x < c_y and c_z < c_y:
        return c_y
    else:
        if c_x < c_z:
            return c_z
        else:
            return c_x

