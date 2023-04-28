from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import mysql.connector
import os
from datetime import date

Emp_id = ""
F_name = ""
L_name = ""
Phone_no = ""
Gender = ""
Dept = ""
Dept_id = ""

A_Emp_id = ""
A_F_name = ""
A_L_name = ""
A_Phone_no = ""

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "1234",
	database = "project"
)

mycursor = mydb.cursor()

class Admin_login:
	def __init__(self,email,password):
		self.L_email = email
		self.L_password = password
		self.email_c = ""
		self.password_c = ""
		
		cred = (self.L_email,self.L_password)
		sql = "Select  * from admin where email_id = %s and password = %s"
		
		mycursor.execute(sql,cred)
		myresult = mycursor.fetchall()
		if myresult:
			self.email_c = myresult[0][4]
			self.password_c = myresult[0][5]
			self.emp_id = myresult[0][3]
			self.f_name = myresult[0][1]
			self.l_name = myresult[0][2]
			self.email_id = myresult[0][4]
			self.phone_no = myresult[0][6]
		
	def show_data(self):
		if (self.L_email != "" and self.L_password != ""):
			if (self.email_c == self.L_email and self.password_c == self.L_password):
				return True

class Login:
    
    def __init__(self,email,password):
        self.L_email = email
        self.L_password = password
        self.email_c = ""
        self.password_c = ""
		
        cred = (self.L_email,self.L_password)
        sql = "Select  * from employees where email_id = %s and password = %s"

        mycursor.execute(sql,cred)

        myresult = mycursor.fetchall()


        if myresult:
            self.email_c = myresult[0][3]
            self.password_c = myresult[0][8]
            self.emp_id = myresult[0][0]
            self.f_name = myresult[0][1]
            self.l_name = myresult[0][2]
            self.email_id = myresult[0][3]
            self.phone_no = myresult[0][4]
            self.gender = myresult[0][5]
            self.dept = myresult[0][6]
            self.dept_id = myresult[0][7]
            self.password = myresult[0][8]

    def show_data(self):
	    if (self.L_email != "" and self.L_password != ""):
		    if (self.email_c == self.L_email and self.password_c == self.L_password):
			    return True

# Create your views here.

class Register:
    def __init__(self,emp_id,f_name,l_name,email_id,phone_no,gender,dept,dept_id,password):
        
        self.emp_id = emp_id
        self.f_name = f_name
        self.l_name = l_name
        self.email_id = email_id
        self.phone_no = phone_no
        self.gender = gender
        self.dept = dept
        self.dept_id = dept_id
        self.password = password
        sqlFormuls = "insert into employees (emp_id,first_name,last_name,email_id,phone_no,gender,dept,dept_id,password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        employee = (self.emp_id,self.f_name,self.l_name,self.email_id,self.phone_no,self.gender,self.dept,self.dept_id,self.password)
        mycursor.execute(sqlFormuls,employee)
        mydb.commit()

def index(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')

def emp_login(request):
	check = False
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('Password')
		lg1 = Login(email,password)
		check = lg1.show_data()
		print(check)
		if check:
			global Emp_id 
			Emp_id = lg1.emp_id
			global F_name 
			F_name = lg1.f_name
			global L_name 
			L_name = lg1.l_name
			global Phone_no 
			Phone_no = lg1.phone_no
			global Gender 
			Gender = lg1.gender
			global Dept 
			Dept = lg1.dept
			global Dept_id 
			Dept_id = lg1.dept_id
		if(check):
			return HttpResponseRedirect('/emp_dashboard')
	return render(request, 'emp_login.html')

def admin_login(request):
	check = False
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('Password')
		lg1 = Admin_login(email,password)
		check = lg1.show_data()
		print(check)
		if check:
			global A_Emp_id 
			A_Emp_id = lg1.emp_id
			global A_F_name 
			A_F_name = lg1.f_name
			global A_L_name 
			A_L_name = lg1.l_name
			global A_Phone_no 
			A_Phone_no = lg1.phone_no
		if(check):
			return HttpResponseRedirect('/admin_dashboard')
	return render(request, 'admin_login.html')

def admin_dashboard(request):
	emp_sql = "select * from projet_list"
	mycursor.execute(emp_sql)
	myresult=mycursor.fetchall()
	dist={}
	count = 0
	for row in myresult:
		print(count)
		dist [count]= row
		count = count+1
	data={'data':dist}
	return render(request, 'admin_dashboard.html',data)


def emp_dashboard(request):
	print("Emp_ID",Emp_id)
	emp_sql = "select * from project_employee where emp_id = %s"
	data_emp = (Emp_id,) 
	mycursor.execute(emp_sql,data_emp)
	myresult=mycursor.fetchall()
	dist={}
	count = 0
	for row in myresult:
		print(row)
		print(count)
		dist [count]= row
		count = count+1
	data={'data':dist}
	print(data)

	if request.method == "POST":
		state = request.POST.get('submit')
		print(state) 
		if state != "":
			new = (Emp_id,state)
			print(new)
			sql_update = "update tasks set submission_date = curdate(),status = 'Done' where emp_id = %s and id = %s;"
			mycursor.execute(sql_update,new)
			mydb.commit()
	
	task = "select * from tasks where emp_id = %s"
	mycursor.execute(task,data_emp)
	myresult_task = mycursor.fetchall()
	task_data = {}
	count = 0
	for row in myresult_task:
		task_data[count] = row
		count = count+1
	data['task']=task_data 
	print(data)

	return render(request, 'emp_dashboard.html',data)

def register(request):
	return render(request, 'register.html')

def admin_profile(request):
	return render(request, 'admin_profile.html') 

def emp_profile(request):
	print(Emp_id)
	data = {}
	sql = "select * from employees where emp_id = %s"
	data_emp = (Emp_id,)
	mycursor.execute(sql,data_emp)
	myresult = mycursor.fetchall()
	emp_detail = {}
	count = 0
	for row in myresult:
		emp_detail[count] = row
		count = count+1
	data['emp_details']= emp_detail
	print(data)		
	return render(request, 'emp_profile.html',data)

def mark_attendance(request):
	return render(request, 'mark_attendance.html')

def admin_add_emp(request):
	if request.method == "POST":
		emp_id = request.POST.get('Emp_ID')
		first_name = request.POST.get('First_Name')
		last_name = request.POST.get('Last_Name')
		email_id = request.POST.get('email')
		phone_no = request.POST.get('phone_no')
		gender = request.POST.get('gender')
		dept = request.POST.get('department')
		dept_id = request.POST.get('department_id')
		password = request.POST.get('password')

		print("Emp ID:", emp_id)
		print("First Name:", first_name)
		print("Last Name:", last_name)
		print("Email ID:", email_id)
		print("Phone No.:", phone_no)
		print("Gender:", gender)
		print("Department:", dept)
		print("Department ID:", dept_id)
		print("Password:", password)

		if emp_id and first_name and last_name and email_id and phone_no and gender and dept and dept_id and password:
			reg = Register(emp_id, first_name, last_name, email_id, phone_no, gender, dept, dept_id, password)

		else:
			print("buy")
	return render(request, 'admin_add_emp.html')

def attendance_record(request):
	if request.method == "POST":
		emp_id = request.POST.get('emp_id')
		emp_name = request.POST.get('emp_name')
		dept = request.POST.get('dept')
		task_desc = request.POST.get('task_desc')
		date = request.POST.get('date')
		dead_line = request.POST.get('dead_line')

			# Print the values for testing purposes
		print("Employee ID: ", emp_id)
		print("Employee Name: ", emp_name)
		print("Department: ", dept)
		print("Task Description: ", task_desc)
		print("Date: ", date)
		print("Deadline: ", dead_line)

		sql = "insert into tasks (id,emp_id,emp_name,dept,task_disc,Date,Dead_line,status) values (NULL,%s,%s,%s,%s,curdate(),%s,'ongoing');"
		data = (emp_id,emp_name,dept,task_desc,dead_line)
		mycursor.execute(sql,data)
		mydb.commit()

	return render(request, 'attendance_record.html')

def show_emp(request):
	emp_qury = "select * from employees;"
	mycursor.execute(emp_qury)
	file_data = {}
	emp_id= {}
	myresult = mycursor.fetchall()
	count = 1
	for row in myresult:
		emp_id[count] = row
		count = count + 1
	file_data['fetch_employees'] = emp_id
	print(file_data)
	return render(request, 'show_emp.html',file_data)

def emp_attendance_record(request):
	return render(request, 'emp_attendance_record.html')

def emp_show_emp(request):
	emp_qury = "select * from employees;"
	mycursor.execute(emp_qury)
	file_data = {}
	emp_id= {}
	myresult = mycursor.fetchall()
	count = 1
	for row in myresult:
		emp_id[count] = row
		count = count + 1
	file_data['fetch_employees'] = emp_id
	print(file_data)
	return render(request, 'emp_show_emp.html',file_data)

def remove(proj_title):
    return proj_title.replace(" ", "")

def admin_add_project(request):
	if request.method == 'POST':
		proj_title = request.POST.get('project_name')
		proj_desc = request.POST.get('project_description')
		print(proj_title)
		print(proj_desc)

		removed_title = remove(proj_title)

		proj = (proj_title,proj_desc)
		add_proj_sql = "insert into projet_list (Id,proj_name,proj_desc,Date) values (NULL,%s,%s,curdate());" 
		if(proj_title!="" and proj_desc!=""):
			myresult = mycursor.execute(add_proj_sql,proj)
			mydb.commit()
		
		project_file_create = "create table "+removed_title+" (id int auto_increment primary key,emp_id int, name varchar(20), file_name varchar(20), file_data longblob,date date)"
		mycursor.execute(project_file_create)

		# employee_removed_title = removed_title+"employee"

		# project_employee_list = "create table "+employee_removed_title+"(emp_id int,name varchar(20),group_no varchar(20))"
		# mycursor.execute(project_employee_list)

	return render(request, 'admin_add_project.html')

def Assigned_task(request):
	print("Emp_ID",Emp_id)
	Project = request.GET.get('Project')
	fn = ""
	lk = (Project,)
	rk = lk[0]
	file_data = {}
	bk_id = {}
	emp_id = {}
	emp_fetch = {}
	# print(rk)
	project_name = remove(lk[0])
	print(project_name)
	proj = "Select * from projet_list where proj_name = %s"
	mycursor.execute(proj,lk)
	myresult = mycursor.fetchall()
	for row in myresult:
		bk_id['title'] = row[1]
		bk_id['desc'] = row[2]
		bk_id[2] = row[3]
		file_data['Book'] = bk_id

	# emp_sql = "select id,name,date from file_detail"
	# mycursor.execute(emp_sql)
	# myresult=mycursor.fetchall()
	# if myresult:
	# 	print("Hello")
	# dist={}
	# count = 0
	# for row in myresult:
	# 	print(count)
	# 	dist [count]= row
	# 	count = count+1
	# data_1={'data':dist}
	# file_data[1]=data_1
	# for i in file_data[1].items():
	# 	for j in i:
	# 		print(j)
	emp_fetch={}
	sql_fetch = "select * from employees where emp_id in (select emp_id from project_employee where proj_name = %s);"

	mycursor.execute(sql_fetch,lk)

	myresult_1 = mycursor.fetchall() 
	count = 0
	for row in myresult_1:
		emp_fetch[count] = row
		count = count + 1
	file_data['fetch_employee'] = emp_fetch
	
	sql_file_fetch = "select id,emp_id,name,file_name,date from "+project_name+";"

	mycursor.execute(sql_file_fetch)
	myresult_2 = mycursor.fetchall()
	
	file_g = {}
	count_file  = 0
	for row in myresult_2:
		file_g[count_file]= row
		count_file = count_file + 1
	file_data['file_fetch_data'] = file_g
	# sql_file_fetch = "select * from"+lk+""
	print("file_data",file_data)

	if request.method == 'POST':

		name_file = request.POST.get('file_name')


		if name_file is not None:
			folder_name = lk[0]# set the name of the new folder here
			path = "C:/" + folder_name   # set the path where the new folder will be created here

			print(path)

			name_file = str(name_file)
			print(path)

			if not os.path.exists(path):
				os.mkdir(path)
				fn = path+"/"+name_file
				print("Folder created successfully")
				print(fn)
				if(fn != ""):
					sql = "Select file_data from "+project_name+" where file_name = %s"
					gg = (name_file,)
					mycursor.execute(sql,gg)
					data = ""
					r = mycursor.fetchall()
					for i in r:
						data = i[0]
				
					with open(fn,"wb") as f:
						f.write(data)
						f.close()
				
					print("File_saved")
			else:
				print(path)
				fn = path+"/"+name_file
				print(fn)
				if(fn != ""):
					sql = "Select file_data from "+project_name+" where file_name = %s"
					gg = (name_file,)
					mycursor.execute(sql,gg)
					r = mycursor.fetchall()
					for i in r:
						data = i[0]
				
					with open(fn,"wb") as f:
						f.write(data)
						f.close()
					print("File_saved")
		else:
			print('empty')


			try:
				file_path = request.FILES['file_location']
				print(file_path.name)
				print(file_path.size)
				initialdir = "C:/"
				fn = initialdir + file_path.name
				print(fn)
				with open(fn,"rb") as f:
					data = f.read()
				Name = F_name+ " "+L_name
				print(type(data))
				lower_project_name = project_name.lower()
				print(lower_project_name)
				if Emp_id != "":
					sql = "Insert into "+lower_project_name+" (id,emp_id,name,file_name,file_data,date) values (NULL,%s,%s,%s,%s,curdate())"
					mycursor.execute(sql,(Emp_id,Name,file_path.name,data))

					mydb.commit()
			except:
				if Emp_id != "":
					print("Employee",Emp_id)
				print("No path")


	return render(request, 'Assigned_task.html',file_data)

def Assigned_task_admin(request):
	Project = request.GET.get('Project')
	lk = (Project,)
	fn = ""
	# print("Book Name:",lk[0])
	proj = "Select * from projet_list where proj_name = %s"
	mycursor.execute(proj,lk)
	myresult = mycursor.fetchall()
	file_data = {}
	bk_id = {}
	emp_id = {}
	emp_fetch = {}
	for row in myresult:
		bk_id['title'] = row[1]
		bk_id['desc'] = row[2]
		bk_id[2] = row[3]
		file_data['Book'] = bk_id


	emp_qury = "select * from employees where emp_id not in (Select emp_id from project_employee);"

	mycursor.execute(emp_qury)

	myresult = mycursor.fetchall()
	count = 1
	for row in myresult:
		emp_id[count] = row
		count = count + 1
	file_data['employees'] = emp_id

	# print(file_data)
	sql_fetch = "select * from employees where emp_id in (select emp_id from project_employee where proj_name = %s);"

	mycursor.execute(sql_fetch,lk)

	myresult_1 = mycursor.fetchall() 
	count = 0
	for row in myresult_1:
		emp_fetch[count] = row
		count = count + 1
	file_data['fetch_employee'] = emp_fetch
	#print(file_data)
	
	project_name = remove(lk[0])
	sql_file_fetch = "select id,emp_id,name,file_name,date from "+project_name+";"

	mycursor.execute(sql_file_fetch)
	myresult_2 = mycursor.fetchall()
	
	file_g = {}
	count_file  = 0
	for row in myresult_2:
		file_g[count_file]= row
		count_file = count_file + 1
		# print(row)
	file_data['file_fetch_data'] = file_g
	# print(file_data['file_fetch_data'])

	if request.method == 'POST':
		value = request.POST.getlist('values')
		name_file = request.POST.get('file_name')
		name_file = str(name_file)
		if name_file != "None":
			folder_name = lk[0]# set the name of the new folder here
			path = "C:/" + folder_name   # set the path where the new folder will be created here

			if not os.path.exists(path):
				os.mkdir(path)
				print("file_path",name_file)

				fn = path+"/"+name_file
				print("Folder created successfully")
				if(fn != ""):
					sql = "Select file_data from "+project_name+" where file_name = %s"
					gg = (name_file,)
					mycursor.execute(sql,gg)
					r = mycursor.fetchall()
					for i in r:
						data = i[0]
				
					with open(fn,"wb") as f:
						f.write(data)
						f.close()
				
					print("File_saved")
			else:
				fn = path+"/"+name_file
				if(fn != ""):
					sql = "Select file_data from "+project_name+" where file_name = %s"
					gg = (name_file,)
					mycursor.execute(sql,gg)
					r = mycursor.fetchall()
					for i in r:
						data = i[0]
				
					with open(fn,"wb") as f:
						f.write(data)
						f.close()
				
					print("File_saved")
		else:
			print('empty')


		if value != []:
			count = 0

			flag = 0
			length = len(value)
			# print(length)
			emp_list = list(range(length))
			print(len(emp_list))
			for i in value:
				emp_list[count] = i
				count = count + 1
				data = (i,)
				print(data)
				sql = "select * from project_employee where emp_id = %s"
				mycursor.execute(sql,data)
				test_myresult = mycursor.fetchall()
				if test_myresult:
					flag = 1


			if flag ==  0:
				for i in emp_list:
					data = (i,)
					sql_1 = "select first_name, last_name, dept from employees where emp_id = %s"
					mycursor.execute(sql_1,data)
					myresult_fetch = mycursor.fetchall()
					for row in myresult_fetch:
						data_disc = list(range(4))
						data_disc [0]= i
						string = row[0] + " "+row[1]
						data_disc [1]= string
						data_disc [2]= lk[0]
						print(lk[0])
						data_disc [3]= row[2] 
						print(data_disc)
						sql_2 = "insert into project_employee (Sr_no,emp_id,emp_name,proj_name,dept) values (NULL,%s,%s,%s,%s)"
						mycursor.execute(sql_2,data_disc)
						mydb.commit()
		

	return render(request,'Assigned_task_admin.html',file_data)


