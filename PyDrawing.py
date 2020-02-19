import pyautogui as pag

def drawing():
    """ This function just for testing """
    pag.drag(100,0)
    pag.drag(0,50)
    pag.drag(-100,0)
    pag.drag(0,-49)

def drawDev(times_drawing):
    """ Drawing's function """
    for i in range(times_drawing):
        distance = 80
        pag.drag(distance,0)
        pag.drag(0, distance)
        distance -= 10
        pag.drag(0, -distance)
        pag.drag(-distance, 0)


if  __name__ == "__main__":
    # An exemple:
    drawDev(10)
