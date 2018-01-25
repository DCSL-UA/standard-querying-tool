<!DOCTYPE html>
 
<html lang="en">


    <style>
 
   html{background: #61210B }
.wrap {
width: 100&#37;;
height: 600px; /* optional */
background: #FFFFFF; /* optional */
font-family: 'times new roman', arial, sans-serif;
font-size: 1em;
color: #FFFFFF;
}
    .nav2 {clear: both; margin: 0px; background-color: #FFFFFF;padding: 0px; font-family: verdana, arial, sans serif; font-size: 1.0em;}
.nav2 ul {float: left; width: 770px; margin: 0px; padding: 0px; border-top: solid 1px rgb(54,83,151); border-bottom: solid 1px rgb(54,83,151); background-color: rgb(127,162,202); font-weight: bold;}  
.nav2 li {display: inline; list-style: none; margin: 0px; padding: 0px;}
.nav2 li a {display: block; float: left; margin: 0px 0px 0px 0px; padding: 5px 10px 5px 10px; border-right: solid 1px rgb(54,83,151); color: rgb(255,255,255); text-transform: uppercase; text-decoration: none; font-size: 100%;}
.nav2 a:hover, .nav2 a.selected {color: rgb(50,50,50); text-decoration: none;}
.buffer {clear: both; width: 730px; height: 0px; margin: 20px; padding: 20px; background-color: rgb(255,255,255);}
.content1-pagetitle {overflow: hidden; width: 750px; margin: 0px 0px 0px 0px; padding: 0px 0px 2px 0px; border-bottom: solid 3px rgb(88,144,168);); background-color: #FFFFFF;font-weight: bold; font-size: 180%;}


.page-container-3 {width: 770px;margin: 0px auto; padding: 0px; background-color: url('crimson-background.gif'); border: solid 1px rgb(0,0,250);}

  .style16 {
    margin-left: 40px;
    font-size: medium;
}
body {font-size: 90%; width: 800px;margin: 0px auto; padding: 20px; background-color: rgb(255,255,255); font-family: arial, sans-serif;min-height: 500px;}


.content3 {float: left; width: 800px; min-height: 500px; background-color: #FFFFFF; margin: 0px; padding: 0px 0px 2px 0px; color: rgb(0,0,0); font-size: 1.0em;}

.site-name {
    width: 300px;
    height: 45px;
    top: 12px;
    position: absolute;
    z-index: 4;
    overflow: hidden;
    margin: 0px;
    padding-left: 0px;
   background-image: url('crimson-background.gif');
}








a:link {
    color: blue;
    background-color: transparent;
    text-decoration: none;
}
a:visited {
    color: blue;
    background-color: transparent;
    text-decoration: none;
}
a:hover {
    color: black;
    background-color: transparent;
    text-decoration: underline;
}
a:active {
    color: yellow;
    background-color: transparent;
    text-decoration: underline;
}
</style>
    <head>

    <title>Search Completed</title>

<div class="style16">
        <meta charset="utf-8" />


    
         
    </head>
    

    <body>
  


    <table border="0" cellpadding="10">
      <tr>
        <td>
          

<img src="bama.jpg">
  


<?php
function html_form(){

    ?> <html> <body> <form enctype="multipart/form-data" action="results.php" method="POST">

    <input type="submit" value="CLick to continue" />

</form>
        
         <form enctype="multipart/form-data" action="gmaps.html" method="POST">

    <input type="submit" value="CLick to go back" />

</form>   
    </body>
</html>
<?php
}
date_default_timezone_set("America/Chicago");

session_start();

    $_SESSION['Got_key_count'] = 0;
    $_SESSION['time_stretch'] = 0;
    
       
   
   #print $_SESSION['Mode1;   
   #print $_SESSION['Mode2;
   #print $_SESSION['Mode3;
   #print $_SESSION['Mode4;
if($_SESSION['Mode1'] == "0" && $_SESSION['Mode2'] == "0" && $_SESSION['Mode3'] == "0" && $_SESSION['Mode4'] == "0"){
    print "No Modes were Selected. Please Retry Again.";
    exit;
}
$_SESSION['mode_count'] = 0;
if($_SESSION['Mode1'] == "on"){
    $_SESSION['mode_count'] += 1;
}
if($_SESSION['Mode2'] == "on"){
    $_SESSION['mode_count'] += 1;
}
if($_SESSION['Mode3'] == "on"){
    $_SESSION['mode_count'] += 1;
}
if($_SESSION['Mode4'] == "on"){
    $_SESSION['mode_count'] += 1;
}

#print "TIMES:";
#print $_SESSION['Start_Time;
#print $_SESSION['End_Time;

    if($_SESSION['Start_Time'] != "" and $_SESSION['End_Time'] != ""){
       
        $_SESSION['time_stretch'] = 1;
    }
    else{
$_SESSION['Start_Time'] = 0;
        $_SESSION['End_Time'] = 0;
        $_SESSION['time_stretch'] = 0;
    }

if($_SESSION['API_KEYs1']==""){
   echo "An API key must be present in the first entry at least. Please Try again.";
}
if($_SESSION['API_KEYs2']==""){
$_SESSION['Filler2'] = "0";
}
else{
    $_SESSION['Filler2'] = $_SESSION['API_KEYs2'];
}
if($_SESSION['API_KEYs3']==""){
$_SESSION['Filler3'] = "0";
}
else{
    $_SESSION['Filler3'] = $_SESSION['API_KEYs3'];
}
if($_SESSION['API_KEYs4']==""){
$_SESSION['Filler4'] = "0";
}
else{
    $_SESSION['Filler4'] = $_SESSION['API_KEYs4'];
}
if($_SESSION['API_KEYs5']==""){
$_SESSION['Filler5'] = "0";
}
else{
    $_SESSION['Filler5'] = $_SESSION['API_KEYs5'];
}
   # $_SESSION['uploaddir'] = __DIR__;
    $filename = $_SESSION['original'];
  
$_SESSION['linecount'] = 0;


$handle = fopen($_SESSION['uploadfile'], "r");

   while(!feof($handle)){
  $_SESSION['line'] = fgets($handle);
  $_SESSION['linecount'] += 1;
}

 $_SESSION['name']='out_'.date('m-d_hia').'.csv';
move_uploaded_file($_SESSION['temp'], $_SESSION['uploadfile']);
$name = $_SESSION['name'];
$API_KEYs1 = $_SESSION['API_KEYs1'];
$Filler2 = $_SESSION['Filler2'];
$Filler3 = $_SESSION['Filler3'];
$Filler4 = $_SESSION['Filler4'];
$Filler5 = $_SESSION['Filler5'];
$Mode1 = $_SESSION['Mode1'];
$Mode2 = $_SESSION['Mode2'];
$Mode3 = $_SESSION['Mode3'];
$Mode4 = $_SESSION['Mode4'];
$Start_Time = $_SESSION['Start_Time'];
$End_Time = $_SESSION['End_Time'];
$time_stretch = $_SESSION['time_stretch'];
$string = 'python gmaps_standard.py "uploads' . "\\" . "$filename" . '"' . " output" . '\\' . "$name -off $API_KEYs1 $Filler2 $Filler3 $Filler4 $Filler5 $Mode1 $Mode2 $Mode3 $Mode4 $Start_Time $End_Time $time_stretch 2>&1";

passthru($string);
 echo"<br><br><br><br>";
 #if ($_SESSION['return_var==0) {
      echo "File is valid, and was successfully uploaded.\n";
  #  } else {
    #   echo "Something went wrong. See error above.\n\n\n\n\n";
   # }
     echo"<br><br><br><br>";
#if($_SESSION['return_var==0){
    ?><html><body><a href="output/<?php echo $_SESSION['name'];?>" download="<?php echo $_SESSION['name'];?>">Download The Summary File Here</a>
</body>

    
</html>
<?php
#}
#else{
#    echo "Please try again.";
#}


?>


</body>

    
</html>