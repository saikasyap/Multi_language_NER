# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import spacy

def Multilang_NER(text, language_code):
    # Use a breakpoint in the code line below to debug your script.
    #print(f"Text is: {text}")  # Print text
    result =[]
    nlp = spacy.load(language_code+ '_core_web_sm')
    doc = nlp(text)


    for i in doc.ents:
        result.append({'text':i.text,'type': i.label_,'start_pos': i.start_char, 'end_pos': i.end_char })
    return result



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(Multilang_NER('My name is Kasyap, nice to meet you.', 'en'))

