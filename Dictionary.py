from bs4 import BeautifulSoup
import requests



class WordInterpretation:
    
    @staticmethod
    def getdata(URL):
        

    
        page = requests.get(str(URL))

     
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.body#find(id='top')
        results=soup.find(class_='termDefintion')
       # print(results)
        results=results.getText()
        results=(str(results).strip())
        return(results)
        
    @staticmethod
    def getMeaning(word):
        
        meaning=WordInterpretation.getdata("https://www.arabdict.com/ar/"+"عربي-عربي/"+str(word))
        return(meaning)
        

print(WordInterpretation.getMeaning("عشب"))