import sys
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                             QHBoxLayout, QGraphicsOpacityEffect)
from PySide6.QtCore import QPropertyAnimation, Qt, QEasingCurve
from PySide6.QtGui import QPalette, QColor

class AnimatedButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)
        self.opacity_animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.opacity_animation.setDuration(500) # Длительность анимации (мс)
        self.opacity_animation.setEasingCurve(QEasingCurve.Type.OutQuad) # Тип анимации

        #Устанавливаем изначальную прозрачность
        self.opacity_effect.setOpacity(0.0)

    def fadeIn(self):
        self.opacity_animation.setStartValue(0.0)
        self.opacity_animation.setEndValue(1.0)
        self.opacity_animation.start()

    def fadeOut(self):
        self.opacity_animation.setStartValue(1.0)
        self.opacity_animation.setEndValue(0.0)
        self.opacity_animation.start()


class ModeSwitchExample(QWidget):
    def __init__(self):
        super().__init__()

        self.mode = "Mode 1"
        self.buttons_mode1 = []
        self.buttons_mode2 = []
        self.current_buttons = []

        self.button_switch = QPushButton("Switch to Mode 2")
        self.button_switch.clicked.connect(self.switch_mode)

        # Создаем кнопки для режима 1
        for i in range(3):
            button = AnimatedButton(f"Button {i+1} (Mode 1)")
            self.buttons_mode1.append(button)

        # Создаем кнопки для режима 2
        for i in range(5):
            button = AnimatedButton(f"Button {i+1} (Mode 2)")
            self.buttons_mode2.append(button)

        # Начинаем с режима 1
        self.current_buttons = self.buttons_mode1
        self.button_switch.setText("Switch to Mode 2")

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.button_switch)

        self.button_layout = QHBoxLayout()
        self.vbox.addLayout(self.button_layout)

        self.setLayout(self.vbox)
        self.show_buttons(self.current_buttons)

        #Стиль
        self.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
            }

            QPushButton:hover {
                background-color: #2980b9;
            }
        """)

    def show_buttons(self, buttons):
        """Отображает кнопки с анимацией."""

        #Удаляем предыдущие кнопки
        for i in reversed(range(self.button_layout.count())):
            widget = self.button_layout.itemAt(i).widget()
            if widget is not None:
                widget.fadeOut()
                widget.setParent(None)


        # Добавляем новые кнопки с анимацией
        for button in buttons:
            self.button_layout.addWidget(button)
            button.fadeIn()

    def switch_mode(self):
        """Переключает режимы и анимирует появление/исчезновение кнопок."""
        if self.mode == "Mode 1":
            self.mode = "Mode 2"
            self.current_buttons = self.buttons_mode2
            self.button_switch.setText("Switch to Mode 1")
        else:
            self.mode = "Mode 1"
            self.current_buttons = self.buttons_mode1
            self.button_switch.setText("Switch to Mode 2")

        self.show_buttons(self.current_buttons)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = ModeSwitchExample()
    example.show()
    sys.exit(app.exec())
