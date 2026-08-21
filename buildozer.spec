
[app]
title = MyDzApp
package.name = mydzapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.1,requests,urllib3,chardet,idna
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1
