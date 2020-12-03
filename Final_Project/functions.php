<?php

function addNode($roomID)
{
    try {
?>
        <br>
        <!-- create new button with an id corresponding with the node index -->
        <a class="nodelink" href="http://127.0.0.1/demo2/node_page.php?<?php echo "id=$roomID";?>"><?php echo "$roomID"; ?></a>

<?php
        return true;
    } catch (Exception $e) {
        echo 'Caught exception: ',  $e->getMessage(), "\n";
    }
}
