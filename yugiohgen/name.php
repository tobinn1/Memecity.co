<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>php</title>
</head>

<body>
<?php
function generateRandomString($length = 5) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $charactersLength = strlen($characters);
    $randomString = "";
    for ($i = 0; $i < $length; $i++) {
		$randomString .= $characters[rand(0, $charactersLength - 1)];
    }
	
	return $randomString;
}

$randomString = generateRandomString();
$txt = ".txt";
$nameoffile = ($randomString . "" . $txt);
$myfile = fopen("namecheck/$nameoffile" , "w");

if(isset($_POST['field1'])) {
    $data = $_POST['field1'];
    $xd = fwrite($myfile, $data);
	fclose($myfile);
	//$ret = file_put_contents("$myfile", $data, FILE_APPEND | LOCK_EX);
    if($xd === false) {
        die('There was an error writing this file');
    }
    else {
        //echo "$ret bytes written to file";
		//exec ('email.php');
		header("Location: sent.html", true, 302);
        exit;
    }
}
else {
   die('no post data to process');
}
?>

</body>
</html>

