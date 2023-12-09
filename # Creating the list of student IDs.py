company_list=[["01","2110987","Bashundhara Group",100000],
  ["02","8363564","BEXIMCO",0],
  ["03","6455372","Abul Khair  Group",0],
  ["04","3654538","Navana Group",100000],
  ["05","9575643","Ananda  Group",0],
  ["06","7593759","City Group",0],
  ["07","7454839","Square  Group",0],
  ["08","9304754","Akij Group",100000],
  ["09","6364383","PRAN-RFL  Group",200000],
  ["10","7465748","Grameenphone",0]]

new_company_list = []

def add_company():
  while True:
    id = input('Enter company id: ')
    if len(id) < 7:
      print("Uh oh! Looks like the ID isn't long enough. Maybe you missed a digit?")

    else:
      for i in range(len(company_list)):
        if company_list[i][1] == id:
          print('This ID is already in use. Please try again.')
        else:
          new_company_list.append(str(len(company_list)+1))
          new_company_list.append(id)
          break
    

    
  while True:
    name = input("Enter Company Name: \n")
    for i in range(len(company_list)):
      if company_list[i][2] == name:
        print("Seems like this name is already associated with another company. Please enter a different name.")
      else:
        new_company_list.append(name)
        new_company_list.append(int(input("Enter Donation Amount: ")))
        company_list.append(new_company_list)
    break
 

  



add_company()

def printlist(x):
  print("\n")
  print("{0:18}{1:18}{2:24}{3:18}".format("Company number", "Company ID", "Company name", "Donation amount"))
  print("\n")
  for i in range(len(x)):
     print("{0:18}{1:18}{2:24}{3:15}".format(x[i][0], company_list[i][1], x[i][2], x[i][3]))


printlist(company_list)