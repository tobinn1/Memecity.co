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

$allowed_types =array('jpg','png');

$info = pathinfo($_FILES['userFile']['name']);
$ext = $info['extension']; // get the extension of the file
$newname = ($randomString . "." . "" . $ext); 

if (in_array($ext, $allowed_types, false) != true) {

        header("Location: error.html", true, 303);
        exit;
    }

$target = 'tempinput/'.$newname;
$xd = move_uploaded_file( $_FILES['userFile']['tmp_name'], $target);

if($xd === false) {
        die('There was an error writing this file');
    }
else {
		ob_start();
	$input = ("sudo python /var/www/yugiohgen/custommeme.py " .$newname);
    passthru($input); 
	$var = ob_get_contents();
	ob_end_clean();
	$img = $var;
    header("Location: http://autistickid.tk/yugiohgen$img", true, 303);
    exit;
    }
    ?>

</body>
</html>

