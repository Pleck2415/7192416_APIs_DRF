import pyodbc 
cnxn = pyodbc.connect(
    'Driver={ODBC Driver 18 for SQL Server};Server=tcp:sqlsrv-plecksolution-prod-cc.database.windows.net,1433;Database=sqldb-plecksolution-prod;Uid=pleckadmin;Pwd=pMlm001_Az!;Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=30;'
    )

cursor = cnxn.cursor()
cursor.execute("INSERT INTO dbo.Users (id, userName, email, firstName, lastName) VALUES (4, 'dex_jaune', 'dexter.morgane@gmail.com', 'Dexter', 'Morgane')")
# cursor.execute("UPDATE dbo.Users SET firstName='Marie-Josée_User' WHERE id=3")
cnxn.commit()

cursor = cnxn.cursor()	
cursor.execute("SELECT * FROM dbo.Users") 
row = cursor.fetchone() 
while row:
    print (row) 
    row = cursor.fetchone()
