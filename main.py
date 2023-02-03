from gtts import gTTS
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

def convert_pdf_to_audio(path, language, output_file):
    manager = PDFResourceManager()
    file_string = StringIO()
    converter = TextConverter(manager, file_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    with open(path, 'rb') as file:
        for page in PDFPage.get_pages(file, check_extractable=True):
            interpreter.process_page(page)

    text = file_string.getvalue()
    file_string.close()
    converter.close()
    print(f'Text for "{path}" is ready')
    print('Now converting text into audio')

    output = gTTS(text=text, lang=language, slow=False)
    output.save(output_file)
    print('Done')

pdf_file = 'book.pdf'
language = 'ru'
output_file = 'output.mp3'

convert_pdf_to_audio(pdf_file, language, output_file)
