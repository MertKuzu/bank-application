# bank-application

You have to need local db in your computer if you want to use.
I used MySQL for local db.

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
          *info_id([int] not null, unique),
          gender([char(6)] not null)
          
*info_id is information(id)
