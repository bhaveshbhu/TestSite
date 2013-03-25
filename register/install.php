<?php
 include_once "scripts/connect_to_mysql.php"; 
$table1 = "CREATE TABLE members (
		 		 id int(11) NOT NULL auto_increment,
				 fame varchar(255) NOT NULL,
		 		 lname varchar(255) NOT NULL,
		 		 email varchar(255) NOT NULL,
		 		 password varchar(255) NOT NULL,
				 ipaddress varchar(255) NOT NULL,
		 		 sign_up_date date NOT NULL default '0000-00-00',
		 		 PRIMARY KEY (id),
		 		 UNIQUE KEY email (email)
		 		 ) ";
if (mysql_query($table1)){ echo "Your members table has been created successfully!<br /><br />"; } else { echo "CRITICAL ERROR: members table cannot be created ;";}
				 ?>