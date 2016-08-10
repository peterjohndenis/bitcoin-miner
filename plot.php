<?php
session_start();
require 'phplot.php';
$config = json_decode(file_get_contents('mysql_config.json'), true);
$server = $config['host'];
$username = $config['login'];
$password = $config['passwd'];
$database = $config['database'];

//$limit = isset($_SESSION['limit']) ? $_SESSION['limit'] : 100;
$start = isset($_SESSION['start']) ? $_SESSION['start'] : (time() - (60*60*24*2));
$end = isset($_SESSION['end']) ? $_SESSION['end'] : time();

// Create connection
$conn = new mysqli($server, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM sensor_data WHERE time BETWEEN $start AND $end";
$result = $conn->query($sql);

$data = array();
if ($result->num_rows > 0) 
{
    //store data of each row
    while($row = $result->fetch_assoc()) 
    {
		//$data[] = array('', strtotime($row['time']), $row['voltage']);
		$data[] = array('', $row['time'], $row['voltage']);
    }
} 


$conn->close();
$plot = new PHPlot(600, 400);
$plot->SetImageBorderType('plain');
$plot->SetMarginsPixels(40, 40);
$plot->SetDataValues($data);
$plot->SetPlotType('lines');
$plot->SetLineWidths(2);
$plot->SetDataType('data-data');
$plot->SetXLabelType('time', ' %d %b %H:%M ');
$plot->SetPlotAreaWorld(NULL, 11.5, NULL, 14.7);
$plot->SetYTickIncrement(0.1);
//$plot->SetXTickIncrement(60*30);
$plot->TuneYAutoRange(0, 'R', 0);
$plot->SetFont('x_label', 2);
$plot->SetXLabelAngle(90);
$plot->DrawGraph();

session_unset(); 
