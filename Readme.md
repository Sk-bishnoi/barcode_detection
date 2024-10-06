
---

# Barcode Detection

## Table of Contents

- [Description](#description)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Tested On](#tested-on)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
- [Directory Structure](#directory-structure)

## Description
This project implements a barcode detection and reading system using Python. It processes single images, multiple images from a folder, or videos to detect barcodes, crop the detected regions, and read the barcode values. The results are saved in an output directory with the detected barcodes annotated in the images.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

Steps to install all the dependencies:

```bash
git clone https://github.com/Sk-bishnoi/barcode_detection.git
cd barcode_detection
pip install -r requirements.txt
sudo apt-get update
sudo apt-get install libzbar0
```

### Tested On

This project has been tested on the following environment:

- **Ubuntu 20.04**

## Usage

### Running the Application

You can run the script with the following commands based on the type of media you want to process:

1. **For a Single Image:**
   ```bash
   python main.py --type image --path /path/to/image.jpg
   ```

2. **For Multiple Images:**
   ```bash
   python main.py --type images --path /path/to/images/folder
   ```

3. **For a Video:**
   ```bash
   python main.py --type video --path /path/to/video.mp4
   ```

## Directory Structure

```
barcode_detection/
├── main.py
├── Readme.md
├── requirements.txt
└── src
    └── app
        └── python
            ├── commons
            │   ├── barcode_detector.py
            │   └── barcode_reader.py
            └── constants
                └── constant.py
```

---
