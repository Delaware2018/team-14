from simple_salesforce import Salesforce
sf = Salesforce(username='navhan978@gmail.com', password='codeforgood123', security_token='Q9qSre8PF53RQpr9F2nqQgCi')


johnsmith = sf.Contact.create({'LastName':'Smith','Email':'example@example.com'})
print(johnsmith)