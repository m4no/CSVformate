import csv
import uuid
import datetime

csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_NONE)
csv.register_dialect('myDialectOut', delimiter=',', quoting=csv.QUOTE_ALL, lineterminator='\n')

def save_csv(fnameIn, inOrEx, fnameOut, inNum):
   with open(fnameIn, newline='', encoding='utf-8') as myFileIn:
        reader = csv.reader(myFileIn, dialect='myDialect')
    #    for row in reader:
    #        print(row)
        today = date.today()
        myFile = open(fnameOut, 'a', encoding='utf-8')
        with myFile:
            myFile.write("\"Windows Excel","AndroMoney",{}\n
"Id","Currency","Amount","Category","Sub-Category","Date","Expense(Transfer Out)","Income(Transfer In)","Note","Periodic","Project","Payee/Payer","uid","Time\"" % today.strftime("%Y%m%d"))
            writer = csv.writer(myFile, dialect='myDialectOut')
            i = inNum
            for row in reader:
                finalrow = []
                i +=1
                finalrow.append(f'{i}')
                finalrow.append('EUR')
                finalrow.append(row[1])
                if inOrEx == 'Income':
                    finalrow.append(inOrEx)
                    finalrow.append(row[2])
                    finalrow.append((datetime.datetime.strptime(row[0], '%m-%d-%Y')).strftime("%Y%m%d"))
                    finalrow.append('')
                    finalrow.append('Bank')
                else:
                    finalrow.append(row[2])
                    finalrow.append('')
                    finalrow.append((datetime.datetime.strptime(row[0], '%m-%d-%Y')).strftime("%Y%m%d"))
                    finalrow.append('Bank')
                    finalrow.append('')
                finalrow.append(row[3])
                finalrow.append('')
                finalrow.append('')
                finalrow.append('')
                finalrow.append(uuid.uuid4().hex)
                finalrow.append('')
                writer.writerow([item.strip() for item in finalrow])
            return i

save_csv('Expenses.csv', 'Expenses', 'AndroMoney.csv', (save_csv('Income.csv', 'Income', 'AndroMoney.csv', 0)))
