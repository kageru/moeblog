<?php

$theStyle    = $_GET["style"];

setcookie("style", $theStyle, time()+36000, "/", "");

header("Location: $HTTP_REFERER");

exit;

?>