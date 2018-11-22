<!DOCTYPE html>
<html>
<head>
	<title>FitBeast</title>
	<?php
	$connect = new mysqli('localhost', 'root', '', 'users');

	if($connect->connect_error)
	{
		die("connection failed");
	}
	

	$eAdr = $_POST['eAdr'];
	$password = $_POST['password'];

	$sql = "SELECT * FROM `users` WHERE eAdr = '$eAdr' AND password ='$password'";

	$res = $connect->query($sql);
	
	$row = $res->fetch_assoc();
	
	if($res->num_rows > 0)
	{
		echo '<script type="text/javascript"> alert("Login Successful")</script>';
		echo '<script type="text/javascript"> window.location="FITBEAST.html" </script>';
	}
	else
	{
		echo '<script type="text/javascript"> alert("Invalid credentials")</script>';
		echo '<script type="text/javascript"> window.location="Login.html" </script>';
	}
?>
</head>
<body>
</body>
</html>