<?php
define("DBNAME",   "sqlite:system.db");

// Set up the connection to the database
function setDBConnection($connString)
{

    try {
        $pdo = new PDO($connString);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    } catch (PDOException $e) {
        echo "Connection failed: " . $e->getMessage();
    }

    return $pdo;
}

function runQuery($pdo, $sql, $parameters=array())     {
    // Ensure parameters are in an array
    if (!is_array($parameters)) {
        $parameters = array($parameters);
    }

    $statement = null;
    if (count($parameters) > 0) {
        // Use a prepared statement if parameters 
        $statement = $pdo->prepare($sql);
        $executedOk = $statement->execute($parameters);
        if (! $executedOk) {
            throw new PDOException;
        }
    } else {
        // Execute a normal query     
        $statement = $pdo->query($sql); 
        if (!$statement) {
            throw new PDOException;
        }
    }
    // Return array containing all of result set rows
    return $statement->fetchall(PDO::FETCH_ASSOC);
}



// Reads all returns all roomIDs from the Room database
function readAllRooms()
{
    $pdo = setDBConnection(DBNAME);
    // Pass PDO object, query string, and parameters (for the query string)
    $statement = runQuery($pdo, "SELECT roomID FROM Room");
    // Returns array with results
    return $statement;
}

// Returns capacity of a room as a string
function readCapacityByroomID($roomID)
{
    $pdo = setDBConnection(DBNAME);

    // Pass PDO object, query string, and parameters (for the query string)
    $statement = runQuery($pdo, "SELECT capacity FROM Room where roomID = ?",array($roomID));
    // Returns array with results
    return $statement[0]["capacity"];
}

// Returns capacity of a room as a string
function readCurrentSizeByroomID($roomID)
{
    $pdo = setDBConnection(DBNAME);

    // Pass PDO object, query string, and parameters (for the query string)
    $statement = runQuery($pdo, "SELECT currentSize FROM Room where roomID = ?",array($roomID));
    // Returns array with results
    return $statement[0]["currentSize"];
}

// Returns managerID of a room as a string
function readManagerIDByroomID($roomID)
{
    $pdo = setDBConnection(DBNAME);

    // Pass PDO object, query string, and parameters (for the query string)
    $statement = runQuery($pdo, "SELECT managerID FROM Room where roomID = ?",array($roomID));
    // Returns array with results
    return $statement[0]["managerID"];
}

// Returns managerID of a room as a string
function readManagerTable($mangerID)
{
    $pdo = setDBConnection(DBNAME);

    // Pass PDO object, query string, and parameters (for the query string)
    $statement = runQuery($pdo, "SELECT * FROM Manager where managerID = ?", array($mangerID));
    // Returns array with results
    return $statement;
}




