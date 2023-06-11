[app]
# Title of your application
title = QuizUp

# Package name
package.name = com.example.quizup

# Package domain (needed for Android/IOS packaging)
package.domain = org.example

# Source code where the main.py is located
source.dir = .

# Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv

# List of inclusions using pattern matching
source.include_patterns =

# Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# List of directories to exclude (let empty to not exclude anything)
source.exclude_dirs =

# Application versioning (method 1)
version = 0.1

# Android API to use
android.api = 24

# Minimum API required
android.minapi = 21

# Android SDK version to use
android.sdk = 24

# Android NDK version to use
android.ndk = 23.0.7599858

# Ant build tool version
android.ant = 1.10.10

# Path to the Android SDK
android.sdk_path = /path/to/android/sdk

# Android NDK directory (if empty, it will be automatically downloaded)
android.ndk_path = /path/to/android/ndk

# Python-for-android branch to use, defaults to master
p4a.branch = develop

# The NDK version to use by default
p4a.ndk_version = 23.0.7599858

# Permissions
android.permissions = INTERNET

# Services
android.services = INTERNET

# Requirements for the build
requirements = kivy, requests, plyer

# Android logcat filters to use
android.logcat_filters = *:S python:D

# Android adb command to use
adb = adb

# Android command to use for running the application
android.deploy_type = apk

[buildozer]
log_level = 2
warn_on_root = 1
