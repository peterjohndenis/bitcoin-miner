<?php
require 'phplot.php';
$plot = new PHPlot();

$config = json_decode(file_get_contents('mysql_config.json'), true);


$server = $config['host'];
$username = $config['login'];
$password = $config['passwd'];
$database = $config['database'];

// Create connection
$conn = new mysqli($server, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "SELECT * FROM sensor_data LIMIT 10";
$result = $conn->query($sql);


if ($result->num_rows > 0) 
{
    $data = array();
    //store data of each row
    $i = 0;
    while($row = $result->fetch_assoc()) 
    {
		$data[] = array('', strtotime($row['datetime']), $row['voltage']);
    }
    //print_r($data);
} 
else 
{
    echo "0 results";
}



$conn->close();

//$data = array(array('', 0, 0), array('', 1, 9));
$plot->SetDataValues($data);
$plot->SetDataType('data-data');
$plot->SetXLabelType('time', '%H:%M');
$plot->DrawGraph();

