import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

# Create a subclass of QWidget
class HelloWorldApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set the title and size of the window
        self.setWindowTitle("Hello World Application")
        self.setGeometry(100, 100, 280, 80)

        # Create a QVBoxLayout instance
        layout = QVBoxLayout()

        # Create a QLabel and add it to the layout
        label = QLabel("Hello, World!")
        layout.addWidget(label)

        # Set the layout to the window
        self.setLayout(layout)

# Main function to run the application
def main():
    app = QApplication(sys.argv)
    window = HelloWorldApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
