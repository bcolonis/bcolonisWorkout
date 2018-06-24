#! /usr/bin/env python3
print('Content-type: text/html')

import cgi

##import MySQLdb
##
##string="i211s17_bcolonis"
##password="my+sql=i211s17_bcolonis"
##
##db_con = MySQLdb.connect(host="db.soic.indiana.edu",port=3306,user=string,passwd=password,db=string)
##
##cursor = db_con.cursor()



form = cgi.FieldStorage()
workoutID = form.getfirst("workoutID","")

html = """
<!doctype html>
<html>

<head>
<meta charset="utf-8">

<title>Workout Info</title>
</head>

<body>
	<p>{workoutID}</p>
</body>
</html>"""


##print the content in HTML format
print(html.format(workoutID=workoutID))
