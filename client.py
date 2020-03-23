import requests
import json
#import raw_intput
s=requests.session()
def list():
    r = s.get('http://localhost:8000/list/')
    instance=r.text.replace('[','')
    instance=instance.replace(']','')
    l=[]
    i=0
    j=0
    tag=' '
    print('Code'+tag*13+'Name'+tag*14+'Year Semester  Taught by')
    while(len(instance)):
        j=instance.find('{')
        i=instance.find('}')
        l.append(instance[j+1:i])
        instance=instance[i+1:]
    for ll in l:
        lll=[]
        k=10
        while(len(ll)and k>0):
            j=ll.find(':')
            i=ll.find('"',j+2)
            lll.append(ll[j+1:i])
            ll=ll[i+1:]
            k-=1
        for i in range(len(lll)):
            lll[i]=lll[i].replace('"','')
        lll[2]=lll[2].replace(',','')
        lll[3]=lll[3].replace(',','')
        print(lll[0]+'  '+lll[1]+tag*(30-len(lll[1]))+lll[2]+'    '+lll[3]+'     '+lll[4]) 
    
    
def view():
    r = s.get('http://localhost:8000/view/')
    text = json.loads(r.text)
    for t in text:
        print('The rating of Professer '+ t['Name']+ ' is:'+ '*'*int(t['Rate']))
def average():
    name = input("Enter the Module Code:")
    pro = input("Enter the Professor Id:")
    r=s.post('http://localhost:8000/avr/',data={'name':name,'professor':pro})
    text = json.loads(r.text)
    t=text[0]
    #for t in text:
    print('The rating of Professor '+t['Professor'] +' in module '+t['Name']+' is'+'*'*int(t['Rate']))
def add():
    name = input("Enter the Module Code:")
    pro = input("Enter the Professor Id:")
    y = int(input("Enter the Year:"))
    ss = int(input("Enter the Semester:"))
    r = int(input("Enter the rate(1-5):"))
    r=s.post('http://localhost:8000/add/',data={'name1':name,'professor':pro,'y':y,'ss':ss,'r':r})
    print(r.text)
def register():
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    r=s.post('http://localhost:8000/register/',data={'name':username,'pwd':password})
    print(r.text)
def login():
    
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    r=s.post('http://localhost:8000/login/',data={'name':username,'pwd':password})
    print(r.text)
def logout():
    r = s.get('http://localhost:8000/logout/')
    print(r.text)
def test():
    r= s.get('http://localhost:8000/test/')
    print(r.text)
if __name__ == '__main__':
    command=['register','login','logout','list','view','avr','rate','end','help','test']
    print('client start!')
    print('Input "help" for all suppored operations!')
    while(1):
        co = input("Enter your command: ")
        if co==command[8]:
            
            print(command)
            continue
        elif co==command[7]:
            print('exit the client!')
            break
        elif co==command[0]:
            register()
        elif co==command[1]:
            login()
        elif co==command[2]:
            logout()
        elif co==command[3]:
            list()
        elif co==command[4]:
            view()
        elif co==command[5]:
            average() 
        elif co==command[6]:
            add()
        elif co==command[9]:
            test()
        else:
            print('the command is invalid, the valid command is as follows:')
            print(command)
    
