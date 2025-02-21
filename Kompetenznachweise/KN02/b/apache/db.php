<?php
$servername = "kn02b-db";
$username = "admin";
$password = "pw";
$dbname = "mysql";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "select Host, User from mysql.user;";
$result = $conn->query($sql);
while ($row = $result->fetch_assoc()) {
    echo ("<li>" . $row["Host"] . " / " . $row["User"] . "</li>");
}
