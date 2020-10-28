import time
countdown = 20
print (countdown)
while 5 > 1:
    countdown -= 1
    time.sleep(1)
    print (countdown)
    if countdown == 0:
        from PIL import Image, ImageSequence
        image = Image.open('simp.jpg')
        image.show()
        if countdown == 0:
            import sys
            sys.exit()
