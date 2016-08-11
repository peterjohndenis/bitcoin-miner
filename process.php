<?php
session_start();
if (!empty($_GET['start']))
	$_SESSION['start'] = strtotime($_GET['start']);
if (!empty($_GET['end']))
	$_SESSION['end'] = strtotime($_GET['end']);
header('Location: ./index.html');
