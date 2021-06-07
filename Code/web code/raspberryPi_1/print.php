<?php

$x = floor(shell_exec("cat t") / 100.0) / 10.0;

$y  = shell_exec("cd /home/pi/Desktop/ACM && sudo python presentWarm.py");

echo "<pre style='font-size:14px'>현재 온도: $x ℃ \n온열 매트: $y</pre>";
?>
