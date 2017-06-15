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

    $time_stretch = 0;
    
    $API_KEYs1 = $_POST['API_KEY1'];
    $API_KEYs2 = $_POST['API_KEY2'];
    $API_KEYs3 = $_POST['API_KEY3'];
    $API_KEYs4 = $_POST['API_KEY4'];
    $API_KEYs5 = $_POST['API_KEY5'];
       
    $Mode1 = $_POST['Driving'];
    $Mode2 = $_POST['Walking'];
    $Mode3 = $_POST['Bicycling'];
    $Mode4 = $_POST['Transit'];
   

    $Start_Time = $_POST['Start_Time'];
    $End_Time = $_POST['End_Time'];

    if($Start_Time != "" and $End_Time != ""){
        $time_stretch = 1;
    }

if($_POST['API_KEY1']==""){
   echo "An API key must be present in the first entry at least. Please Try again.";
}
if($_POST['API_KEY2']==""){
$Filler2 = "0";
}
else{
    $Filler2 = $_POST['API_KEY2'];
}
if($_POST['API_KEY3']==""){
$Filler3 = "0";
}
else{
    $Filler3 = $_POST['API_KEY3'];
}
if($_POST['API_KEY4']==""){
$Filler4 = "0";
}
else{
    $Filler4 = $_POST['API_KEY4'];
}
if($_POST['API_KEY5']==""){
$Filler5 = "0";
}
else{
    $Filler5 = $_POST['API_KEY5'];
}
    $uploaddir = 'uploads/';
    $uploadfile = $uploaddir . basename($_FILES['userfile']['name']);
    $filename = $_FILES['userfile']['name'];
   
  
   

 $name='out_'.date('m-d_hia').'.csv';
move_uploaded_file($_FILES['userfile']['tmp_name'], $uploadfile);
passthru("python gmaps_standard.py uploads/$filename output/$name -off $API_KEYs1 $Filler2 $Filler3 $Filler4 $Filler5 $Mode1 $Mode2 $Mode3 $Mode4 $Start_Time $End_Time $time_stretch 2>&1",$return_var );
#echo "python gmaps_standard.py uploads/$filename output/$name -off $API_KEYs1 $Filler2 $Filler3 $Filler4 $Filler5 2>&1";
 echo"<br><br><br><br>";
 if ($return_var==0) {
      echo "File is valid, and was successfully uploaded.\n";
    } else {
       echo "Something went wrong. See error above.\n\n\n\n\n";
    }
     echo"<br><br><br><br>";
if($return_var==0){
    ?><html><body><a href="output/<?php echo $name;?>" download="<?php echo $name;?>">Download The Summary File Here</a>
</body>

    
</html>
<?php
}
else{
    echo "Please try again.";
}


?>


</body>

    
</html>
