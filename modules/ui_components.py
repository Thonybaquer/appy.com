from PyQt5.QtWidgets import QToolBar, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class CustomToolbar(QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMovable(False)
        self.setup_ui()

    def setup_ui(self):
        # Aquí puedes agregar los botones de la barra de herramientas
        pass

class SidePanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)

        # Botones del panel lateral
        self.calculator_btn = QPushButton("Calculadora")
        self.documents_btn = QPushButton("Documentos")
        self.search_btn = QPushButton("Búsqueda")
        self.analyze_btn = QPushButton("Análisis")

        # Agregar botones al layout
        layout.addWidget(self.calculator_btn)
        layout.addWidget(self.documents_btn)
        layout.addWidget(self.search_btn)
        layout.addWidget(self.analyze_btn)
        layout.addStretch()

        # Estilos
        self.setStyleSheet("""
            QPushButton {
                padding: 10px;
                border: none;
                border-radius: 5px;
                background-color: #f0f0f0;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
            QPushButton:pressed {
                background-color: #d0d0d0;
            }
        """)