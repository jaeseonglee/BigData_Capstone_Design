<!DOCTYPE html>
<html>
	<head>
		<title>Animal Care System</title>		
		<style>
			#symbol {	
				left: 0;
				right: 0;
				top: 0;
				float: left;
				width: 18%;
				height: 18%;
			}

			img {
				width: 100%;	
			}

			iframe {
				border: none;
				margin: 0;	
				overflow:hidden;
			}	

			#iframe_1 {
				margin-left: 100px;
			
			}

			input[type=button] {		
				width:150px;
    			background-color: skyblue;
				border: none;
				color:white;

   				padding: 15px 0;
				text-align: center;
				text-decoration: none;
    			display: inline-block;
    			font-size: 15px;

    			margin: 4px;
				cursor: pointer;
				border-radius:10px;
			}

			div {
				display:flex;
			}

		</style>
	</head>
	<body>
		<img src="symbol.jpg" id="symbol">
		<h2>Animal Care System<br>
			Streaming</h2>

		<a href="camera1.html">
			<img src="http://10.50.246.6:8081/">
		</a>

		<a href="camera2.html">
			<img src="http://10.50.246.7:8081/">
		</a>
		
		<iframe src="print.php" width="200" height="60" id="iframe_1"></iframe>
		
		<div>
			<input type="button" value="새로고침" onclick="location.reload()">		
			<iframe src="http://10.50.246.7" width="600" height="95" id="iframe_2"></iframe>
		</div>	
	</body>
</html>
