import xlsxwriter
newxle=xlsxwriter.Workbook("untitle.xlsx")
filo1=newxle.add_worksheet("filo1")
stiles=int(input("Πόσες στήλες θέλετε να προσθέσετε στο excel αρχείο σας"))
apantisi=input("Θέλετε να προσθέσετε τίτλος   y ή n")
# doymioytgi toy titloys
if apantisi=='y':
    titlos=input("Γράψε τους τίτλους με , αναμεσά")
    titlos=titlos.split(",")
    print(titlos)
    while len(titlos)<stiles:
        print("Δώσατε μικρότερο αριθμό τίτλων από τον αριθμό στηλών")
        titlos=input("Γράψε τους τίτλους με , αναμεσά")
        titlos=titlos.split(",")
    for j in range(len(titlos)):
        filo1.write(0,j,titlos[j])
#eos edo
# ----
# perna tis times        
x=0
while x<stiles:
    sigetrosi_soston=[]
    apantisi=input("Πληκτρολόγησε 1 για προσθήκη αριθμόν στα κελιά 2 για προθήκη δεκαδικών στα κελιά και 3 για προθήκη κείμενου στα κελιά \n")
    if apantisi=='1':
        times=input("Πληκτρολογήστε της τιμές ακέραιον αριθμόν με , αναμεσά σαν διαχωριστικό")
        times=times.split(",")
        for j in range(len(times)):
            try:
                times[j]=int(times[j])
            except ValueError:
                continue
                
        for ar in times:
            if type(ar)==int:
                sigetrosi_soston.append(ar)
        if len(sigetrosi_soston)>0:
            times=sigetrosi_soston
            
                           
    elif apantisi=='2':
        times=input("Πληκτρολογήστε της τιμές δεκαδικών αριθμόν με κενό αναμεσά σαν διαχωριστικό")
        times=times.split(" ")
        print(times)
        for i in range(len(times)):
             times[i]=times[i].replace(",",".")
        print(times)
        for g in range(len(times)):
            try:
                times[g]=float(times[g])
            except ValueError:
                print("Οι τιμή που πληκτρολογήσατε είναι λάθος θα παραληφθεί στην καταχώρηση ")
                continue
        for ar in times:
             if type(ar)==float:
                  sigetrosi_soston.append(ar)
        print(sigetrosi_soston)          
        if len(sigetrosi_soston)>0:
             times=sigetrosi_soston
                       
                
    elif apantisi=='3':
        times=input("Πληκτρολογήστε τα κείμενα σας με , αναμεσά για διαχωριστικό")
        times=times.split(",")
             
         
    for i in range(len(times)):
        filo1.write(i+1,x,times[i])
    x+=1        
    #eos edo
    

newxle.close()


