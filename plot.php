<?php
session_start();
require 'phplot.php';
$config = json_decode(file_get_contents('/var/www/mysql_config.json'), true);
$server = $config['host'];
$username = $config['login'];
$password = $config['passwd'];
$database = $config['database'];

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

$volt_data = array();
$temp_data = array();
if ($result->num_rows > 0) 
{
    //store data of each row
    while($row = $result->fetch_assoc())
    { 
		$volt_data[] = array('', $row['time'], $row['voltage'], 13.5, 11.7);
		$temp_data[] = array('', $row['time'], $row['temp']);
    }
}
$conn->close();
 
$volt_legend = array('volt', 'upper limit', 'lower limit');
$temp_legend = array('temp');

$plot = new PHPlot(1200, 600);
$plot->SetPrintImage(False);
//$plot->SetImageBorderType('plain');


//Volt plot
$plot->SetPlotType('lines');
$plot->SetLineStyles('solid');
$plot->SetDataType('data-data');
$plot->SetDataValues($volt_data);
$plot->SetXLabelType('time', ' %d %b %H:%M ');
$plot->SetXTickIncrement(60*120);
$plot->SetXLabelAngle(90);
$plot->SetFont('x_label', 2);
$plot->SetLineWidths(2);
$plot->SetYTitle("Volt");
$plot->SetLegend($volt_legend);
$plot->SetLegendPixels(0, 30);
$plot->SetMarginsPixels(130, 110);
$plot->SetPlotAreaWorld(NULL, 11.5, NULL, 14.5);
$plot->SetDataColors(array('blue', 'green', 'orange'));
$plot->DrawGraph();

//Temp plot
$plot->SetPlotType('lines');
//$plot->SetDataType('data-data');
$plot->SetDataValues($temp_data);
$plot->SetLineWidths(2);
$plot->SetYTitle("Temperature", 'plotright');
$plot->SetLegend($temp_legend);
$plot->SetLegendPixels(1120, 30);
$plot->SetPlotAreaWorld(NULL, 20, NULL, 30);
$plot->SetYTickIncrement(2);
$plot->SetYTickPos('plotright');
$plot->SetYTickLabelPos('plotright');
$plot->SetDataColors('red');
$plot->DrawGraph();



$plot->PrintImage();


session_unset(); 
