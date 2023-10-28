
def setup():
    size (1000 ,1000)
    background (0 ,0 ,0)
def draw():
     global s ,p ,q
     s=random(1000)
     p=random(1000)
     q=random(1,5)
     stroke (random(200,255),random(200,255),random(200,255))
     strokeWeight (q)
     point (p ,s)
