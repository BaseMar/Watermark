from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter.filedialog import askopenfilename, asksaveasfilename

class App:
    def __init__(self, master):
        # Create a label widget for the image
        self.image_label = Label(master)
        self.image_label.pack()

        # Create a button to open the file dialog
        self.button = Button(master, text='Open Image', command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        # Show the file dialog and get the selected file path
        file_path = askopenfilename(filetypes=[('Image files', '*.jpg *.png')])

        # If no file was selected, return
        if not file_path:
            return

        # Open the image using the Pillow library
        with Image.open(file_path).convert("RGBA") as base:
            text="Watermark"
            txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
            fnt = ImageFont.truetype('arial.ttf', size=150)
            d = ImageDraw.Draw(txt)
            text_width, text_height = d.textsize(text, fnt)
            # Add the watermark to the image
            x = (base.width - text_width) / 2
            y = (base.height - text_height) / 2
            d.text((x, y), text, font=fnt, fill=(255, 255, 255, 15))
            out = Image.alpha_composite(base, txt)

            # Save the modified image to a file
            save_path = asksaveasfilename(defaultextension='.png', filetypes=[('PNG files', '*.png')])
            if save_path:
                out.save(save_path)

# Create a tkinter window
root = Tk()

# Create the app
app = App(root)

# Run the tkinter event loop
root.mainloop()
