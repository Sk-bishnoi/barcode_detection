
import os

OUTPUT_FOLDER = os.path.join(os.getcwd(), 'output')

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

SUPPORTED_IMAGE_FORMATS = ['.jpg', '.png', '.jpeg']
SUPPORTED_VIDEO_FORMATS = ['.mp4', '.avi', '.mov']

LOG_START_PROCESS = "[INFO] Starting barcode detection process..."
LOG_FILE_NOT_FOUND = "[ERROR] File does not exist: {}"
LOG_SAVING_IMAGE = "[INFO] Saving processed image at: {}"
LOG_PROCESS_COMPLETE = "[INFO] Processing completed."
LOG_NO_BARCODE_FOUND = "[INFO] No barcodes detected in: {}"
LOG_BARCODE_FOUND = "[INFO] Barcodes detected in {}: {}"
