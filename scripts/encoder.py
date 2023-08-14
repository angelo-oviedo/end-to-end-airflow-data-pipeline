# The CSV is encoded in ISO-8859-1, so we need to specify the encoding to be UTF-8.
# Otherwise, we will get an error when loading the CSV file to BigQuery.

import csv

def encoderSolutiion():
    # Open the file with 'ISO-8859-1' encoding
    with open('end-to-end-airflow-data-pipeline/include/dataset/Online_Retail_ISO-8859-1.csv', 'r', encoding='ISO-8859-1') as source_file:
        # Read the file
        reader = csv.reader(source_file)
        rows = list(reader)
        
        # Write the file with 'utf-8' encoding
        with open('end-to-end-airflow-data-pipeline/include/dataset/online_retail.csv', 'w', newline='', encoding='utf-8') as target_file:
            writer = csv.writer(target_file)
            writer.writerows(rows)
        
def filteringSolution():
    with open('./include/dataset/online_retail_error.csv', 'rb') as source_file:
        content = source_file.read()
        # Decode using 'utf-8' and replace errors with a replacement character
        decoded_content = content.decode('utf-8', errors='replace')
    
    with open('./include/dataset/online_retail.csv', 'w', encoding='utf-8') as target_file:
        target_file.write(decoded_content)

filteringSolution()