import requests 
from io import BytesIO 
import PyPDF2 
email = "kornbot380@hotmail.com"
project_name = "Smart_Robots"
url = 'https://www.mouser.com/datasheet/2/389/en.DM00347680-1103277.pdf'
Comp_detail = {} 
pdf_payload = {} 
def concatenate_pdf_page(email,project_name,input_url):
         response = requests.get(input_url, headers={'User-Agent':'Chrome/91.0.4472.124'}) #'Mozilla/5.0'})
         if response.status_code == 200:
              # Use BytesIO to treat the byte content as a file-like object
              pdf_file = BytesIO(response.content)
              #Create a PDF reader object
              pdf_reader = PyPDF2.PdfReader(pdf_file)
              all_text = ""
              # Read and print the content of each page
              for page in pdf_reader.pages:
                            all_text += page.extract_text() 
              print(all_text) 
              list_pdf = url.split("/") #Get the list of pdf to processing the data of total pages 
              pdf_name = list_pdf[len(list_pdf)-1] # Get the name ofpdf  
              if email not in list(pdf_payload): 
                         pdf_payload[email] = {pdf_name:list_pdf}
              if email in list(pdf_payload):
                        if pdf_name not in list(pdf_payload[email]):
                                   pdf_payload[email][pdf_name] = all_text 

                        if pdf_name in list(pdf_payload[email]):
                                   pdf_payload[email][pdf_name]  = all_text
              print(pdf_payload)

concatenate_pdf_page(email,project_name,url) 
