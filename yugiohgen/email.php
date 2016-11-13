<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>php</title>
</head>

<body>
<?php
//if "email" variable is filled out, send email
  
  //Email information
  $admin_email = "ohblizard@gmail.com";
//$email = "someone has submited somthing";
  $subject = "Meme submission";
  $comment = "XD someone has submited somthing";
  
  //send email
  mail($admin_email, "$subject", $comment);
?>

</body>
</html>

