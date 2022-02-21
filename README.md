# bank-application

You need to have local db in your computer and you have to download all libraries that i used in the application if you want to use.

Note: I used MySQL for local db.

Local Database tables must be like this:

information: id([int]primary key, not null, unique, auto incremental), 
             username([varchar(45)]not null),
             password([varchar(45)]not null),
             blocked([int]not null),
             counter([int]not null)
             
             
 person: id([int]primary key, not null, unique, auto incremental),
          tckn([int] not null, unique),
          name([varchar(45)] not null),
          surname([varchar(45)] not null),
          birthdate([varchar(45)] not null),
          adress([varchar(45)] not null),
          *info_id([int] not null, unique)*,
          gender([char(6)] not null)
          
*person(info_id) = information(id)   foreign key*


accounts: id([int] primariy key, not null, unique, auto incremental),
          *person_id([int] not null)*,
          iban([varchar(45)] not null, unique),
          account_type([varchar(45)] not null),
          amountTL([int] not null),
          amountUSD([int] not null),
          amountEUR([int] not null)
          
*account(person_id) = person(id)   foreign key*


logs: id([int] primary key, not null, unique, auto incremental),
      process_time([varchar(45)] not null),
      process([varchar(45)] not null),
      username([varchar(45)] not null)
      
      
 <h1> How to use </h1>
 
 Open the folder in vscode or any other similar IDE and
 write "python welcomeWindow.py" on the terminal this command
          
