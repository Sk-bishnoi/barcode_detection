
import argparse
from src.app.python.commons.barcode_detector import BarcodeDetector

def main():
    detector = BarcodeDetector()

    parser = argparse.ArgumentParser(description="Barcode Detection in Image/Video Files")
    parser.add_argument("--type", required=True, choices=['image', 'images', 'video'],
                        help="Type of media to process: 'image' for single image, 'images' for multiple images, or 'video' for video file.")
    parser.add_argument("--path", required=True, help="Path to the file or folder.")
    args = parser.parse_args()

    if args.type == 'image':
        cropped_images, _ = detector.process_single_image(args.path)
    elif args.type == 'images':
        cropped_images, _ = detector.process_multiple_images(args.path)
    elif args.type == 'video':
        cropped_images = detector.process_video(args.path)


if __name__ == "__main__":
    main()
