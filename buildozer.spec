[app]

# App metadata
title = Word Counter
package.name = wordcounter
package.domain = org.example

# Source files (LMAO.png is included via the png extension)
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,ttf,otf

version = 0.1

# All logic is local; no backend, no network permissions needed.
requirements = python3,kivy

# Portrait wallpaper (2160x3840)
orientation = portrait
fullscreen = 1

# Android build settings
android.api = 35
android.minapi = 21
android.ndk_api = 21
android.permissions =
android.accept_sdk_license = True

# Icons / visuals (optional: buildozer uses defaults if left blank)
icon.filename =
presplash.filename =

[buildozer]

log_level = 2
warn_on_root = 1
