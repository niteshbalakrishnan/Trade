import csv
import NSE_Trade.Database

def stock_detail_insert( ):
    db = NSE_Trade.Database
    d = db.database()
    d.connect()
    filename = "C:\\Nitesh\\SECURITY LIST.csv"
    with open(filename, newline='') as csvfile:
        sp = csv.reader(csvfile)
        i = 1
        for row in sp:
            print("row 0" + row[0])
            st = 'Insert into stock_detail values(' + "'" + row[0] + "','"+ row[2] + "',"
            st = st + row[6] + ",'" + row[7]  + "','" +row[8] + "',"+ str(0)+","+str(0)+",'"+row[9]+"','"+row[10]+"'"
            st = st + ")"
            if i > 2:
                 d.insert(st)
            else:
                i = i + 1
    return 1

stock_detail_insert()