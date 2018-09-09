<?php

$username="root";
$password="";
$database="geo_master";




// Opens a connection to a MySQL server
$connection=mysqli_connect ('localhost', $username, $password);
if (!$connection) {
  die('Not connected : ' . mysqli_error());
}

// Set the active MySQL database
$db_selected = mysqli_select_db( $connection,$database);
if (!$db_selected) {
  die ('Can\'t use db : ' . mysqli_error());
}

// Select all the rows in the markers table
$query = "SELECT state,district,boundary FROM `master` ";
$result = mysqli_query($connection,$query);
if (!$result) {
  die('Invalid query: ' . mysqli_error());
}
header("Content-type: text/xml");

// Start XML file, echo parent node
echo "<?xml version='1.0' encoding='utf-8'?>";
echo '<markers>';
$ind=0;
// Iterate through the rows, printing XML nodes for each
while ($row = @mysqli_fetch_assoc($result)){
  // Add to XML document node
 //
 
 //$string = str_replace(array('&', '<', '>'),array('&amp;', '&lt;', '&gt;'),$row['address']);
 //$string=transliterateString($string);
 
 //echo strpos($string,"ï¿½");
 
 //$string = preg_replace("/&#?[a-z0-9]+;/i","",$string); 
 //$string = strtr($string , $convert );
 //$string = str_replace('ï¿½ ', '--------', $string);
 
 //echo $row['address'];
 //echo "<br>";
 
 //echo 'address="' . ($string) . '" ';
 //echo "<br>";
 /*
  echo '<marker ';
  echo 'id="' . $row['id'] . '" ';
  echo 'name="' . ($row['name']) . '" ';
  echo 'address="' . utf8_encode($row['address']) . '" ';
  echo 'lat="' . $row['lat'] . '" ';
  echo 'lng="' . $row['lng'] . '" ';
  echo 'type="' . $row['type'] . '" ';
  echo '/>';
  $ind = $ind + 1;
  <coord lat="39.007513" lng="-92.311378"/>
*/

$cod_list = explode("], [",$row['boundary']);


//print_r( $row);

    



      echo '<state name="' . htmlspecialchars($row['state']) . '"> ';
      
      echo  '<district name="' . htmlspecialchars($row['district']) . '"> ';
	  //echo '<coord lat="39.00748" lng="-92.323222"/>';
	  
foreach ($cod_list as $cord) {
	$cords = explode(",",$cord);
	$lat= ($cords[0]);
	$lng=($cords[1]);
	$lat= str_replace("[[","",$lat);
	$lng= str_replace("]]","",$lng);
	echo '<coord lat="'.$lat.'" lng="'.$lng.'"/>';
	  
	//echo "lat:-".$lat."\n";
	//echo "lng:-".$lng."\n";
	}
	  echo '</district>';
	  echo '</state>';
  }

// End XML file
echo '</markers>';



?>