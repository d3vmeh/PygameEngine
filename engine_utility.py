
def draw_all(widgets,display):
    for w in widgets:
        w.draw(display)


class Alignment:
    def __init__(self,surfacex,surfacey):
        self.surfacex = surfacex
        self.surfacey = surfacey



    def align_center_x(self,surfacewidth,objectwidth):
        centerx = surfacewidth/2
        return self.surfacex+(centerx-(objectwidth/2))

    def align_center_y(self,surfaceheight,objectheight):
        centery = surfaceheight/2
        return self.surfacey+(centery-(objectheight/2))

    def align_center(self,surfacewidth,surfaceheight,objectwidth,objectheight):
        return (self.align_center_x(surfacewidth,objectwidth),self.align_center_y(surfaceheight,objectheight))



def text_align_center(textsurface,surfacex,surfacey,surfacewidth,surfaceheight):
    text_rect = textsurface.get_rect(center=(surfacewidth / 2 + surfacex, surfaceheight / 2 + surfacey))
    #display.blit(self.textsurface, self.text_rect)
    return text_rect