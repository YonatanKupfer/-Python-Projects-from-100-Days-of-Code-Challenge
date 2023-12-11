# Watermark App

## Overview
The Watermark App is a simple Python application built using the Tkinter library and the Pillow (PIL) library for image processing. This application allows users to upload an image, add a customizable text watermark to it, preview the watermarked image, and save the result.

## Features
- **Upload Image:** Choose an image file (PNG, JPG, JPEG, GIF) using the "Upload Image" button.
- **Add Watermark:** Enter text in the provided field and click "Add Watermark" to add a centered text watermark to the image.
- **Preview:** View the watermarked image in a scrollable canvas with horizontal and vertical scrollbars.
- **Save Image:** Save the watermarked image using the "Save" button.

## How to Use
1. Run the `main.py` file using Python.
2. Click the "Upload Image" button and select an image file.
3. Enter text in the text entry field and click "Add Watermark" to add the watermark.
4. Use the scrollbars to navigate the preview canvas.
5. Click "Save" to save the watermarked image.

## Requirements
- Python 3.x
- Tkinter (usually included with Python)
- Pillow (PIL) library (`pip install Pillow`)

## Project Structure
- **main.py:** The main entry point of the application.
- **watermark_app.py:** Defines the WatermarkApp class, managing the Tkinter GUI and interaction with the ImageEditor.
- **image_editor.py:** Handles image loading, processing, and saving. Provides methods for adding a text watermark.

## Dependencies
- Tkinter: Standard GUI toolkit for Python.
- Pillow: A powerful library for image processing tasks.

Feel free to use, modify, and distribute the code for your own projects.
