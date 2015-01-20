xtodo
====

todo list
======

run
======
python xtodo.py

sql
======

import sqlite3
csql = "CREATE TABLE xtodo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status int NOT NULL, time TIMESTAMP NULL  DEFAULT CURRENT_TIMESTAMP)"
con = sqlite3.connect('todo.db') # Warning: This file is created in the current directory
con.execute("drop table if exists xtodo")
con.execute(csql)
con.execute("INSERT INTO xtodo (task,status) VALUES ('testtesttest111111111111',0)")
con.execute("INSERT INTO xtodo (task,status) VALUES ('eeeeeeeeeeeeeeeeeeeeeeeeee',1)")
con.execute("INSERT INTO xtodo (task,status) VALUES ('888888888888888888888888888888',0)")
con.commit()


