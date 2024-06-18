# CHANGELOG.md

## 1.0.0 (2024-6-18)

[Full Changelog](https://github.com/izzalDev/izlearn/compare/origin...v1.0.0)

### **Features:**
- Introduced `ImageExplorer` class within the `izlearn.vision` module.
- Automated metadata extraction including class names, file paths, labels, image dimensions, and file extensions from specified directories.
- Supported image formats: ['jpg', 'jpeg', 'jpe', 'png', 'bmp', 'ppm', 'pbm', 'pgm', 'sr', 'ras', 'tif', 'tiff', 'webp'].
- Added visualization tools:
  - `show_sample_images`: Displayed random sample images with labels.
  - `show_class_distribution`: Visualized class distribution using bar charts.
  - `show_summary`: Presented comprehensive dataset summaries including image count, dimensions, and file extension distribution.

### **Removed:**
- Removed `fungsiku` module previously used for XYZ functionality. Users are advised to refer to [GitHub](https://github.com/your_organization/izlearn/issues) for alternatives or updates.

### **Dependencies:**
- Python (>=3.6)
- Dependencies: OpenCV, scikit-image, Pillow (PIL), NumPy, Matplotlib

## 0.1.11 (unreleased)
Starting this project

<!-- ## 1.8.0 (unreleased)

Features:

  - add support for SVN sources -> [95f32s5b](http://www.google.com)
  - add metadata allowed_push_host to new gem template -> [95f32s5b](http://www.google.com)
  - adds a `--no-install` flag to `bundle package` -> [95f32s5b](http://www.google.com)

## 1.7.0 (2014-08-13)

Security:

  - Fix for CVE-2013-0334, installing gems from an unexpected source -> [95f32s5b](http://www.google.com)

Features:

  - Gemfile `source` calls now take a block containing gems from that source -> [95f32s5b](http://www.google.com)
  - added the `:source` option to `gem` to specify a source -> [95f32s5b](http://www.google.com)

Fix:

  - warn on ambiguous gems available from more than one source -> [95f32s5b](http://www.google.com)

## 1.6.5 (2014-07-23)

Bugfixes:

  - require openssl explicitly to fix rare HTTPS request failures -> [95f32s5b](http://www.google.com)



 -->
