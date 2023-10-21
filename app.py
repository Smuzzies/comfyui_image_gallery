import os
from flask import Flask, render_template, request
from PIL import Image, ImageFilter

app = Flask(__name__)

# Define the directory where your original images are stored
image_dir = 'static/images/output'

# Define the directory where thumbnails will be stored
thumbnail_dir = 'static/thumbnails'

@app.route('/')
def image_gallery():
    # Get a list of image files from the specified directory
    image_files = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.png', '.jpeg', '.gif'))]
    # Sort the list of image files by last modified date (newest first)
    image_files.sort(key=lambda x: os.path.getmtime(os.path.join(image_dir, x)), reverse=True)

    # Get the page number from the query string (default to 1)
    page = int(request.args.get('page', 1))

    # Calculate the total number of pages
    total_pages = (len(image_files) + 99) // 100  # Ensure a maximum of 100 images per page

    # Calculate the available width based on the browser window size (adjust as needed)
    available_width = request.args.get('browser_width', type=int, default=1200)  # Default to 1200 pixels

    # Calculate the maximum number of columns based on the available width
    max_columns = min(available_width // 220, 5)  # Adjust the width (220) as needed

    # Calculate the number of rows and columns for the current page
    images_per_page = min(len(image_files), 100)  # Maximum of 100 images per page
    rows = (images_per_page + max_columns - 1) // max_columns
    columns = max_columns

    # Calculate the start and end indices for the current page
    start_idx = (page - 1) * images_per_page
    end_idx = start_idx + images_per_page

    # Slice the image list to display images for the current page
    current_images = image_files[start_idx:end_idx]

    # Generate thumbnails for the current page if they don't exist
    generate_thumbnails(current_images)

    return render_template('index.html', current_thumbnails=current_images, total_pages=total_pages, page=page)

def generate_thumbnails(image_list):
    for image in image_list:
        thumbnail_path = os.path.join(thumbnail_dir, image)
        if not os.path.exists(thumbnail_path):
            try:
                original_image = Image.open(os.path.join(image_dir, image))
                max_width = 200  # Define your desired thumbnail width
                max_height = 200  # Define your desired thumbnail height
                original_image.thumbnail((max_width, max_height), Image.ANTIALIAS)
                original_image.save(thumbnail_path)
            except Exception as e:
                print(f"Error generating thumbnail for {image}: {str(e)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
