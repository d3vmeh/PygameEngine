import widget

class Button (widget.Widget):

    def isClicked(self,eventx,eventy):
        if self.x<eventx<self.x+self.width and self.y<eventy<self.y+self.height:
            return True
        else:
            return False

    def onClicked(self):
        print("button clicked")
