from bs4 import BeautifulSoup
import re
import os
import re
from nltk.corpus import stopwords 
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer

def clean_html_text(html_text):
    '''
    Function uses BeautifulSoup to parse html text and replaces any tags
    or punctuation with a space. '\W' refers to matching any non-word 
    defined by regex and '+' refers to matching more than one non-words
    '''
    soup = BeautifulSoup(html_text, 'html.parser')
    soup_text = soup.get_text()
    return_list = []
    stopword_list = stopwords.words('english')

    cleaned_text = re.sub(r'\W+', ' ', soup_text.lower())
    clean_text_tokenized = word_tokenize(cleaned_text)
    
    for i in stopword_list:
        if i in clean_text_tokenized:
            clean_text_tokenized.remove(i)
            
    lemmatizer = WordNetLemmatizer()
    clean_text_lemmatized = [lemmatizer.lemmatize(j) for j in clean_text_tokenized]
    regex = re.compile(r'\d+')
    no_numbers = [item for item in clean_text_lemmatized if not regex.search(item)]
    no_letters = [word for word in no_numbers if len(word) != 1]
    

    result = ' '.join(no_letters)
    
    return result

def write_clean_html_text_files(input_folder, dest_folder):
    '''
    Function reads the files in the input folder and and calls the clean_html_text function
    and stores a text file in the destination directory.
    
    '''
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    for filename in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, filename)
        new_name = filename.split('.')
        
        with open(input_file_path,'r' ,encoding="utf8") as f:
            html_text = f.read()
            cleaned_text = clean_html_text(html_text)
            
        dest_filename = f'{new_name[0]}.txt' 
        dest_file_path = os.path.join(dest_folder, dest_filename)
    
        os.remove(input_file_path)
        with open(dest_file_path, 'w') as f:
            f.write(cleaned_text)
