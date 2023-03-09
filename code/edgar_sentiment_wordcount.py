import pandas as pd 
from ref_data import get_sentiment_word_dict
import os

def write_document_sentiments(input_folder, output_file):
    
    sentiment_df = pd.DataFrame(columns=['Symbol', 'ReportType', 'FilingDate'] + list(get_sentiment_word_dict().keys()))
    sentiment_dict = get_sentiment_word_dict()
    
    for filename in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, filename)
        
        with open(input_file_path, 'r') as f:
            text = f.read()
            new_name = filename.split('_')
            symbol, report_type, filing_date = new_name[:3]
            row = {'Symbol': symbol, 'ReportType': report_type, 'FilingDate': filing_date.split('.')[0]}
            
            for word in text.split(): 
                for key, value in sentiment_dict.items():         
                    if word in sentiment_dict[key]:
                        row[key] = row.get(key, 0) + 1
            
            sentiment_df.loc[len(sentiment_df)] = row
    
    sentiment_df.to_csv(output_file, index=False)

                    