from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
import sqlite3

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fetch and Display Data")
        
        self.label = QLabel(self)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        # Fetch and display data when the window is initialized
        self.load_data()

    def load_data(self):
        conn = sqlite3.connect('rank.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM "Ranking Rewards"')
        data = cursor.fetchall()
        
        display_text = "<br>".join(["&nbsp;&nbsp;".join(map(str, row[1:])) for row in data])
        self.label.setText(display_text)
        
        conn.close()

def main():
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
