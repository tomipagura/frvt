# Práctico PyQt5: Editor de Texto con Menús y Diálogos
# ------------------------------------------------
#
# Objetivo: Crear un editor de texto completo integrando todos los conceptos aprendidos:
# menús, diálogos, gestión de archivos, barras de estado y shortcuts de teclado.
#
# Este ejercicio te guiará para construir una aplicación profesional paso a paso.
#
# -----------------------------------------------------------------------------
# Ejercicio 1: Ventana principal con área de texto
# -----------------------------------------------------------------------------
# Teoría:
# - QMainWindow es la base para aplicaciones con menús y barras de herramientas.
# - QTextEdit permite editar texto con formato básico.
# - setCentralWidget() define el widget principal de la ventana.
#
# Consigna:
# - Crear ventana principal (QMainWindow) de 800x600, título "Editor de Texto".
# - Agregar QTextEdit como widget central.
# - Configurar texto inicial: "Escribe aquí tu texto..."

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QMenuBar, 
                             QAction, QFileDialog, QMessageBox, QStatusBar,
                             QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence

class EditorTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de Texto")
        self.setGeometry(100, 100, 800, 600)
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        self.editor.setPlaceholderText("Escribe aquí tu texto...")
        self.crear_menus()
        self.crear_barra_estado()
        
        # COMPLETAR: Crear QTextEdit y establecerlo como widget central
        # self.editor = QTextEdit()
        # self.setCentralWidget(self.editor)
        # self.editor.setPlaceholderText("Escribe aquí tu texto...")

# -----------------------------------------------------------------------------
# Ejercicio 2: Crear la barra de menús
# -----------------------------------------------------------------------------
# Teoría:
# - menuBar() devuelve la barra de menús de QMainWindow.
# - addMenu() crea un menú nuevo.
# - QAction representa una acción que puede estar en menús o barras de herramientas.
#
# Consigna:
# - Crear menú "Archivo" con opciones: "Nuevo", "Abrir", "Guardar", "Salir".
# - Crear menú "Editar" con opciones: "Cortar", "Copiar", "Pegar".
# - Crear menú "Ayuda" con opción: "Acerca de".

    def crear_menus(self):
        menuBar = self.menuBar()
        menu_archivo = menuBar.addMenu('&Archivo')
        menu_editar = menuBar.addMenu('&Editar')
        menu_ayuda = menuBar.addMenu('&Ayuda')
        accion_nuevo = QAction('&Nuevo', self)
        accion_nuevo.setShortcut(QKeySequence.New)  # Ctrl+N
        accion_nuevo.triggered.connect(self.nuevo_archivo)
        menu_archivo.addAction(accion_nuevo)

        accion_abrir = QAction('&Abrir', self)
        accion_abrir.setShortcut(QKeySequence.Open)  # Ctrl+O
        accion_abrir.triggered.connect(self.abrir_archivo)
        menu_archivo.addAction(accion_abrir)

        accion_guardar = QAction('&Guardar', self)
        accion_guardar.setShortcut(QKeySequence.Save)  # Ctrl+S
        accion_guardar.triggered.connect(self.guardar_archivo)
        menu_archivo.addAction(accion_guardar)

        accion_salir = QAction('S&alir', self)
        accion_salir.setShortcut(QKeySequence.Quit)  # Ctrl+Q
        accion_salir.triggered.connect(self.salir)
        menu_archivo.addAction(accion_salir)

        accion_cortar = QAction('Cortar', self)
        accion_cortar.setShortcut(QKeySequence.Cut)  # Ctrl+X
        accion_cortar.triggered.connect(self.editor.cut)
        menu_editar.addAction(accion_cortar)

        accion_copiar = QAction('Copiar', self)
        accion_copiar.setShortcut(QKeySequence.Copy)  # Ctrl+C
        accion_copiar.triggered.connect(self.editor.copy)
        menu_editar.addAction(accion_copiar)

        accion_pegar = QAction('Pegar', self)
        accion_pegar.setShortcut(QKeySequence.Paste)  # Ctrl+V
        accion_pegar.triggered.connect(self.editor.paste)
        menu_editar.addAction(accion_pegar)

        accion_acerca = QAction('Acerca de', self)
        accion_acerca.triggered.connect(self.acerca_de)
        menu_ayuda.addAction(accion_acerca)
        # COMPLETAR: Obtener la barra de menús
        # menubar = self.menuBar()
        
        # COMPLETAR: Crear menú Archivo
        # menu_archivo = menubar.addMenu('&Archivo')
        
        # COMPLETAR: Crear acciones para el menú Archivo
        # accion_nuevo = QAction('&Nuevo', self)
        # accion_nuevo.setShortcut(QKeySequence.New)  # Ctrl+N
        # accion_nuevo.triggered.connect(self.nuevo_archivo)
        # menu_archivo.addAction(accion_nuevo)
        
        # Repite para: Abrir (Ctrl+O), Guardar (Ctrl+S), Salir (Ctrl+Q)
        pass

# -----------------------------------------------------------------------------
# Ejercicio 3: Implementar funciones de archivo
# -----------------------------------------------------------------------------
# Teoría:
# - QFileDialog proporciona diálogos estándar para abrir/guardar archivos.
# - QFileDialog.getOpenFileName() abre diálogo para seleccionar archivo.
# - QFileDialog.getSaveFileName() abre diálogo para guardar archivo.
#
# Consigna:
# - Implementar nuevo_archivo(): limpiar el editor.
# - Implementar abrir_archivo(): usar QFileDialog para cargar archivo.
# - Implementar guardar_archivo(): usar QFileDialog para guardar texto.

    def nuevo_archivo(self):
        if self.editor.document().isModified():
            respuesta = QMessageBox.question(self, 'Guardar cambios', 
                                             '¿Desea guardar los cambios?',
                                             QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if respuesta == QMessageBox.Yes:
                self.guardar_archivo()
            elif respuesta == QMessageBox.Cancel:
                return
            
            self.editor.clear()
            self.archivo_activo = None
            self.setWindowTitle("Editor de Texto - Nuevo Archivo")
            self.statusBar().showMessage('Nuevo archivo creado', 2000)

        # COMPLETAR: Limpiar el contenido del editor
        pass
    
    def abrir_archivo(self):
        archivo = QFileDialog.getOpenFileName(self, 'Abrir archivo', '', 'Archivos de texto (*.txt)')
        if archivo:
            try:
                with open(archivo[0], 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    self.editor.setPlainText(contenido)
                    self.archivo_activo = archivo[0]
                    self.setWindowTitle(f"Editor de Texto - {self.archivo_activo}")
                    self.statusBar().showMessage(f'Archivo abierto: {self.archivo_activo}', 2000)
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'No se pudo abrir el archivo:\n{e}')
        # COMPLETAR: Abrir diálogo de archivo y cargar contenido
        # archivo, _ = QFileDialog.getOpenFileName(self, 'Abrir archivo', '', 'Archivos de texto (*.txt)')
        # if archivo:
        #     try:
        #         with open(archivo, 'r', encoding='utf-8') as f:
        #             contenido = f.read()
        #             self.editor.setPlainText(contenido)
        #     except Exception as e:
        #         QMessageBox.warning(self, 'Error', f'No se pudo abrir el archivo:\n{e}')
        pass
    
    def guardar_archivo(self):
        archivo = QFileDialog.getSaveFileName(self, 'Guardar archivo', '', 'Archivos de texto (*.txt)')
        if archivo:
            try:
                with open(archivo[0], 'w', encoding='utf-8') as f:
                    contenido = self.editor.toPlainText()
                    f.write(contenido)
                    self.archivo_activo = archivo[0]
                    self.setWindowTitle(f"Editor de Texto - {self.archivo_activo}")
                    self.statusBar().showMessage(f'Archivo guardado: {self.archivo_activo}', 2000)
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'No se pudo guardar el archivo:\n{e}')
        # COMPLETAR: Abrir diálogo de guardado y escribir archivo
        pass

# -----------------------------------------------------------------------------
# Ejercicio 4: Agregar diálogos informativos
# -----------------------------------------------------------------------------
# Teoría:
# - QMessageBox permite mostrar mensajes, advertencias y preguntas al usuario.
# - QMessageBox.information() muestra información.
# - QMessageBox.question() hace preguntas con botones Sí/No.
#
# Consigna:
# - Implementar acerca_de(): mostrar información del programa.
# - Modificar salir(): preguntar si desea guardar antes de cerrar.

    def acerca_de(self):
        QMessageBox.information(self, 'Acerca de', 
                               'Editor de Texto v1.0\n\nCreado con PyQt5\nPara aprender desarrollo de interfaces.')

        # COMPLETAR: Mostrar información del programa
        # QMessageBox.information(self, 'Acerca de', 
        #                        'Editor de Texto v1.0\n\nCreado con PyQt5\nPara aprender desarrollo de interfaces.')
        pass
    
    def salir(self):
        respuesta = QMessageBox.question(self, 'Salir', 
                                         '¿Desea guardar los cambios antes de salir?',
                                         QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        if respuesta == QMessageBox.Yes:
            self.guardar_archivo()
            self.close()
        elif respuesta == QMessageBox.No:
            self.close()
        # COMPLETAR: Preguntar si desea guardar antes de salir
        # respuesta = QMessageBox.question(self, 'Salir', 
        #                                 '¿Desea guardar los cambios antes de salir?',
        #                                 QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        # if respuesta == QMessageBox.Yes:
        #     self.guardar_archivo()
        # elif respuesta == QMessageBox.No:
        #     self.close()
        pass

# -----------------------------------------------------------------------------
# Ejercicio 5: Agregar barra de estado
# -----------------------------------------------------------------------------
# Teoría:
# - QStatusBar muestra información en la parte inferior de la ventana.
# - statusBar() devuelve la barra de estado de QMainWindow.
# - showMessage() muestra un mensaje temporal.
#
# Consigna:
# - Agregar barra de estado que muestre "Listo" al inicio.
# - Actualizar mensaje cuando se realizan acciones (abrir, guardar, etc.).

    def crear_barra_estado(self):
        self.statusBar().showMessage('Listo')
     
           
        # COMPLETAR: Crear y configurar barra de estado
        # self.statusBar().showMessage('Listo')
        pass

# -----------------------------------------------------------------------------
# Ejercicio 6: Integración completa
# -----------------------------------------------------------------------------
# Consigna:
# - Llamar todos los métodos de configuración en __init__.
# - Probar todas las funcionalidades del editor.
# - Personalizar colores, fuentes o agregar más opciones de menú.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = EditorTexto()
    
    # COMPLETAR: Llamar métodos de configuración
    # editor.crear_menus()
    # editor.crear_barra_estado()
    editor.show()
    sys.exit(app.exec_())

# -----------------------------------------------------------------------------
# Ejercicio Extra: Mejoras opcionales
# -----------------------------------------------------------------------------
# - Agregar función "Buscar y reemplazar".
# - Implementar vista previa de impresión.
# - Añadir formato de texto (negrita, cursiva).
# - Crear diálogo de configuración de fuente.
# - Implementar funcionalidad de "Archivos recientes".
