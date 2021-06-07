<!DOCTYPE html>
<html>

<style>
input[type=text] {
	width:100px;
	background-color: #f888;
	border: none;
    	color:#fff;
        padding: 15px 0;
        text-align: center;
	text-decoration: none;
    	display: inline-block;
    	font-size: 15px;
    	margin: 0;
    	cursor: pointer;
	border-radius:10px;
	overflow:hidden;
	}
</style>
<body>

<?php

$motor = shell_exec("cd /home/pi/Desktop && sudo python servoMotor.py");


?>

<input type="text" value="사료 공급 완료" readonly>
</body>
</html>
