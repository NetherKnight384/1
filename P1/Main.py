import sys
import pybullet as p
import pybullet_data
from PyQt5.QtWidgets import QApplication, QMainWindow, QOpenGLWidget, QVBoxLayout, QWidget
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

class BulletOpenGLWidget(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(800, 600)
        self.timer_id = None

    def initializeGL(self):
        # Инициализация OpenGL
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.1, 0.1, 0.1, 1)

        # Инициализация PyBullet
        self.physics_client = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -8)

        # Добавляем плоскость и куб
        p.loadURDF("plane.urdf")
        self.cube_id = p.loadURDF("cube.urdf", [0, 0, 1])

        # Устанавливаем таймер для обновления экрана
        self.timer_id = self.startTimer(16)

    def paintGL(self):
        # Очищаем экран и буфер глубины
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Устанавливаем камеру
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(90, self.width() / self.height(), 0.1, 100.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(15, 20, 10, 0, 0, 0, 0, 0, 1)

        # Шаг симуляции в PyBullet
        p.stepSimulation()

        # Получаем позицию и ориентацию куба
        cube_pos, cube_orn = p.getBasePositionAndOrientation(self.cube_id)
        cube_pos = np.array(cube_pos)
        cube_orn_matrix = np.array(p.getMatrixFromQuaternion(cube_orn)).reshape(3, 3)

        # Формируем 4x4 матрицу трансформации
        transform_matrix = np.eye(4)
        transform_matrix[:3, :3] = cube_orn_matrix # Вставляем 3x3 матрицу ориентации
        transform_matrix[:3, 3] = cube_pos # Вставляем позицию

        print()
        print(transform_matrix)

        # Рендеринг куба
        glPushMatrix()
        glMultMatrixf(transform_matrix.flatten())

        glBegin(GL_QUADS)
        # Верхняя грань (синяя)
        glColor3f(0, 0, 1)
        self.draw_quad([1, 1, 1], [-1, 1, 1], [-1, -1, 1], [1, -1, 1])
        # Нижняя грань (красная)
        glColor3f(1, 0, 0)
        self.draw_quad([1, -1, -1], [-1, -1, -1], [-1, 1, -1], [1, 1, -1])
        # Передняя грань (зеленая)
        glColor3f(0, 1, 0)
        self.draw_quad([1, -1, 1], [-1, -1, 1], [-1, -1, -1], [1, -1, -1])
        # Задняя грань (желтая)
        glColor3f(1, 1, 0)
        self.draw_quad([1, 1, -1], [-1, 1, -1], [-1, 1, 1], [1, 1, 1])
        # Левая грань (фиолетовая)
        glColor3f(1, 0, 1)
        self.draw_quad([-1, 1, 1], [-1, 1, -1], [-1, -1, -1], [-1, -1, 1])
        # Правая грань (голубая)
        glColor3f(0, 1, 1)
        self.draw_quad([1, 1, -1], [1, 1, 1], [1, -1, 1], [1, -1, -1])
        glEnd()
        glPopMatrix()

    def draw_quad(self, v1, v2, v3, v4):
        # Утилита для рисования грани куба
        glVertex3fv(v1)
        glVertex3fv(v2)
        glVertex3fv(v3)
        glVertex3fv(v4)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)

    def timerEvent(self, event):
        self.update()

    def closeEvent(self, event):
        p.disconnect(self.physics_client)
        if self.timer_id:
            self.killTimer(self.timer_id)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyBullet + OpenGL 3D Scene")

        # Основной виджет и макет
        main_widget = QWidget()
        layout = QVBoxLayout(main_widget)

        # OpenGL виджет
        self.gl_widget = BulletOpenGLWidget()
        layout.addWidget(self.gl_widget)

        self.setCentralWidget(main_widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())