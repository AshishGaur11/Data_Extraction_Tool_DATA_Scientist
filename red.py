
#Web scraping Engine for DATA Science

import subprocess
from bs4 import BeautifulSoup
import lxml
import requests
from requests.models import Response
import urllib.parse

import urllib



class prec:
    
    def __init__(self,data):
        self.data = data
        self.next = None 
        
class linkedlist:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self,data):
        new_node = prec(data)
        if self.head == None:
            self.head = new_node
        if self.tail != None:
            self.tail.next = new_node
        self.tail = new_node
    
    def delete(self,index):
        pre = None 
        node = self.head
        i = 0
        
        while node != None and i < index :
            pre = node
            node = node.next
            i = i + 1
            
        if pre == None:
            self.head = node.next
        else:
            pre.next = node.next
            
    def show(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next 
    

if __name__=="__main__":
    
    qlist = linkedlist()


    def push():
    
       w = (input("Enter Task\n"))
       qlist.add(w)
       main()
    
    def pop():
    
        q = int(input("Tasks are remove by positions----\n"))
        qlist.delete(q-1)
        main()    
        
    def display():
    
        print("your entries are down here----\n")
        qlist.show()
        main()


    def subdomains(werq):
        
        target_url = werq
        with open("q.txt","r") as wordlist_file:
            for line in wordlist_file:
                word = line.strip()
                test_url = word + "." + target_url
                Response = request(test_url)
                if Response:
                    print("[+] Discovered URL -->", test_url)
                else:
                    main()
        main()


    
    def subfiles(wer):
        
        target_url = wer
        with open("q.txt","r") as wordlist_file:
            for line in wordlist_file:
                word = line.strip()
                test_url = target_url + "/" + word
                Response = request(test_url)
                if Response:
                    print("[+] Discovered URL -->", test_url)
                else:
                    main()
        main()


    def request(url):
        try:
            return requests.get("https://" + url)
        except request.exceptions.ConnectionError:
            pass

    def whole(url):
        target_url1 = url
        Response = request(target_url1)
        print(Response.content)
        main()

    
    def webscreper(data):
        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 "
        }
        params = {'q': data}
        html = requests.get(f'https://www.google.com/search?q=', headers=headers, params=params).text
        soup = BeautifulSoup(html, 'lxml')
        for container in soup.findAll('div', class_='RnJeZd top pla-unit-title'):
            title = container.text
            startOfLink = 'https://www.googleadservices.com/pagead'
            endOfLink = container.find('a')['href']
            ad_link = urllib.parse.urljoin(startOfLink, endOfLink)
            print(f'{title}\n{ad_link}\n')
        main()

    def req(e):
        r = requests.get("https://"+e)
        print(r.status_code)
        print(r.ok)
        main()

    def add_links(data):
        headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582"
        }
        params = {'q': data}
        html = requests.get(f'https://www.google.com/search?q=',
                    headers=headers,
                    params=params).text
        soup = BeautifulSoup(html, 'lxml')
        for container in soup.findAll('span', class_='Zu0yb LWAWHf qzEoUe'):
            ad_link = container.text
            print(ad_link)
        main()

    
    def main(): 
    
        print("\nWelcome to MortalBit web scraping engine with task list for Information gathering in data science--\n")
        print("Author & Writer Ashish Gaur")
        print("\nPress the value to perform those functions in down there--\n")
        print("1 for insert Task.")
        print("2 for remove Task.")
        print("3 for display Task.")
        print("4 get status.")
        print("5 To get Subdomains")
        print("6 To get Subfiles")
        print("7 get the whole content HTML, CSS, JavaScript")
        print("8 Get all advertisement")
        print("9 Get all the links")



        print("press q & Enter--\n")
        
        
        n = input()
        while True  :
            if n == '0':
                main()
            elif n == '1':
                push()
            elif n == '2':
                pop()
            elif n == '3':
                display()

            elif n == '4':
                A1 = input("Enter resource value(wibsite's  IP)\n")
                req(A1) 

            elif n == '5':
                A1 = input("Enter website (or IP)\n")
                subdomains(A1)     

            elif n == '6':
                A1 = input("Enter website (or IP)\n")
                subfiles(A1)

            elif n == '7':
                A1 = input("Enter website (or IP)\n")
                whole(A1)

            elif n == '8':
                A1 = input("Enter whatever you want to search on google for advertisement collection(or IP)\n")
                webscreper(A1)   

            elif n == '9':
                A1 = input("Get all Links available on google\n")
                add_links(A1)
            elif n == 'q':
                print("Hope your expireance was good!!")
                break
            else :
                print("sorry does'nt work")
                main()

    main()












