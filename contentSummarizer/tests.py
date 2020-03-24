from django.test import TestCase
from werkzeug.utils import secure_filename
import docx2txt
path = 'media/'
file_name ='Draft format of a TENANCY_AGREEMENT.docx'
file = path+file_name
print(file)
MY_TEXT = docx2txt.process(file)
print(MY_TEXT)
# Create your tests here.
