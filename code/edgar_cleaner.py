from bs4 import BeautifulSoup
import re
import os
import re
from nltk.corpus import stopwords 
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer

def clean_html_text(html_text):
    """Function uses BeautifulSoup to parse html text and replaces any tags
    or punctuation with a space and performs NLP for data analysis later.

    Args:
        html_text (str): html string from the website

    Returns:
        result (str): string containing all the words from the website after NLP
    """    
    
    # Uses BeautifulSoup to get all the text from the html provided
    soup = BeautifulSoup(html_text, 'html.parser')
    soup_text = soup.get_text()
    
    # List containing all the stopwords in the english dictionary
    stopword_list = stopwords.words('english')

    # Removes all puncutation, makes everything lower case and tokenizes the text
    cleaned_text = re.sub(r'\W+', ' ', soup_text.lower())
    clean_text_tokenized = word_tokenize(cleaned_text)
    
    # Removes all the stopwords from the text
    for i in stopword_list:
        if i in clean_text_tokenized:
            clean_text_tokenized.remove(i)
    
    # Lemmatizes the text
    lemmatizer = WordNetLemmatizer()
    clean_text_lemmatized = [lemmatizer.lemmatize(j) for j in clean_text_tokenized]
    
    # Removes all the numbers and letters from the text
    regex = re.compile(r'\d+')
    no_numbers = [item for item in clean_text_lemmatized if not regex.search(item)]
    no_letters = [word for word in no_numbers if len(word) != 1]
    
    # Joins the cleaned tokenized list into a large string and returns it
    result = ' '.join(no_letters)
    
    return result

def write_clean_html_text_files(input_folder, dest_folder):
    """
    Function reads the files in the input folder and calls the 
    clean_html_text function and stores a text file in the destination 
    directory

    Args:
        input_folder (str): directory to obtain the html links
        dest_folder (str): directory to save all the text documents.
    """    
    
    # If the destination folder does not exists, it creates it
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    # Obtains each file from the input folder
    for filename in os.listdir(input_folder):
        
        # Generates directory to dsave the file
        input_file_path = os.path.join(input_folder, filename)
        new_name = filename.split('.')
        
        # Uses clean_html_text() to perform NLP
        with open(input_file_path,'r' ,encoding="utf8") as f:
            html_text = f.read()
            cleaned_text = clean_html_text(html_text)
        
        # Creates destination path to save the txt
        dest_filename = f'{new_name[0]}.txt' 
        dest_file_path = os.path.join(dest_folder, dest_filename)

        # Deletes the original html file to save storage space
        os.remove(input_file_path)
        
        # Saves the txt file
        with open(dest_file_path, 'w') as f:
            f.write(cleaned_text)
