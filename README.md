
# Gradio Interface For Logo 2 Details

This project is a Python-based web application utilizing the **Gradio** framework to display image data and related company information from a CSV file. Users can view the images, correct or validate company names and URLs, and save their edits back to a CSV file.

## Project Structure

- **Main Script**: 
  - Loads data from a CSV file.
  - Displays images and corresponding information using Gradio.
  - Allows users to validate and correct the displayed data.
  - Writes user input back to a CSV file.

## Key Functionalities

1. **Load Sample Data**:
   - Reads a CSV file containing image names, company details, URLs, and confidence scores.
   - Converts the CSV data into a format that the Gradio interface can use.
   
2. **Display Interface**:
   - Each row from the CSV data is displayed with:
     - Image (or "Image not found" if the image is missing).
     - Text fields for company name and URL.
     - Yes/No radio buttons to indicate whether the company name or URL is correct.
     - Confidence scores for both company names and URLs.
     
3. **Save Data to CSV**:
   - After the user validates/corrects the data, they can save their input by clicking the "Add" button.
   - The modified data is appended to a new CSV file named `new_morning_batch.csv`.

## File Paths

- The script expects the following:
  - Images are located in: `D:/Langchain/new_morning_test/`
  - CSV file path: `D:/Langchain/New_batch_morning.csv`

Ensure the paths are correct before running the application.

## Requirements

- Python 3.x
- Required Python Libraries:
  - `gradio`
  - `pandas`

You can install the required libraries with:

```bash
pip install gradio pandas
```

## Usage

1. Clone or download this repository.
2. Make sure your CSV and image files are correctly placed in their respective directories.
3. Run the script. The Gradio interface will launch in a web browser or generate a shareable link.

```bash
python app.py
```

If the sample data loads successfully, the Gradio interface will display images and their related data.

## CSV File Format

The CSV file should have the following columns:
- `Image Name`: Name of the image file.
- `Company Details`: Information about the company.
- `URL`: The company URL.
- `Time Taken`: Time-related information (optional).
- `Name Confidence`: Confidence score for the company name.
- `URL Confidence`: Confidence score for the company URL.

Example:

| Image Name   | Company Details | URL               | Time Taken | Name Confidence | URL Confidence |
|--------------|-----------------|-------------------|------------|-----------------|----------------|
| image1.png   | ABC Corp         | http://abc.com    | 30 sec     | 0.85            | 0.90           |
| image2.png   | XYZ Ltd          | http://xyz.com    | 45 sec     | 0.95            | 0.88           |

## How it Works

- When the application is launched, it reads the CSV file and displays the corresponding image and data.
- Users can validate or correct the data, then save the changes to a new CSV file.
  
## Contributions

Feel free to fork this repository and submit a pull request for improvements.
