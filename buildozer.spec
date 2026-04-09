[app]

# (str) Title of your application
title = MyApp

# (str) Package name
package.name = myapp

# (str) Package domain (unique, reverse domain style)
package.domain = org.example

# (str) Source code directory
source.dir = .

# (str) Python entry point file
entrypoint = ap_appy.py

# (list) Include extensions (images, audio)
source.include_exts = py,png,jpg,mp3

# (str) Version of your app
version = 1.0

# (list) Application requirements
requirements = python3,kivy

# (bool) Fullscreen
fullscreen = 1

# (str) Icon (optional)
icon.filename = assets/icon.png

# (str) Presplash (optional)
presplash.filename =

# (list) Permissions
android.permissions = INTERNET

# (bool) Copy assets folder
android.copy_assets = 1

# (int) Minimum Android API level (recommended 21+)
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.ndk_api = 21
android.gradle_dependencies =

# (bool) Allow debug mode
android.debug = 1