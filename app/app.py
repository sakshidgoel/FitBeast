from flask import Flask, render_template,request,redirect,jsonify,abort, Response
from pymongo import MongoClient
import os
import ast

app = Flask(__name__)

#DEFINING DB HANDLER
client = MongoClient('localhost', 27017)

db = client.signup
collection = db.signup
global name

@app.route('/')
def front_page():
	print("START PAGE")
	return render_template('first.html')

@app.route('/terms')
def terms_page():
	print("TERMS PAGE")
	return render_template('Terms.html')

@app.route('/privacy')
def privacy_page():
	print("PRIVACY PAGE")
	return render_template('Privacy.html')

@app.route('/contact')
def contact_page():
	print("START PAGE")
	return render_template('Contact.html')

@app.route('/homepage')
def homepage():
	print('HOME PAGE')
	return render_template('homepage.html')

@app.route('/payment')
def make_payment():
	print('PAYMENT PAGE')
	return render_template('payment.html')

@app.route('/cult')
def load_cult():
	print('WORKOUT PAGE')
	return render_template('cult.html')	

@app.route('/login')
def render_static():
    print("LOGIN PAGE")
    return render_template('Login.html')
    
@app.route('/signup')
def sign_up():
	print("SIGNUP PAGE")
	return render_template('signup.html')    

@app.route('/recommend')
def rec():
	print("RECOMMENDATIONS PAGE")
	return render_template('recommend.html')

@app.route('/merch')
def merchandise():
	print("MERCHANDISE PAGE")
	return render_template('merchandise.html')

@app.route('/register_user',methods=['POST'])
def reguser():
	req=request.get_json()
	name=req['name']
	email=req['email']
	record=collection.find()
	temp=[]
	for i in record:
	    temp.append(i)
	for i in temp:
	    if i['email']==email:
	        return Response(status=409)
	file=open('signup.txt','w')
	file.write(name)
	file.close()
	record=collection.insert_one(req)
	return {"status":200}
#    #All data is recieved in json format
#    req=request.get_json()
#    #this is the object that i want to add in mongo
#    record=collection.insert_one(req) 
#    return record
#    #print("inserted record with entry: ",record)
    
@app.route('/verify_login',methods=['POST'])
def verify():
    req=request.get_json()
    email=req['email']    
    record=collection.find()
    temp=[]
    for i in record:
        temp.append(i)

    name=''
    for i in temp:
        if i['email']==email:
            passfromdb=i['password']
            name=i['name']
	
    if name=='':
        return Response(status=500)
		
	
    
#    record=temp[-1]
    passfromreq=req['password']
#    passfromdb=record['password']
    
    #storing the name in a global variable, rather putting
	#it in a text file and then putting it in the same folder, can be explained as a local cache or so...
	#currently logged in customer's name will be in the temp.txt folder
#    name=record['name']
    file = open('temp.txt','w') 
    file.write(name) 
    file.close()
    
    if(passfromreq==passfromdb):
        # print("in if")
        # print("global name is: ",name)
        return Response(status=200)
    else:
        # print("in else")
        # print("global name is: ",name)
        return Response(status=400)
    return {"status":200}
    
@app.route('/temp',methods=['GET'])
def temp_send():
	file = open('temp.txt', 'r')
	name=file.read()
	file.close()
	return name

@app.route('/extended_signup')
def extend_signup():
	print("EXTENDED SIGNUP")
	return render_template('extended_signup.html')
	
	
@app.route('/preprocess',methods=['GET'])
def prep():
    file = open('temp.txt', 'r') 
    data=file.read()
    file.close()
    print("data: ",data)
    return {"status":"200","name":data}

@app.route('/eat')
def cart():
	print('FOOD PAGE')
	return render_template('Eat.html')

@app.route('/cart')
def show_cart():
	print('CART CONTENTS')
	return render_template('cart.html')

@app.route('/add_to_cart',methods=['POST'])
def add():
	print('ADDING ITEM TO CART')
	req=request.get_json()
	print("PRODUCT BEING ADDED:", req)
	item=req['item']
	cost=req['cost']
	category=req['category']
	filer= open('temp.txt', 'r')
	name=filer.read()
	filer.close()
	filew=open('orders.txt','a')
	# print("name is:",name)
	filew.write('\n')
	s=name+"={"+"item:"+item+","+"cost:"+str(cost)+ "," + "category:" +category  +"}"+'\n'
	filew.write(s)
	filew.close()
	return {"status":200}
    
@app.route('/show_cart',methods=['GET'])
def show():
	filer= open('temp.txt', 'r')
	name=filer.read()
	filer.close()	
	#return format expected is:-> name: value or just a dictionary would do since we are doing it for a particular person eventually!
	
	
	file=open('orders.txt','r')
	lines=file.read()	
	lines=lines.split('\n')
	
	
	send_dict=dict()
	send_dict[name]=[]
	for line in lines:
		if line=='':
			continue
		k,v=line.split('=')
		if k==name:
			send_dict[k].append(v)
	file.close()

	# print("send_dict is: ",send_dict)
	return jsonify(send_dict)
	
@app.route('/logout',methods=['GET'])
def log_out():
	print('LOGGING OUT')
	if os.stat('temp.txt').st_size==0:
		return Response(status=400)
	else:
		open('temp.txt','w').close()
		return {"validity":1}
	
@app.route('/initial_store',methods=['POST'])
def initial():
	print('INITIAL RECOMMENDATIONS')
	req=request.get_json()
	file=open('signup.txt','r')
	name=file.read()
	file.close()
	req["name"]=name
	file=open('recommend.txt','w')
	file.write(str(req))
	file.close()
	# print("req from initial: ",req)
	
	db1 = client.signup
	collection1 = db1.initial
	record=collection1.insert_one(req)
	return {"validity":"ok"}


#intelligent part goes here
@app.route('/get_recommendations',methods=['GET'])
def get_rec():
	print('UPDATED RECOMMENDATIONS')
	file=open('signup.txt')
	name=file.read()
	file.close()

	filerec=open('recommend.txt')
	line=filerec.read()
	filerec.close()
	#d is a dictionary form of line
	thatguy=ast.literal_eval(line)
	food_type=thatguy["food_type"]
	gender=thatguy["gender"]
	
	nameone=name.split(" ")[0]
	if os.path.exists('./repo/'+nameone+"_recommend.txt"):
		# print("Exists")
		filedata=open('./repo/'+nameone+"_recommend.txt",'r')
		line=filedata.read()
		filedata.close()
		recommend_data=ast.literal_eval(line)
		all_image_paths=recommend_data[food_type]


		#getting the required merchandise
		filegender=open('./repo/'+nameone+"_gender.txt",'r')
		line=filegender.read()
		filegender.close()
		gender_data=ast.literal_eval(line)
		merch=gender_data[gender]
	else:
		#getting the required food items
		# print("Doesnt")
		filedata=open('recommend_data.txt','r')
		line=filedata.read()
		filedata.close()
		recommend_data=ast.literal_eval(line)
		all_image_paths=recommend_data[food_type]


		#getting the required merchandise
		filegender=open('gender_data.txt','r')
		line=filegender.read()
		filegender.close()
		gender_data=ast.literal_eval(line)
		merch=gender_data[gender]
	print("Recommened Food:", all_image_paths)
	print("Recommended Merchandise:", merch)
	
	# print("all image paths: ",all_image_paths,type(all_image_paths))
	return {'name':name,'image':all_image_paths,'merchandise':merch}

#hardest part goes here
@app.route('/pay_and_recommend',methods=['GET'])
def pay_and_rec():
	#whats the plan now?
	#get all his gender related stuff here
	# print('in pay and rec')
	filer=open('recommend.txt','r')
	line=filer.read()
	filer.close()
	personal_data=ast.literal_eval(line)
	name=personal_data['name']
	food_type=personal_data['food_type']
	gender=personal_data['gender']
	
	file=open('orders.txt','r')
	lines=file.read()	
	lines=lines.split('\n')
	
	food_data_cart=[]
	gender_data_cart=[]
	
	for line in lines:
		if line=='':
			continue
		splitted=line.split('=')
		# print(splitted[1].split(','))
		if splitted[0]==name:
			item=splitted[1].split(',')[0].split(':')[1]
			cost=splitted[1].split(',')[1].split(':')[1]
			category=splitted[1].split(',')[2].split(':')[1]
			category=category[:len(category)-1]
			if category=='food':
				food_data_cart.append(item)
			elif category=='merchandise':
				gender_data_cart.append(item)
	file.close()
	# print("Food List: ",food_data_cart)
	# print("Merch List: ",gender_data_cart)
	
	#conversion of these two now from name into jpg will be done shortly
	
	for i in range(len(food_data_cart)):
		x=food_data_cart[i]
		x=x.lower().split()
		x='_'.join(x)+'.jpg'
		food_data_cart[i]=x
	
	for i in range(len(gender_data_cart)):
		x=gender_data_cart[i]
		x=x.lower().split()
		x='_'.join(x)+'.jpg'
		gender_data_cart[i]=x
		
	
	
	
	#reading the original ones-->
	filer=open('recommend_data.txt','r')
	filer_data=filer.read()
	recommend_data_txt=ast.literal_eval(filer_data)
	required_recommend_data_txt=recommend_data_txt[food_type]
	filer.close()
	
	
	filer=open('gender_data.txt','r')
	filer_data=filer.read()
	gender_data_txt=ast.literal_eval(filer_data)
	required_gender_data_txt=gender_data_txt[gender]
	filer.close()
	
	
	# We have 3 lists now, how?
	#for now lets replace them?
	
#	recommend_data_txt[food_type]=food_data_cart
#	gender_data_txt[gender]=gender_data_cart
#	
##	print("recommend_data_txt: ",recommend_data_txt)
##	print("gender_data_txt:  ",gender_data_txt)
	
	#take all the 4 lists and manipulate them
	#food_data_cart required_recommend_data_txt
	#gender_data_cart and required_gender_data_txt
	
	temp_food=[]
	n=len(required_recommend_data_txt)
	for i in food_data_cart:
		if len(temp_food)>=n:
			break
		temp_food.append(i)
	
	for i in required_recommend_data_txt:
		if len(temp_food)>=n:
			break
		if i not in temp_food:
			temp_food.append(i)
	
	temp_gender=[]
	n=len(required_gender_data_txt)
	for j in gender_data_cart:
		if len(temp_gender)>=n:
			break
		temp_gender.append(j)
	
	for j in required_gender_data_txt:
		if len(temp_gender)>=n:
			break
		if i not in temp_gender:
			temp_gender.append(j)
	
	
	recommend_data_txt[food_type]=temp_food
	gender_data_txt[gender]=temp_gender
	
	print("Recommended Food:",recommend_data_txt)
	print("Recommended Merchandise:",gender_data_txt)
	
	#Now write these to new files so it doesn't hamper the others
	nameone=name.split(" ")[0]	
	
	filenew=open('./repo/'+nameone+'_recommend'+".txt","w")
	filenew.write(str(recommend_data_txt))
	filenew.close()
	
	filenew=open('./repo/'+nameone+'_gender'+".txt","w")
	filenew.write(str(gender_data_txt))
	filenew.close()
	
	
	#Clearing cart
	file=open('orders.txt','r')
	lines=file.read()
	file.close()
	lines=lines.split('\n')
	c=dict()
	for line in lines:
		if line!='':
			naam,rest=line.split('=')
			if naam!=name:
				c[naam]=rest
	print("c:::::::::::::::::",c)
	file.close()
	
	#s=name+"={"+"item:"+item+","+"cost:"+str(cost)+ "," + "category:" +category  +"}"+'\n'
	
	file=open('orders.txt','w')
	for k in c:
		s= '\n' + k + "=" + c[k]+'\n'
		file.write(s)
	file.close()
	
	
	
	
	
	return {"validity":"okays"}
	

if __name__ == '__main__':
    app.run(debug=True)