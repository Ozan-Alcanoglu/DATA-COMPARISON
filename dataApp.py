import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication
from graphs import MainWindow_Function


class MainWindow(MainWindow_Function):

   
    def __init__(self):
        super().__init__()

        
        self.setupUi()
        self.update_button_F.clicked.connect(self.update_graph_F)
        self.update_button_B.clicked.connect(self.update_graph_B)
        self.update_button_FvB.clicked.connect(self.update_graph_FvB)
        
    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            
            if isinstance(widget, FigureCanvas):
                widget.setParent(None)

    def update_graph_F(self,function_name):
        function_name=self.combobox_F.currentText().replace(" ","_")
        function=getattr(self, function_name)
        
        self.clear_layout(self.layout_F)

        self.figure_F.clf()  
        self.canvas_F.draw()

        return function()
         
    def update_graph_B(self,function_name):
        function_name=self.combobox_B.currentText().replace(" ","_")
        function=getattr(self, function_name)
        
        self.clear_layout(self.layout_B)

        self.figure_B.clf()  
        self.canvas_B.draw()

        return function()
    
    def update_graph_FvB(self,function_name):
        function_name=self.combobox_FvB.currentText().replace(" ","_")
        function=getattr(self, function_name)
        
        self.clear_layout(self.layout_FvB)

        self.figure_FvB.clf()  
        self.canvas_FvB.draw()

        return function()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
