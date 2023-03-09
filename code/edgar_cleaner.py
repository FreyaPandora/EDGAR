import os
import requests
import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer

def clean_html_text(html_text):
    '''
    Function uses BeautifulSoup to parse html text and replaces any tags
    or punctuation with a space. '\W' refers to matching any non-word 
    defined by regex and '+' refers to matching more than one non-words
    '''

    user_agent = r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    response = requests.get(html_text, headers={'User-Agent':user_agent})
    soup = BeautifulSoup(response.content, 'html.parser')

    if soup.find('document'):
        paragraphs = soup.find_all('p')
    else:
        paragraphs = soup.find_all('span')

    stopword_list = stopwords.words('english')

    return_list = []
    for p in paragraphs:
        if not p.find_previous('h1'):
            text = p.get_text(strip=True)
            clean_text = re.sub(r'[^A-Za-z0-9]', ' ', text.lower())
            clean_text_tokenized = word_tokenize(clean_text)
            for i in stopword_list:
                if i in clean_text_tokenized:
                    clean_text_tokenized.remove(i)
            lemmatizer = WordNetLemmatizer()
            clean_text_lemmatized = [lemmatizer.lemmatize(j) for j in clean_text_tokenized]
            
            regex = re.compile(r'\d+')
            
            no_numbers = [item for item in clean_text_lemmatized if not regex.search(item)]
            
            no_letters = [word for word in no_numbers if len(word) != 1]
            if len(no_letters) > 8:
                return_list.append(no_letters)
            
    result = '\n'.join([' '.join(inner_list) for inner_list in return_list])
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
    
        
        with open(dest_file_path, 'w') as f:
            f.write(cleaned_text)

    
    
            