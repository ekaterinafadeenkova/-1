class Contact:
    def __init__(self, name, phone, mail):
         self.name = name
         self.phone = phone
         self.mail = mail
class Contacts:
    def __init__(self):
        self.bd = [[],[],[],[],[],[]]

    def __add__(self, contact):
        self.bd[0].append(len(self.bd[0])+1)
        fio = contact.name.split(" ")
        while len(fio)<3:
            fio.append(None)
        self.bd[1].append(fio[0])
        self.bd[2].append(fio[1])
        self.bd[3].append(fio[2])
        if contact.phone !='':
            seld.bd[4].append(contact.phone)
        else:
            self.bd[4].append(None)
        if contact.mail != '':
            self.bd[5].append(contact.mail)
        else:
            self.bd[5].append(None)
    def getContact(self, iD):
        ans = "ID: " + str(self.bd[0][iD])+"\n"
        ans += "ФИО: "+self.bd[1][iD]
        if self.bd[2][iD]!= None:
            ans += " " + self.bd[2][iD]
        if self.bd[3][iD]!= None:
            ans += " " + self.bd[3][iD]
        if self.bd[4][iD]!= None:
            ans += "\n" + "Номер телефона: " + self.bd[4][iD]
        else:
            ans += "\n" + "Номер телефона: " + "нет"
        if self.bd[5][iD]!= None:
            ans += "\n" + "Почта: " + self.bd[5][iD] + "\n"
        else:
            ans += "\n" + "Почта: " + "нет" + "\n"
        return ans
    def phoneSearch(self, phone):
        if self.bd[4].__contains__(phone):
            id = self.bd[4].index(phone)
            print(self.getContact(id))
        else:
            print("Ничего не найдено")
            
    def mailSearch(self, mail):
        if self.bd[5].__contains__(mail):
            id = self.bd[5].index(mail)
            print(self.getContact(id))
        else:
            print("Ничего не найдено")
            
    def search(self, fio):
        ids = []
        if fio[0] != None:
            for i in range(len(self.bd[1])):
                if fio[0] == self.bd[1][i]:
                    ids.append(self.bd[0][i]-1)
        if fio[1]!= None:
            if fio[0]!= None:
                for id in ids:
                    if fio[1] != self.bd[2][id]:
                        ids.remove(id)

            else:
                for i in range(len(self.bd[2])):
                    if fio[1] == self.bd[2][i]:
                        ids.append(self.bd[0][i] - 1)
        if fio[2]!=None:
            if fio[0]!= None or fio[1]!=None:
                for id in ids:
                    if fio[2] != self.bd[2][id]:
                        ids.remove(id)

            else:
                for i in range(len(self.bd[3])):
                    if fio[2] == self.bd[3][i]:
                        ids.append(self.bd[0][i] - 1)

        if len(ids)==0:
            print("Ничего не найдено")
        else:
            for id in ids:
                print(self.getContact(id))

    def getWithoutPhoneOrMail(self, num):
        if num == 1:
            for i in range(len(self.bd[4])):
                if self.bd[4][i] == None:
                    print(self.getContact(i))
            return
        if num == 1:
            for i in range(len(self.bd[5])):
                if self.bd[5][i] == None:
                    print(self.getContact(i))
            return
        if num == 1:
            for i in range(len(self.bd[4])):
                if self.bd[4][i] == None and self.bd[5][i] == None:
                    print(self.getContact(i))
            return
        
     def change(self, id, contact):
         id -=1
         fio = contact.name.split(" ")
         while len(fio)<3:
             fio.append(None)
        self.bd[1][id] = fio[0]
        self.bd[2][id] = fio[1]
        self.bd[3][id] = fio[2]
        self.bd[4][id] = contact.phone if len(contact.phone)>0 else None
        self.bd[5][id] = contact.mail if len(contact.mail)>0 else None

     def printAll(self):
         for i in range(len(self.bd[0])):
             print(self.getContact(i))
def printCommands():
    print("Список всех доступных команд: ")
    print("1 - Показать все контакты", "2 - Поиск по номеру телефона", "3 - Поиск по электронной почте", "4 - Поиск по отсутсвию номера телефона или почты", "6 - Изменить какой-то контакт", "7 - Остановить работу программы", sep = "\n"

print("Введите название файла")
fileName = input()
file = open(fileName, encoding = 'utf-8')
base = Contacts()
for st in file:
          arr = st.split(",")
          contact = Contact(arr[0], arr[1].replace(" ", ""), arr[2].replace(" ", "").replace("\n", ""))
          base.__add__(contact)
print("База сформирована")
printCommands()
ab = int(input())
while ab!="jefjuwe2@4":
    if ab==1:
        base.printAll()
    elif ab == 2:
        print("Введите номер телефона")
        phone = input()
        base.phoneSearch(phone)
    elif ab == 3:
        print("Введите адрес электронной почты")
        mail = input()
        base.mailSearch(mail)
    elif ab == 4:
        fio = []
        print("Введите фамилию или оставьте строку пустой")
        f = input()
        if f== '':
            fio.append(None)
        else:
            fio.append(f)
            
        print("Введите имя или оставьте строку пустой")
        i = input()
        if f== '':
            fio.append(None)
        else:
            fio.append(i)

        print("Введите отчество или оставьте строку пустой")
        o = input()
        if f== '':
            fio.append(None)
        else:
            fio.append(o)
        base.search(fio)
    elif ab == 5:
        print("Введите параметр, по которому хотите искать: ", "1 - без номера телефона", "2 - без адреса электронной почты", "3 - без номера и без почты")
        num = int(input()
        base.getWithoutPhoneOrMail(num)
    elif ab == 6:
        print("Введите id контакта, который хотите изменить, а также новые данные, которые хотите в него добавить", "(в две разные строки)", sep = "\n"
        id = int(input())
        q = input().split(",")
        contact = Contact(q[0], q[1].replace(" ", ""), q[2].replace(" ", "").replace("\n", ""))
        base.change(id, contact)
    elif ab == 7:
        "Вы закрыли программу"
        break
    print()
    printCommands()
    ab = int(input())
     
            
            
 
          
          
          
          
          
         
        
                
                
            
                        
            
        
    
            
           
            
        
        
         
            
        
        
    

         
