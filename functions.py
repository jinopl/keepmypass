import os
import sqlite3
import getpass
import random
import string
from sqlite3 import Error
from prettytable import PrettyTable
from password_generator import PasswordGenerator

sql_file ="forget.db"  

def create_connection(db_file):
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)
 
	return None

def filechk(Name):
	if not os.path.exists(Name):
	   return True	


def intialsetup():
	
	   
	if not os.path.exists('forget.db'):
		os.mknod('forget.db')

	create_data="""CREATE TABLE `data` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`tag`	BLOB NOT NULL,
	`uname`	BLOB,
	`pswd`	BLOB);"""
	conn = create_connection(sql_file)
	if conn is not None:
		sql_execute(conn,create_data)
	else:
		print("error")


def sql_execute(conn, sqlquery):
	""" create a table from the create_table_sql statement
	:param conn: Connection object
	:param create_table_sql: a CREATE TABLE statement
	:return:
	"""
	try:
		handle = conn.cursor()
		handle.execute(sqlquery)
	except Error as e:
		print(e)


def caller():
	global conn 
	conn = create_connection(sql_file)
	
	while True:
		print(" ===========================")
		print(" 1. Create a new entry")
		print(" 2. Search data ")
		print(" 3. Create random password for me  ")
		print(" 4. Delete entry  ")
		print(" 5. Exit  ")
		print(" ===========================")
		option = input("Enter your option ? :")

		if option == "1":
			insert()
		elif option == "2":
			if checkdata() is False :
				print("No records, please create some ! ")
			else:
				selectdata()
		elif option == "3":
			print(id_generator())
		elif option == "4":
			delete()
		if option == "5":
			break


def insert():
	tag = input("Enter tag for this account : ")
	uname = input("Enter user name for this account : ")
	option = input("Do you want me to create a password for you ? [Secure] ? [y/n]")

	if option == 'y':
		password = id_generator()
		print ("your strong password is : {} ".format(password))
		print("Account added !")
		
	else:
		password = getpass.getpass("Enter password : ")
	
	data = (tag,uname,password)
	handle = conn.cursor()
	handle.execute('insert into data (tag,uname,pswd) values (?,?,?)', data)
	conn.commit()

def all_tags():
	handle = conn.cursor()
	handle.execute('select distinct tag from data')
	records = handle.fetchall()
	t = PrettyTable(['Tags'])
	for row in records:
		t.add_row([row[0]])
	print(t)
	handle.close()

def checkdata():
	handle = conn.cursor()
	handle.execute('select * from data limit 1')
	records = handle.fetchall()
	if len(records) == 0:
		return False
	else:
		True

def selectdata():
	option = input("Do you want display all tags ? [y/n]")

	if option == 'y':
		all_tags()
		tag = input("Enter the respective tag : ")
	else:
		tag = input("Enter the respective tag : ")
	
	handle = conn.cursor()
	handle.execute("select tag,uname,pswd from data where tag like ? ",['%'+tag+'%'])
	records = handle.fetchall()
	t = PrettyTable(['Tag', 'Username', 'Password'])
	for row in records:
		t.add_row([row[0], row[1],row[2]])
	print(t)
	handle.close()

def id_generator():
	pwo = PasswordGenerator()
	pwo.minlen = 15
	pwo.excludeschars = "^'"
	print (pwo.generate())

def delete():
	all_tags()
	tag = input("Enter the respective tag for the entry : ")
	handle = conn.cursor()
	handle.execute("select id,uname,pswd from data where tag like ? ",['%'+tag+'%'])
	records = handle.fetchall()
	t = PrettyTable(['sl num', 'entry id', 'Username', 'Password'])
	for i,row in enumerate(records,1):
		t.add_row([i,row[0],row[1],row[2]])
	print(t)
	entryId = input("Enter respective entry id for delteing the entry :")
	handle.execute("delete from data where id=?",[entryId])
	conn.commit()
	handle.close()
