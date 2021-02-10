# Overview

Color-Splitter is a simple Python script which takes an image and splits it into the channels of a given color space.
Each channel is saved as its own image, offering support for both data accuracy and viewability.

# Usage

This program takes in arguments of the form `key=value`. Arguments currently supported are as follows:

| Argument Name | Purpose                                                                  |               Values               |
| :-----------: | :----------------------------------------------------------------------- | :--------------------------------: |
|    `input`    | The location of the image to split.                                      |           Any input image          |
|    `output`   | The extension of the output image. _Default_: the extension of the input |     Any image format extension     |
|    `space`    | The color space for which the image will be split into.                  | `RGB`, `CMYK`, `YCbCr`, `HSV`, `L` |
|   `rgb_out`   | Whether or not the image should be converted to RGB at the end.          |          `true`, `false`           |

# Examples

To split the image _image.png_ into the YCbCr color space, the following command could be used:

```bash
python color_splitter.py input=image.png output=jpg space=YCbCr
```

This would produce three images: _image_Y.jpg_, _image_Cb.jpg_, and _image_Cr.jpg_.

The PNG format does not support the YCbCr color space, so if the user in this instance wanted to save the images as PNG files, they should enable the `rgb_out` argument like so:

```bash
python color_splitter.py input=image.png rgb_out=true space=YCbCr
```

This will split the image into the Y, Cb, and Cr channels but convert them to RGB before they are saved, allowing them to be saved as PNG images. Some information can be lost as a result of this conversion, however; to avoid this, the output format should be changed to a format which supports the given color space.
