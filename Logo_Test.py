import gradio as gr
import pandas as pd
import os
a = "DONE"
# Function to load data from a CSV file and convert it to the required format
def load_sample_data(csv_file):
    if not os.path.exists(csv_file):
        print(f"File {csv_file} not found!")
        return {}

    # Read the CSV into a DataFrame
    df = pd.read_csv(csv_file)

    # Assuming the CSV has columns: "Image Name", "Company Details", "URL", "Time Taken", "Name Confidence", "URL Confidence"
    sample_data = {}
    for _, row in df.iterrows():
        image_key = row['Image Name']
        company_info = f"THE NAME IS: {row['Company Details']}"
        url_info = f"THE URL IS: {row['URL']}"
        score = row['Time Taken']
        name_confidence = row['Name Confidence']
        url_confidence = row['URL Confidence']
        sample_data[image_key] = [[company_info, url_info, name_confidence, url_confidence], score]

    return sample_data

# Function to process data and return information
def get_image_data(image_key, sample_data):
    if image_key is None or image_key == "":
        return None, "", "", "", "", ""

    data = sample_data.get(image_key)
    if data:
        company_info = data[0][0].replace("THE NAME IS: ", "")
        url_info = data[0][1].replace("THE URL IS: ", "")
        name_confidence = data[0][2]
        url_confidence = data[0][3]

        # Construct image path assuming images are stored in "./content/Test50/"
        image_path = 'D:/Langchain/new_morning_test/' + image_key
        if os.path.exists(image_path):
            return image_path, image_key, company_info, url_info, name_confidence, url_confidence
        else:
            return None, image_key, company_info, url_info, name_confidence, url_confidence
    return None, image_key, "", "", "", ""


# Function to add data to CSV
def add_data_to_csv(data):
    csv_file = "new_morning_batch.csv"
    df = pd.DataFrame([data])
    # Append to CSV or create a new one
    if os.path.exists(csv_file):
        df.to_csv(csv_file, mode='a', header=False, index=False)
    else:
        df.to_csv(csv_file, index=False)
    return "You Have Clicked This Button."

# Define the Gradio Interface
def create_interface(sample_data):
    with gr.Blocks() as demo:
        # Create UI for each item in the list
        for i in range(len(sample_data.keys())):  # Adjust number of rows as needed
            with gr.Row():
                # Extract image information from sample_data
                gr.Markdown(f"**Row {i}**")  # Number each row
                image_keys = list(sample_data.keys())
                if i < len(image_keys):
                    image_file = image_keys[i]
                    image_path, image_label, company_info, url_info, name_confidence_value, url_confidence_value = get_image_data(image_file, sample_data)
                else:
                    image_path = None
                    image_label = ""
                    company_info = ""
                    url_info = ""
                    name_confidence_value = ""
                    url_confidence_value = ""

                # Display image, Image source, Company name, Yes/No radio buttons, URL, URL Yes/No
                image_display = gr.Image(value=image_path, label="Image", interactive=False) if image_path else gr.Textbox(value="Image not found", label="Image", interactive=False)
                image_source = gr.Textbox(value=image_label, label="Image Source", interactive=False)
                company_name = gr.Textbox(value=company_info, label="Company Name")
                company_name_correct = gr.Radio(["Correct", "Wrong", "Not Found", "Red Box", "Not Logo"], label="Company Name Correct", value="Correct")
                url = gr.Textbox(value=url_info, label="URL")
                url_correct = gr.Radio(["Correct", "Wrong", "Not Found", "Partially", "Red Box", "Not Logo"], label="URL Correct", value="Correct")

                # Add Name_Confidence and Url_Confidence textboxes
                name_confidence = gr.Textbox(value=name_confidence_value, label="Confidence")
                url_confidence =  gr.Textbox(value=url_confidence_value, label="URL Confidence")

               
               
                # Add button to directly save each row to CSV
                add_button = gr.Button("Add")
                add_button.click(
                    fn=lambda img_src, cmp_name, cmp_name_correct, name_conf, cmp_url, url_correct, url_conf: add_data_to_csv({
                        "Image Source": img_src,
                        "Company Name": cmp_name,
                        "Company Name Correct": cmp_name_correct,
                        "Name Confidence": name_conf,
                        "Company URL": cmp_url,
                        "URL Correct": url_correct,
                        "URL Confidence": url_conf

                    }),
                    inputs=[image_source, company_name, company_name_correct, name_confidence, url, url_correct, url_confidence],
                    outputs=add_button
                )

    return demo

# Load the sample data from CSV
sample_data = load_sample_data("D:/Langchain/New_batch_morning.csv")

# Run the Gradio app if the sample data is loaded successfully
if sample_data:
    demo = create_interface(sample_data)
    demo.launch( share=True)
else:
    print("Failed to load sample data. Please check the input CSV file.")
