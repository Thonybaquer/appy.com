import sys
import pandas as pd
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QStackedWidget, QSplitter, QMenuBar, QAction, QMessageBox, QDialog)
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import Qt
from modules.calculator import Calculator
from modules.document_processor import DocumentProcessor
from modules.file_manager import FileManager
from modules.search_engine import SearchEngine
from modules.data_analyzer import DataAnalyzer
from modules.ui_components import CustomToolbar, SidePanel
from modules.themes import ThemeManager
from modules.settings import AppSettings
from modules.ai_assistant import AIAssistant
from modules.settings_dialog import SettingsDialog
from modules.manual_viewer import ManualViewer
from modules.interactive_graph import InteractiveGraph


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Job Assistance Program")
        self.setMinimumSize(1200, 800)

        self.theme_manager = ThemeManager()
        self.settings = AppSettings()
        self.file_manager = FileManager()

        # Inicializa interactive_graph aquí
        self.interactive_graph = InteractiveGraph()  # Asegúrate de inicializarlo

        self.setup_ui()
        self.setup_menu()
        self.setup_connections()
        self.load_settings()

        self.ai_assistant = AIAssistant()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        self.main_splitter = QSplitter(Qt.Horizontal)

        self.side_panel = SidePanel()
        self.main_splitter.addWidget(self.side_panel)

        work_area = QWidget()
        work_layout = QVBoxLayout(work_area)

        self.toolbar = CustomToolbar()
        work_layout.addWidget(self.toolbar)

        work_splitter = QSplitter(Qt.Horizontal)

        self.stack = QStackedWidget()
        self.calculator = Calculator()
        self.doc_processor = DocumentProcessor()
        self.search_engine = SearchEngine()
        self.data_analyzer = DataAnalyzer()

        self.stack.addWidget(self.calculator)
        self.stack.addWidget(self.doc_processor)
        self.stack.addWidget(self.search_engine)
        self.stack.addWidget(self.data_analyzer)
        self.stack.addWidget(self.interactive_graph)  # Ahora interactive_graph está inicializado

        work_splitter.addWidget(self.stack)
        work_splitter.addWidget(self.ai_assistant)

        work_splitter.setStretchFactor(0, 2)
        work_splitter.setStretchFactor(1, 1)

        work_layout.addWidget(work_splitter)
        self.main_splitter.addWidget(work_area)

        main_layout.addWidget(self.main_splitter)

    def setup_menu(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu('&Archivo')
        file_menu.addAction('&Nuevo', self.new_file, QKeySequence.New)
        file_menu.addAction('&Abrir', self.open_file, QKeySequence.Open)
        file_menu.addAction('&Guardar', self.save_file, QKeySequence.Save)
        file_menu.addSeparator()
        file_menu.addAction('&Salir', self.close, QKeySequence.Quit)

        edit_menu = menubar.addMenu('&Editar')
        edit_menu.addAction(
            '&Deshacer', self.doc_processor.editor.undo, QKeySequence.Undo)
        edit_menu.addAction(
            '&Rehacer', self.doc_processor.editor.redo, QKeySequence.Redo)
        edit_menu.addSeparator()
        edit_menu.addAction('&Preferencias', self.show_settings)

        view_menu = menubar.addMenu('&Ver')
        view_menu.addAction('Cambiar &Tema', self.toggle_theme)

        tools_menu = menubar.addMenu('&Herramientas')
        tools_menu.addAction(
            '&Calculadora', lambda: self.stack.setCurrentWidget(self.calculator))
        tools_menu.addAction(
            '&Análisis de Datos', lambda: self.stack.setCurrentWidget(self.data_analyzer))

        help_menu = menubar.addMenu('A&yuda')
        help_menu.addAction('&Manual', self.show_manual)
        help_menu.addAction('&Acerca de', self.show_about)

    def setup_connections(self):
        self.side_panel.calculator_btn.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.calculator))
        self.side_panel.documents_btn.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.doc_processor))
        self.side_panel.search_btn.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.search_engine))
        self.side_panel.analyze_btn.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.data_analyzer))

        self.ai_assistant.response_received.connect(self.handle_ai_response)

    def load_settings(self):
        theme = self.settings.get_setting('theme')
        if theme:
            self.apply_theme(theme)

        geometry = self.settings.get_setting('window_geometry')
        if geometry:
            self.restoreGeometry(geometry)

    def save_settings(self):
        self.settings.set_setting('window_geometry', self.saveGeometry())
        self.settings.set_setting('theme', self.theme_manager.current_theme)

    def new_file(self):
        if self.stack.currentWidget() == self.doc_processor:
            self.doc_processor.editor.clear()

    def open_file(self):
        content = self.file_manager.open_file()
        if content is not None:
            if isinstance(content, str):
                self.doc_processor.editor.setText(content)
            elif isinstance(content, pd.DataFrame):
                self.data_analyzer.load_data(content)

    def save_file(self):
        if self.stack.currentWidget() == self.doc_processor:
            content = self.doc_processor.editor.toPlainText()
            self.file_manager.save_file(content)

    def toggle_theme(self):
        palette = self.theme_manager.toggle_theme()
        self.setPalette(palette)

    def show_settings(self):
        dialog = SettingsDialog(self.settings, self)
        if dialog.exec_() == QDialog.Accepted:
            self.apply_settings()

    def show_manual(self):
        manual = ManualViewer(self)
        manual.exec_()

    def show_about(self):
        QMessageBox.about(self, "Acerca de JAP",
                          "Job Assistance Program v1.0\n"
                          "Un programa de asistencia integral para profesionales.")

    def handle_ai_response(self, response):
        if "abrir_calculadora" in response.lower():
            self.stack.setCurrentWidget(self.calculator)
        elif "analizar_datos" in response.lower():
            self.stack.setCurrentWidget(self.data_analyzer)

    def closeEvent(self, event):
        self.save_settings()
        event.accept()

    def apply_settings(self):
        theme = self.settings.get_setting('theme')
        self.apply_theme(theme)

        font_size = self.settings.get_setting('font_size')
        font = self.font()
        font.setPointSize(int(font_size))
        self.setFont(font)

        language = self.settings.get_setting('language')
        self.change_language(language)