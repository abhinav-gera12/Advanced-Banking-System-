import mysql.connector as SQL
import procedual 
from banking import BankAccount


try:
    conn = SQL.connect(
        user ='root',
        password = "Abhi@12!",
        host = "localhost",
        port = 3306
    )
except Exception as e:
    print("cannot connect")
else:
    print("connected")




# # 1-> cur.execute("CREATE DATABASE banking")
# cur.execute("USE banking")
# cur.execute('''
#             CREATE TABLE IF NOT EXISTS records
#             (
#                 account_no INT PRIMARY KEY,
#                 name VARCHAR(100),
#                 age INT NOT NULL,
#                 gender VARCHAR(10), 
#                 phone_number INT,
#                 pin INT,
#                 balance FLOAT NOT NULL
#             )
#             ''')


# sql_query = '''INSERT INTO records
#                 (account_no,name,age,gender,phone_number,pin,balance)
#                 VALUES(%s,%s,%s,%s,%s,%s,%s)
#             '''



    
# try:
#     while procedual.new_customer():
#         cur.execute(sql_query,((BankAccount.account_number-1),procedual.name,procedual.age, procedual.gender,procedual.phone_number,procedual.pin,BankAccount.balance))
#         conn.commit()
#         print("-"*50)

# except Exception as error:
#     conn.rollback()
#     print("Something went wrong.",error)



    
# cur.close()
# conn.close()


# #   2- Adding data to the records table
# #   try:
# #       cur.execute(sql)
# #       conn.commit()
# #       print("Successfully data inserted into the records")
# #       print(f"{cur.rowcount} total data updated")
# #   except Exception as error:
# #       conn.rollback()
# #       print("Something went wrong.")
# #   cur.close()

# # **************************************************************


# #     3- Updating and deleting data from records
# #     sql1 = "UPDATE records SET name = 'Arun' WHERE account_no = 101"
# #   sql2 = "DELETE FROM records WHERE account_no= 101"

# #   try:
# #       cur.execute(sql1)
# #       conn.commit()
# #       print(f"{cur.rowcount} data updated successfully")
# #       cur.execute(sql2)
# #       conn.commmit()
# #       print(f"{cur.rowcount} data successfully deleted")

# #   except:
# #       conn.rollback()
# #       print("Something Went Wrong")