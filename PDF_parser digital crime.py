# Databricks notebook source
pip install pymupdf

# COMMAND ----------

import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    text = ""
    textarray = []
    
    # Iterate over each page
    for page_num in range(len(pdf_document)):
        # Get the page
        page = pdf_document.load_page(page_num)
        # Extract text from the page
        text += page.get_text()

    return text

# Example usage
pdf_path = "/Volumes/whitepapers/testschema1/myvol/PreventionOfDigitalCrimeAndCorruptionInAWeb3-dot-0World.pdf"
extracted_text = extract_text_from_pdf(pdf_path)
print(extracted_text)

# COMMAND ----------

pip install databricks_genai_inference

# COMMAND ----------

from databricks_genai_inference import ChatCompletion

# Only required when running this example outside of a Databricks Notebook
#export DATABRICKS_HOST="https://dbc-deded88a-54e7.cloud.databricks.com"
#export DATABRICKS_TOKEN="dapi63684d28c80bdefe51f646994eedfee0"

response = ChatCompletion.create(model="databricks-dbrx-instruct",
                                messages=[{"role": "system", "content": "You are a helpful assistant."},
                                          {"role": "user","content": f"You will be provided with a document and asked to convert it to a conversation.\n\nSummarize the following document into a conversation:\n\n { extracted_text}"}
                                          ],
                                max_tokens=4096)
print(f"response.message:{response.message}")

# COMMAND ----------

resp1 = str(response.message)

# COMMAND ----------

from databricks_genai_inference import ChatCompletion

# Only required when running this example outside of a Databricks Notebook
#export DATABRICKS_HOST="https://dbc-deded88a-54e7.cloud.databricks.com"
#export DATABRICKS_TOKEN="dapi63684d28c80bdefe51f646994eedfee0"

response = ChatCompletion.create(model="databricks-dbrx-instruct",
                                messages=[{"role": "system", "content": "You are a helpful assistant."},
                                          {"role": "user","content": f"You will be provided with a document and asked to convert it to a conversation.\n\nSummarize the following document into a conversation:\n\n { extracted_text}"},
                                          {"role": "assistant","content": resp1},
                                          {"role": "user","content": "now convert this into a podcast between 2 people, bob the host and ryan the guest"}],
                                max_tokens=4096)
print(f"response.message:{response.message}")

# COMMAND ----------

str(response.message)

# COMMAND ----------

final_response =str(response.message)

# COMMAND ----------

pip install pyt2s

# COMMAND ----------

from IPython.display import Audio
from pyt2s.services import stream_elements

obj = stream_elements.StreamElements()

data = obj.requestTTS(final_response, 'Russell')

mp3_file_path = "/Volumes/whitepapers/whitepod/whitepods/digital_crime.mp3"

with open(mp3_file_path, '+wb') as file:
   file.write(data)

# Play the MP3 file
Audio(data , rate=44100)

# COMMAND ----------


