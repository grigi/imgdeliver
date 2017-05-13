ImgDeliver - Image Delivery platform
####################################

ImgDeliver is an Image Delivery platform.

It supports the following:

* Deliver the optimal image format that is supported by the browser (using User-Agent)
* Deliver the image in the requested size
* Deliver the image in the requested aspect ratio
* ImgDeliver will never upscale the image, its purpose is to deliver as small as possible image payloads.

Images are namespaced, and each namespace carries configuration for:

* Where to get image from
* Where to upload rendered image to
* Defaults

  * Size
  * Aspect ratio

* Format config overrides

Rendered images are saved via their sha2, so as to guarantee uniqueness in URL.

Images are requested in the url of:

``<namespace>/<resource-name>?<params>``

``params`` are any sensible combination of the following:

w:
    Requested width in pixels. Image will be scaled down by aspect ratio.
h:
    Requested height. Image will be scaled up by aspect ratio.
r:
    Requested aspect ratio, in the form of:

    * Ratio: ``3:2`` or ``16:9``
    * Value: ``1.191`` 
s:
    Reliative Scale. A value of ``1.0`` is the default.


