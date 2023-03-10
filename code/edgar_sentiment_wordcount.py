import pandas as pd 
from ref_data import get_sentiment_word_dict
import os

def write_document_sentiments(input_folder, output_file):
    """
    Obtains all the txt docs containing words from 10-K filings for each
    company for every year from 2012-2023. It then compares each word with
    the LM dictionary to perform the sentimental analysis and save the data
    in a csv file.

    Args:
        input_folder (str): folder directory where txt docs are stores
        output_file (str): folder directory to store the csv file
    """ 
    
    # Creates dataframe and dictionary to perform sentimental analysis
    sentiment_df = pd.DataFrame(columns=['Symbol', 'ReportType', 'FilingDate'] + list(get_sentiment_word_dict().keys()))
    sentiment_dict = get_sentiment_word_dict()
    
    # Obtain each txt doc in the input folder
    for filename in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, filename)
        
        # Open each txt doc and store the ticker, report type and filing date in the dataframe created
        with open(input_file_path, 'r') as f:
            text = f.read()
            new_name = filename.split('_')
            symbol, report_type, filing_date = new_name[:3]
            row = {'Symbol': symbol, 'ReportType': report_type, 'FilingDate': filing_date.split('.')[0]}
            
            # For every word in the txt doc, check if its in the LM dictionary and count the number 
            #       of positive, negative, uncertain, etc.. words. It then includes it in the dataframe.
            for word in text.split(): 
                for key, value in sentiment_dict.items():         
                    if word in sentiment_dict[key]:
                        row[key] = row.get(key, 0) + 1
            
            sentiment_df.loc[len(sentiment_df)] = row
    
    # Save the excel file in the output firectory.
    sentiment_df.to_csv(output_file, index=False)

                    