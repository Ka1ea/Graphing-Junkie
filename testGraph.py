
import pickle
import sqlite3
import os

conn = sqlite3.connect("/Users/catherinepark/Documents/boilermake/grapher.db")
c = conn.cursor()
c.execute("SELECT sum(field4) as count, field3 as date from Films group by field3")
tables = (c.fetchall())
for i in range(0, len(tables)):
    fig = pickle.loads(tables[i][0])
    fig.savefig(str(i)+'.png')
print("The plots are saved in directory: ",os.getcwd())

# data = pandas.read_sql(sql, conn)
# #x values: data.Country,  y values: data.sum_deaths
# plt.bar(data.Country, data.sum_deaths)
# plt.title("SARS Death in 2003")
# plt.show()

# cnxn = pyodbc.connect('DRIVER=SQL Server;SERVER={SERVER_NAME};DATABASE={DB_NAME};UID={USER_NAME};PWD={PASSWORD}')
# cursor = cnxn.cursor()
# cursor.execute("EXECUTE [dbo].[PyPlotMatplotlib]")
# tables = cursor.fetchall()
# for i in range(0, len(tables)):
#     fig = pickle.loads(tables[i][0])
#     fig.savefig(str(i)+'.png')
# print("The plots are saved in directory: ",os.getcwd())