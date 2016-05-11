import csv
csvfile=open('E Block.csv','r')
reader=csv.reader(csvfile,delimiter='\n')
names=[]
numbers=[]
email_ids=[]
for row in reader:
	s=row[0].strip('\'').split(',')
	names.append(s[0].strip())
	numbers.append(s[1].strip())
	if(len(s)==3):
		email_ids.append(s[2].strip())
	else:
		email_ids.append('')
# print numbers
writer=csv.writer(open('temp.csv','wb'),delimiter=',')
writer.writerow(['Name','Given Name','Additional Name','Family Name','Yomi Name','Given Name Yomi','Additional Name Yomi','Family Name Yomi','Name Prefix','Name Suffix','Initials','Nickname','Short Name','Maiden Name','Birthday','Gender','Location','Billing Information','Directory Server','Mileage','Occupation','Hobby','Sensitivity','Priority','Subject','Notes','Group Membership','E-mail 1 - Type','E-mail 1 - Value','E-mail 2 - Type','E-mail 2 - Value','E-mail 3 - Type','E-mail 3 - Value','Phone 1 - Type','Phone 1 - Value','Phone 2 - Type','Phone 2 - Value','Phone 3 - Type','Phone 3 - Value','Phone 4 - Type','Phone 4 - Value','Phone 5 - Type','Phone 5 - Value','Phone 6 - Type','Phone 6 - Value','Phone 7 - Type','Phone 7 - Value','Phone 8 - Type','Phone 8 - Value','Address 1 - Type','Address 1 - Formatted','Address 1 - Street','Address 1 - City','Address 1 - PO Box','Address 1 - Region','Address 1 - Postal Code','Address 1 - Country','Address 1 - Extended Address','Address 2 - Type','Address 2 - Formatted','Address 2 - Street','Address 2 - City','Address 2 - PO Box','Address 2 - Region','Address 2 - Postal Code','Address 2 - Country','Address 2 - Extended Address','Organization 1 - Type','Organization 1 - Name','Organization 1 - Yomi Name','Organization 1 - Title','Organization 1 - Department','Organization 1 - Symbol','Organization 1 - Location','Organization 1 - Job Description','Relation 1 - Type','Relation 1 - Value','Website 1 - Type','Website 1 - Value'])
for i in range(len(names)):
	if('/' in numbers[i]):
		a1=numbers[i].split('/')[0].strip()
		a2=numbers[i].split('/')[1].strip()
		if(len(a1)==8):
			if(email_ids[i]==''):
				writer.writerow([names[i].strip(),'','','','','','','','','','','','','','','','','','','','','','','','','','* My Contacts','','','','','','','Mobile',a2,'Home',a1,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''])
			else:
				writer.writerow([names[i].strip(),'','','','','','','','','','','','','','','','','','','','','','','','','','* My Contacts','','','','','','','Mobile',a2,'Home',a1,'Work',email_ids[i],'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''])
		else:
			if(len(a2)==8):
				if(email_ids[i]==''):
					writer.writerow([names[i].strip(),'','','','','','','','','','','','','','','','','','','','','','','','','','* My Contacts','','','','','','','Mobile',a1,'Home',a2,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''])
				else:
					writer.writerow([names[i].strip(),'','','','','','','','','','','','','','','','','','','','','','','','','','* My Contacts','','','','','','','Mobile',a1,'Home',a2,'Work',email_ids[i],'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''])
			else:
				if(email_ids[i]==''):
					writer.writerow([names[i].strip(),'','','','','','','','','','','','','','','','','','','','','','','','','','* My Contacts','','','','','','','Mobile',a1,'Other',a2,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''])
				else:
					writer.writerow([names[i].strip(),'','','','','','','','','','','','','','','','','','','','','','','','','','* My Contacts','','','','','','','Mobile',a1,'Other',a2,'Work',email_ids[i],'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''])
	else:
		if(len(numbers[i])!=10 and len(numbers[i])>0):
			if(email_ids[i]==''):
				writer.writerow([names[i].strip(),'','','','','','','','','','','','','','','','','','','','','','','','','','* My Contacts','','','','','','','','','Home',numbers[i],'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''])
			else:
				writer.writerow([names[i].strip(),'','','','','','','','','','','','','','','','','','','','','','','','','','* My Contacts','','','','','','','','','Home',numbers[i],'Work',email_ids[i],'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''])
		elif(len(numbers[i])==10):
			if(email_ids[i]==''):
				writer.writerow([names[i].strip(),'','','','','','','','','','','','','','','','','','','','','','','','','','* My Contacts','','','','','','','Mobile',numbers[i],'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''])
			else:
				writer.writerow([names[i].strip(),'','','','','','','','','','','','','','','','','','','','','','','','','','* My Contacts','','','','','','','Mobile',numbers[i],'Work',email_ids[i],'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''])
		else:
			if(email_ids[i]==''):
				writer.writerow([names[i].strip(),'','','','','','','','','','','','','','','','','','','','','','','','','','* My Contacts','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''])
			else:
				writer.writerow([names[i].strip(),'','','','','','','','','','','','','','','','','','','','','','','','','','* My Contacts','','','','','','','Work',email_ids[i],'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''])
		# 26 commas then * My Contacts
		# 7 commas after my contacts add numbers