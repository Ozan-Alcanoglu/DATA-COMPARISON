import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QComboBox


class Ui_MainWindow(QMainWindow):

    def setupUi(self):

        self.setWindowTitle('Football And Basketball Data Application')
        self.setGeometry(0,0,1940,1080)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.figure_F = plt.figure()
        self.figure_B = plt.figure()
        self.figure_FvB = plt.figure()

        self.canvas_F = FigureCanvas(self.figure_F)
        self.canvas_B = FigureCanvas(self.figure_B)
        self.canvas_FvB = FigureCanvas(self.figure_FvB)

        graph_widget_F = QWidget(self)
        self.layout_F = QVBoxLayout(graph_widget_F)

        self.combobox_F = QComboBox()
        self.combobox_F.addItems(["Football Statistics", "Forwards vs Defenders Aerial", "Goals vs Assists Ratio", "Best Forwards"
                    , "Forwards vs Defenders Attack and Defend", "Most Played Minutes", "Best Passing Goalkeeper", "Midfielders Pass Choices"
                    , "Best Defenders"
                    ])
        self.layout_F.addWidget(self.combobox_F)

        self.update_button_F = QPushButton("Show Graph")
        self.layout_F.addWidget(self.update_button_F)
        graph_widget_F.setGeometry(40, 10, 600, 500)
        self.layout_F.addWidget(self.canvas_F)

        graph_widget_B = QWidget(self)
        self.layout_B = QVBoxLayout(graph_widget_B)

        self.combobox_B = QComboBox()
        self.combobox_B.addItems(["Basketball Statistics", "Best Basketball Player by Points", "Best Basketball Players by Rating"
                    , "Best Players of the Last 5 Years", "Best Assisters of the Last 5 Years", "Average Assists of the Last 5 Years"
                    , "Average Points of the Last 5 Years", "Top 3 Tallest Players", "Tallest Players of the Last 5 Years"
                    ])
        self.layout_B.addWidget(self.combobox_B)

        self.update_button_B = QPushButton("Show Graph")
        self.layout_B.addWidget(self.update_button_B)
        graph_widget_B.setGeometry(1280, 10, 600, 500)
        self.layout_B.addWidget(self.canvas_B)
        

        graph_widget_FvB = QWidget(self)
        self.layout_FvB = QVBoxLayout(graph_widget_FvB)

        self.combobox_FvB = QComboBox()
        self.combobox_FvB.addItems(["Footballer vs Basketballer 2022", "Football vs Basketball by Shoot", "Football vs Basketball by Assist"
                        ,"Football vs Basketball by Minute","Football vs Basketball by Age"            
                        ])
        self.layout_FvB.addWidget(self.combobox_FvB)

        self.update_button_FvB = QPushButton("Show Graph")
        self.layout_FvB.addWidget(self.update_button_FvB)
        graph_widget_FvB.setGeometry(660, 500, 600, 500)
        self.layout_FvB.addWidget(self.canvas_FvB)
