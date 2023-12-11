import tkinter as tk
from tkinter import filedialog, messagebox
from image_editor import ImageEditor
from PIL import ImageTk

class WatermarkApp:
    def __init__(self, root):
        # Initialize the main Tkinter window
        self.root = root
        self.root.title("Watermark App")
        self.root.config(padx=20, pady=20, bg="white")

        # Create the ImageEditor instance
        self.image_editor = ImageEditor()

        # UI components
        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.watermark_text_entry = tk.Entry(root, width=30)
        self.watermark_button = tk.Button(root, text="Add Watermark", command=self.add_watermark)
        self.watermark_button["state"] = "disabled"
        self.save_button = tk.Button(root, text="Save", command=self.save_image)
        self.save_button["state"] = "disabled"
        self.preview_canvas = tk.Canvas(root, width=600, height=600, bg="white")

        self.scrollbar_y = tk.Scrollbar(root, orient=tk.VERTICAL, command=self.preview_canvas.yview)
        self.scrollbar_x = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=self.preview_canvas.xview)
        self.preview_canvas.configure(yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)

        # Grid Layout
        self.upload_button.grid(row=0, column=0, padx=5, pady=5)
        self.watermark_text_entry.grid(row=0, column=1, padx=5, pady=5)
        self.watermark_button.grid(row=0, column=2, padx=5, pady=5)
        self.save_button.grid(row=0, column=3, padx=5, pady=5)
        self.preview_canvas.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
        self.scrollbar_y.grid(row=1, column=4, sticky=tk.NS)
        self.scrollbar_x.grid(row=2, column=0, columnspan=4, sticky=tk.EW)

        self.preview_image = None

    def upload_image(self):
        # Open the file dialog to allow the user to select an image
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            # Load the image and enable the watermark button
            self.image_editor.load_image(file_path)
            self.watermark_button["state"] = "normal"
            self.update_preview()
           

    def add_watermark(self):
        # Get the text from the entry and add it to the image
        text = self.watermark_text_entry.get()
        if text:
            self.image_editor.add_text(text)
            self.save_button["state"] = "normal"
            self.update_preview()
            tk.messagebox.showinfo("Success!", "Watermark added successfully!")

    def save_image(self):
        # Save the watermarked image
        self.image_editor.save_image()
        tk.messagebox.showinfo("Success!", "Image saved successfully!")

    def update_preview(self):
        # Update the preview canvas with the watermarked image
        if self.image_editor.image:
            image = ImageTk.PhotoImage(self.image_editor.image)
            self.preview_image = image
            self.preview_canvas.config(width=min(1000, image.width()), height=min(700, image.height()))
            self.preview_canvas.create_image(0, 0, image=image, anchor="nw")
            self.preview_canvas.config(scrollregion=self.preview_canvas.bbox(tk.ALL))