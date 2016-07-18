<?php
//require 'phplot.php';
//$plot = new PHPlot();

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


if ($result->num_rows > 0) {
    print_r($result->fetch_assoc());
    print_r($result->fetch_assoc());
    // output data of each row
    //while($row = $result->fetch_assoc()) {
    //    echo "id: " . $row["id"]. " - Name: " . $row["firstname"]. " " . $row["lastname"]. "<br>";
    //}
} else {
    echo "0 results";
}



$conn->close();

/*$data = array(array('', 0, 0), array('', 1, 9));
$plot->SetDataValues($data);
$plot->SetDataType('data-data');
$plot->DrawGraph();
*/
