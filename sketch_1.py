select =int(input("press 1 for first sketch or press 2 for second sketch or press 3 for third sketch "))
if select == 1:
    # First sketchpy
    import sketchpy
    from sketchpy import canvas
    obj=canvas.sketch_from_image("D:\Himai Sharma\Desktop\kainchi-dham-neem-karoli-baba-.jpg")
    obj.draw(threshold=120)
if select == 2:
    # second sketch
    from sketchpy import library as l
    apjabdul_kalam=l.apj() 
    apjabdul_kalam.draw()
if select == 3:
    # Third sketch
    from sketchpy import library
    myObject = library.flag()
    myObject.draw()








