<?php
  echo "hello world<br>"; // outputs "hello world"
  ECHO "helllooo<br>"; // outputs "helllooo"
  eCho "oookk<br>"; // outputs "oookk"
  
  $cars = array("Volvo", "BMW", "Mercedes", "Bugatti"); // creates an array of car brands
  echo "<br>SORT :" ; // outputs the array contents to the screen
  sort($cars);
  print_r($cars);
  $clength=count($cars);
  for($x=0;$x<$clength;$x++)
  {
    echo $cars[$x] ;
    echo "<br>";
  }
  rsort($cars);
  print_r($cars);
  $clength=count($cars);
  for($x=0;$x<$clength;$x++)
  {
    echo $cars[$x] ;
    echo "<br>";
  }
  $ag = array("shah"=>'21', "aman"=>'20', "rahul"=>'19', "utkarsh"=>"21");
  print_r($ag);
  asort($ag);
  print_r($ag);
  $clength=count($ag);
  foreach($ag as $key => $value)
  {
    echo $key." is ".$value." years old.<br>";
  } 
  $age = array("shah"=>'21', "aman"=>'20', "rahul"=>'19', "utkarsh"=>"21");
  ksort($age);
  foreach($age as $key => $value)
  {
    echo $key." is ".$value." years old.<br>";
  } 
  $agee = array("shah"=>'21', "aman"=>'20', "rahul"=>'19', "utkarsh"=>"21");
  arsort($agee);
  foreach($agee as $key => $value)
  {
    echo $key." is ".$value." years old.<br>";
  } 
  $ageee = array("shah"=>'21', "aman"=>'20', "rahul"=>'19', "utkarsh"=>"21");
  krsort($ageee);
  foreach($ageee as $key => $value)
  {
    echo $key." is ".$value." years old.<br>";
  }  
?>
