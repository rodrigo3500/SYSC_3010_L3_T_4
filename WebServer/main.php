<?php
require_once("database.inc.php");
require_once("functions.php");


?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>Room Capacitor Limiter Ultra</title>

    <link href="css/reset.css?v=<?php echo time(); ?>" rel="stylesheet" type="text/css" />
    <link href="css/styles.css?v=<?php echo time(); ?>" rel="stylesheet" type="text/css" />

</head>

<body>
    <header>
        <h1>Room Capacity Limiter Ultra </h1>
        <p>Protecting you from COVID-19 </p>
        <nav>

        </nav>
    </header>
    <main>
        <section class="diagram">
            <h3>Node Architecture</h3>
            <figure>
                <a href="images/system_diagram.png"><img src="images/system_diagram.png" alt="Node Diagram" title="Node Diagram" height="378" /></a>
                <figcaption>
                    <em>Individual Data Collection Node Architecture</em>
                </figcaption>
            </figure>


        </section>
        <section>
            <h3>Select a Node</h3>
            <?php

            // Returns an array of arrays containing room datas
            $rows = readAllRooms();



            // Loop through database rooms
            foreach ($rows as $room) {
                echo "<pre>";
                addNode($room['roomID']);
                echo "<pre>";
            }


            ?>
            </form>
        </section>
        <section id="reviews">
            <h3>Team Members</h3>
            <p>Rodrigo Fierro</p>
            <p>Tarun Kalikivaya </p>
            <p>Carling Clough</p>
            <p>Hari Govindasamy</p>

        </section>
    </main>
    <footer>
        <p><em>Copyright &copy; 2020 L3_t_4</em></p>
    </footer>
</body>

</html>