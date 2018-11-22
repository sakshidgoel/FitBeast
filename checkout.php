<!DOCTYPE html>
<html>
<head>
	<title>Checkout</title>
	 <link href="style.css" rel="stylesheet" type="text/css">
	 <script type="text/javascript">
    function fb()
    {
      window.location = "https://www.facebook.com/FitBeast-370979666779699/?ref=bookmarks";
    }

    function insta()
    {
      window.location = "https://www.instagram.com/fitbeast3?utm_source=ig_profile_share&igshid=nv1rx9quezld";
    }

    function twitter()
    {
      window.location = "https://twitter.com/FitBeast2?s=17";
    }

    
  </script>
	 <style type="text/css">
	 	body {
  background-image:url("food-meal-healthy-table-preview.jpg");
  padding: 0px;
  border: 0px;
  height: 750px;
  background-size: 100% 100%;
  background-color: white;
  margin: 0px;
  color: #151515;
  font-family: "Gill Sans", "Gill Sans MT", "Myriad Pro", "DejaVu Sans Condensed", "Helvetica", "Arial", "sans-serif";
}
	 </style>
	<script type="text/javascript">
		function foo()
		{
			window.location = "cart.html"
		}
	</script>
</head>
<body>
	 <a href="FITBEAST.html" class="thispage">
        <img src="FitBeast_Black.png" alt="FITBEAST" style="width:300px; height:100px;border:0;"/></a>
  <nav id="mainnav">
    <ul> 
      <li><a href="Eat.html">Food</a></li>
      <li><a href="Cult.html">Workout</a></li>
      <li><a href="Location.html">Location</a></li>
      <li><a href="Login.html">Login</a></li>
    </ul>
  </nav>
  <br><br><br><br>
	<?php 
	$connect = new mysqli('localhost', 'root', '', 'users');

	if($connect->connect_error)
	{
		die("connection failed");
	}
	

	$query="SELECT * FROM order1";
	$results = mysqli_query($connect,$query);
	$total=0;

	echo "<h1><font color='white'> Your bill</font> </h1>";


	while ($row = mysqli_fetch_array($results)) {

    echo"<b><font color='black'>". $row[0].":    ".$row[1]."Rs ,      Qty:".$row[2]."   <br>";
	
    $total+=$row[1]*$row[2];


	}	
	echo "<br>TOTAL: ".$total."Rs<br><br></font></b>";
	$query="TRUNCATE order1";
	$results = mysqli_query($connect,$query);
	echo '<button onclick="foo()">Proceed to checkout</button>';

	
	 ?>
	 <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
	 <footer>
    <nav id="footernav">
    <ul>
      <li><a href="Terms.html">Terms & conditions</a></li>
      <li><a href="Privacy.html">Privacy Policy</a></li>
      <li><a href="Contact.html">Contact Us</a></li>
      <li><img src="fb.png" class="icon" height="35" width="35" onclick="fb()" style="cursor:pointer;">
      <img src="twitter.png" class="icon" height="35" width="35" onclick="twitter()" style="cursor: pointer;">
      <img src="insta.png" class="icon" height="35" width="35" onclick="insta()" style="cursor: pointer;"></li>
    </ul>
    </nav>
  </footer>
</body>
</html>