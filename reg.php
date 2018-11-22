<!DOCTYPE html>
<html>
<head>
	<title>REGISTER SERVER</title>
	 <link rel="stylesheet" type="text/css" href="style.css">
</head>

<?php
$host = 'localhost';
$username = 'root';
$password = '';
$db_name = 'users';

//Establishes the connection
$conn = mysqli_init();
mysqli_real_connect($conn, $host, $username, $password, $db_name, 3306);
if (mysqli_connect_errno($conn)) {
die('Failed to connect to MySQL: '.mysqli_connect_error());
}

$username = $_POST['username'];
$password = $_POST['password'];
$eAdr = $_POST['eAdr'];

echo "REGISTERED!";

if($stmt = mysqli_prepare($conn, "INSERT INTO users(username,  eAdr, password) VALUES (?, ?, ?)")) {
mysqli_stmt_bind_param($stmt, 'sss', $username,$eAdr, $password);
mysqli_stmt_execute($stmt);
mysqli_stmt_close($stmt);
}
//Close the connection
mysqli_close($conn);
echo '<script> alert("registered");window.location = "Login.html"</script>';
?>
</body>
</html>