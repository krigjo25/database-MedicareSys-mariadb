#   Python Libraries
import datetime
from os import getenv

#   Third party libraries
from dotenv import load_dotenv
load_dotenv()

#   Internal Libraries
from lib.database_connection import MariaDB


class Calculators():

    def __init__(self): pass

    def CalculateAge(self, birthDate:datetime.date) -> int:

        '''         calculateAge     
        
            Calculates the age difference between the current
            date and the given date

            The leap year is added 

        '''

        #   Converting the date into a string, then back to a date
        birthDate:str = str(birthDate)
        birthDate:datetime.date = datetime.datetime.strptime(birthDate, '%Y-%d-%m').date()

        #   Get the today's date
        today = datetime.date.today()

        #   Calculate the difference in years
        difference = today.year - birthDate.year  
        oneOrZero = ((today.month, today.day) < (birthDate.month, birthDate.day))

        #   Age equals the difference - one or zero
        return difference - oneOrZero

    def Calculatebmi(self, kg:int, cm:int, age:int, gender:str) -> str:

        #   Convert heights
        m = cm / 100

        #   Finds the bmi by dividing  with age and gender
        bmi: float = 0
        if age < 21 and gender == 'M': bmi = kg / (m * m) * 10000

        elif age < 21 and gender == 'F': bmi = kg / (m * m) * 10000

        elif age > 20 and gender =='F': bmi = kg / (m * m)
        else: bmi = kg / (m * m)

        bmi = round(bmi, 2)

        # Checking the body's condition
        #   Checking if the bmi is below 18.5
        message:str = ''
        if bmi < 18.5: message = f'{bmi}, UW'

        #   Checking if the bmi is equal to 18.5 or above
        elif bmi == 18.5 and bmi < 25.1: message = f'{bmi}, N' # Normal

        #   Checking if the bmi is equal 25.0 or above 18.5
        elif bmi > 25.0 and bmi < 30.0: message = f'{bmi}, OW'
            
        #   Checking if the bmi is equal 25.0 or above 18.5
        elif bmi > 30.0: message = f'{bmi}, Obese'

        return message

class Converters():

    '''         Converters   

        TrimValues
            Trimming valuesCalculate a age type : yyyy-dd-mm

    '''

    def __init__(self): pass

    def TrimValue(self, kwarg: list, kwargs: str) -> str:

        kwarg = str(kwarg[0:3]).split("-")

        kwargs = str(kwargs).replace("-", "")
        kwargs = str(kwargs[5:9])

        result = kwarg + kwargs

        return result

class Dictionaries():

    def __init__(self): pass

    def AmericanPostalCodes(self, zip_code: int) -> str:

        '''         AmericanPostalCodes

            In life there would be an api for this
            so we leave it as an demostration.
            
            AmericanPostalCodes, lists of given 
            postalcodes in america.
        '''

        #   Creating a list to walk through
        zip_map = { 0000:'Warshington' }

        return zip_map.get(zip_code) or 'Not found'

class UploadFile():
    def __init__(self):

        self.dc = MariaDB
        self.database: str = getenv('database2', '')

    def BinaryConverter(self, fName: str) -> bytes:

        #   Converting data to binary format
        with open(fName, 'rb') as file:
            binaryData = file.read()
            
        return binaryData

    def generateBlob(self, query: str, path: str) -> bytes:
        file: bytes = self.BinaryConverter(path,)
    
        #   Converting information into tuple
        query_tuple: tuple = (query, path)
        self.dc.upsert_table(self.database, query_tuple)

        return file

    def generatePDF(self, pdf: str, path: str) -> bytes:

        query: str = f' UPDATE patient SET pdf = "{pdf}" WHERE id = 100'
        return self.generateBlob(query, pdf)


