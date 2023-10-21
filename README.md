# ComfyUI Output Images Gallery

## Introduction

ComfyUI Output Images Gallery is a simple web application built with Flask to display a gallery of images. It's designed to showcase a collection of images with thumbnails and provides an easy way for users to view and navigate through the gallery.

<img src="logo.png" width="50%" height="50%">

## Features

- Display images with responsive thumbnails.
- Modern and professional design for desktop browser and mobile.
- Pagination for easy navigation.
- Click on thumbnails to view full-sized images in a lightbox (Fancybox).
- Dark mode aesthetic for an elegant look.

## Installation and Setup

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python:** You can download Python from [Python's official website](https://www.python.org/downloads/).
- **Flask:** Install Flask, the web framework, using pip:
- **Pillow:** Pillow is used for image processing. Install it using pip:

### Symlink Your Image Directory

To use your own images, symlink your image directory to the project's "static/images/output" directory:

```ln -s /path/to/your/images /path/to/gallery/static/images/output```

Configure Paths
You may need to configure the paths for the logo, thumbnails, and original images in the app.py file:

logo.png - Change the path of the logo image on line 16.
thumbnails - The generated thumbnail images will be saved in the static/thumbnails directory.
original images - The original images are expected in the static/images/output directory (symlinked from your image directory).
Set Port Number and Run the App
You can change the port number and host as needed in the app.py file on line 44. By default, it's set to run on http://0.0.0.0:9999.

Start the Flask app by running the following command in your terminal or command prompt:

```python app.py```

The app should now be running, and you can access it by opening a web browser and navigating to http://localhost:9999 (or the custom host and port you've specified).

Customization
You can customize the gallery's appearance and behavior by modifying the HTML templates, CSS styles, and the Flask application code. Feel free to tailor it to your specific requirements.

![image](https://github.com/Smuzzies/comfyui_image_gallery/assets/110495122/eb8adc34-811e-434b-9ea7-d225f7cc63bb)
![image](https://github.com/Smuzzies/comfyui_image_gallery/assets/110495122/cf30e7ab-041d-4b9a-99c5-b6d863bb09f8)
