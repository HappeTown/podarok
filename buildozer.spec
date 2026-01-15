[app]
title = Подарок Насте
package.name = nastya_gift
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3
version = 1.0
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.permissions = INTERNET, READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1