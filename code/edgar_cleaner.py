from bs4 import BeautifulSoup
import re
import os


def clean_html_text(html_text):
    '''
    Function uses BeautifulSoup to parse html text and replaces any tags
    or punctuation with a space. '\W' refers to matching any non-word 
    defined by regex and '+' refers to matching more than one non-words
    '''
    soup = BeautifulSoup(html_text, 'html.parser')
    soup_text = soup.get_text()

    cleaned_text = re.sub(r'\W+', ' ', soup_text)

    return cleaned_text   

def write_clean_html_text_files(input_folder, dest_folder):
    '''
    Function reads the files in the input folder and and calls the clean_html_text function
    and stores a text file in the destination directory.
    
    '''
    for filename in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, filename)
        new_name = filename.split('.')
        
        with open(input_file_path,'r' ,encoding="utf8") as f:
            html_text = f.read()
            cleaned_text = clean_html_text(html_text)
            
        dest_filename = f'{new_name[0]}.txt' 
        dest_file_path = os.path.join(dest_folder, dest_filename)
    
        
        with open(dest_file_path, 'w') as f:
            f.write(cleaned_text)

    
    
            