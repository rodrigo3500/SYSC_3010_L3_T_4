<?php
require_once('database.inc.php');
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="css/reset.css?v=<?php echo time(); ?>" rel="stylesheet" type="text/css" />
    <link href="css/styles.css?v=<?php echo time(); ?>" rel="stylesheet" type="text/css" />


</head>

<body>
    <?php
    $roomID = $_GET['id'];
    $currentOccupancy = readCurrentSizeByroomID($roomID);
    $capacity = readCapacityByroomID($_GET['id']);
    $managerID = readManagerIDByroomID($roomID);

    // Manager Variables
    $firstName = readManagerTable($managerID)[0]['firstName'];
    $lastName = readManagerTable($managerID)[0]['lastName'];
    $email = readManagerTable($managerID)[0]['email'];
    $phoneNumber = readManagerTable($managerID)[0]['phoneNumber'];
    ?>
    <div class="data">
        <b>Room ID: </b>
        <?php echo $roomID; ?>

        <br><br>

        <b>Current Occupancy: </b>
        <?php echo $currentOccupancy; ?>

        <br><br>

        <b>Capacity: </b>
        <?php echo $capacity; ?>
    </div>

    <br><br>

    <div class="manager">
        <b>Manager Information </b>
        <br>
        <br>
        <p>Manager ID: <?php echo $managerID; ?></p>
        <br>
        <p>First Name: <?php echo $firstName; ?></p>
        <br>
        <p>Last Name: <?php echo $lastName; ?></p>
        <br>
        <p>Email: <?php echo $email; ?></p>
        <br>
        <p>Phone Number: <?php echo $phoneNumber; ?></p>

    </div>




</body>

</html>