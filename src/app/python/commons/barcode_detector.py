import cv2
from pyzbar import pyzbar
import os
from src.app.python.constants.constant import OUTPUT_FOLDER, LOG_FILE_NOT_FOUND, LOG_SAVING_IMAGE, LOG_PROCESS_COMPLETE, SUPPORTED_IMAGE_FORMATS

class BarcodeDetector:
    """
    Class for detecting barcodes in images and videos.
    """

    def __init__(self):
        pass

    def detect_barcodes(self, image):
        """
        Detect barcodes in an image using pyzbar.
        Returns the image with detected barcodes and a list of cropped barcode images.
        """
        try:
            barcodes = pyzbar.decode(image)
            cropped_images = []
            barcode_numbers = []

            for barcode in barcodes:
                # Get barcode data and position
                barcode_data = barcode.data.decode("utf-8")
                (x, y, w, h) = barcode.rect
                barcode_numbers.append(barcode_data)

                # Crop the detected barcode area
                cropped_image = image[y-100:y + h+100, x-100:x + w+100]
                cropped_images.append(cropped_image)

                # Draw a rectangle around the barcode
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                # Display the barcode number on the image
                text = f"Barcode: {barcode_data}"
                cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            return image, barcode_numbers
        except Exception as e:
            print(f"[ERROR] Failed to detect barcodes: {str(e)}")
            return None, [], []

    def save_output_image(self, image, file_name):
        """
        Save the processed image with detected barcodes in the output folder.
        """
        try:
            output_path = os.path.join(OUTPUT_FOLDER, file_name)
            cv2.imwrite(output_path, image)
            print(LOG_SAVING_IMAGE.format(output_path))
        except Exception as e:
            print(f"[ERROR] Failed to save image: {str(e)}")

    def process_single_image(self, image_path):
        """
        Process a single image for barcode detection.
        """
        try:
            if not os.path.exists(image_path):
                print(LOG_FILE_NOT_FOUND.format(image_path))
                return
            
            image = cv2.imread(image_path)
            processed_image, barcodes = self.detect_barcodes(image)
            if processed_image is not None:
                file_name = os.path.basename(image_path)
                self.save_output_image(processed_image, file_name)

                # Return cropped images for barcode reading
                return processed_image, barcodes
        except Exception as e:
            print(f"[ERROR] Error in processing image: {str(e)}")
            return [], []

    def process_multiple_images(self, images_folder):
        """
        Process multiple images for barcode detection.
        """
        try:
            for file_name in os.listdir(images_folder):
                ext = os.path.splitext(file_name)[-1].lower()
                if ext in SUPPORTED_IMAGE_FORMATS:
                    image_path = os.path.join(images_folder, file_name)
                    cropped_images, barcodes = self.process_single_image(image_path)
                    # Return all cropped images for barcode reading
                    if cropped_images:
                        return cropped_images, barcodes
        except Exception as e:
            print(f"[ERROR] Error in processing multiple images: {str(e)}")
            return [], []

    def process_video(self, video_path):
        """
        Process a video for barcode detection.
        """
        try:
            if not os.path.exists(video_path):
                print(LOG_FILE_NOT_FOUND.format(video_path))
                return
            
            cap = cv2.VideoCapture(video_path)
            frame_count = 0
            cropped_images = []
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                processed_frame, barcodes = self.detect_barcodes(frame)
                file_name = f"frame_{frame_count}.jpg"
                self.save_output_image(processed_frame, file_name)
                frame_count += 1
            
            cap.release()
            print(LOG_PROCESS_COMPLETE)
            return cropped_images  # Return all cropped images for barcode reading
        except Exception as e:
            print(f"[ERROR] Error in processing video: {str(e)}")
            return []
