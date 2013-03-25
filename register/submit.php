<?php

// we check if everything is filled in

include_once "scripts/connect_to_mysql.php";
if(empty($_POST['fname']) || empty($_POST['lname']) || empty($_POST['email']) || empty($_POST['pass']))
{
	die(msg(0,"All the fields are required"));
}


// is the email valid?

if(!(preg_match("/^[\.A-z0-9_\-\+]+[@][A-z0-9_\-]+([.][A-z0-9_\-]+)+[A-z]{1,4}$/", $_POST['email'])))
	die(msg(0,"You haven't provided a valid email"));
$fname = $_POST['fname'];
$lname =$_POST['lname'];
$email = $_POST['email'];
$pass = $_POST['pass'];
$db_password = md5($pass); 
$ipaddress = getenv('REMOTE_ADDR');
$sql = mysql_query("INSERT INTO members (fname,lname, email, password, ipaddress, sign_up_date) 
     VALUES('$fname','$lname','$email','$db_password', '$ipaddress', now())")  
     or die (mysql_error());

echo msg(1,"registered.html");

function msg($status,$txt)
{
	return '{"status":'.$status.',"txt":"'.$txt.'"}';
}
?>
