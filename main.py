import os
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

# Настройка размеров окна для теста на ПК (на телефоне проигнорируется)
Window.size = (360, 640)

class GiftApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.theme_style = "Dark"
        
        screen = Screen()
        
        # Данные слайдов
        self.slides = [
            {"img": "assets/1.jpg", "text": "Ты самая лучшая! ✨"},
            {"img": "assets/2.jpg", "text": "Твоя улыбка сияет..."},
            {"img": "assets/3.jpg", "text": "Люблю тебя! ❤️"},
        ]
        self.current_slide = 0

        # Основной слой
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Картинка
        self.image = Image(
            source=self.slides[0]["img"], 
            allow_stretch=True, 
            keep_ratio=True,
            size_hint=(1, 0.7)
        )
        
        # Текст
        self.label = MDLabel(
            text="Настя, это для тебя...", 
            halign="center", 
            font_style="H5",
            theme_text_color="Custom",
            text_color=(1, 0.75, 0.8, 1) # Розовый оттенок
        )
        
        # Кнопка
        self.btn = MDRaisedButton(
            text="Открыть подарок 🎁", 
            pos_hint={"center_x": .5}, 
            on_release=self.start_gift,
            md_bg_color=(0.8, 0, 0.4, 1) # Ярко-розовая кнопка
        )

        layout.add_widget(self.image)
        layout.add_widget(self.label)
        layout.add_widget(self.btn)
        
        screen.add_widget(layout)
        
        # Загрузка музыки
        # KivyMD надежнее грузит звук, если указать полный путь
        self.sound = SoundLoader.load('assets/music.mp3')
        
        return screen

    def start_gift(self, *args):
        self.btn.disabled = True
        self.btn.opacity = 0  # Скрываем кнопку
        
        if self.sound:
            self.sound.play()
            self.sound.loop = True # Зациклить музыку
        
        # Запускаем смену слайдов каждые 4 секунды
        Clock.schedule_interval(self.next_slide, 4)

    def next_slide(self, dt):
        if self.current_slide < len(self.slides) - 1:
            self.current_slide += 1
            self.image.source = self.slides[self.current_slide]["img"]
            self.label.text = self.slides[self.current_slide]["text"]
        else:
            self.label.text = "С любовью! ❤️"
            return False # Остановить таймер

if __name__ == "__main__":
    GiftApp().run()