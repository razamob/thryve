

<!DOCTYPE html>

<html>
    <head>
        <meta charset='UTF-8'>
        <title>Connect To Tryve Database</title>
        <style>
            p::first-letter 
            {
                color: red;
                font-size: 29px;
                font-style: italic;
            }
        </style>
        
    </head>
    <body>
        <div>hiiii</div>
        <?php
  
        try
        {
            $host="localhost";
            $dbname="capstonethryve";
            $username = "root";
            $password = "sheridan";
            //$conn = new PDO('mysql:host=localhost;dbname=root', $username, $password);
            $conn = new PDO('mysql:host=$host;dbname=$dbname', $username, $password);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            // set the PDO error mode to exception
            
             $sql='SELECT * FROM registration';
            $stmt = $conn->prepare($sql);
            $stmt->execute();
            $titles = Array();                                                              
            echo "<table>";
            $tablehead = false;

            while($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                    if($tablehead == false) {
                            echo '<tr>';

                            foreach($row as $key=>$value) {
                                    echo "<th>".$key."</th>";
                            }

                            echo '</tr>';
                            $tablehead = true;
                    }

                    echo "<tr>";
                    foreach($row as $value) {
                            echo "<td>".$value."</td>";
                    }

                    echo "</tr>";
            }
            echo "</table>";   
        }    
        catch(PDOException $e)
        {
            echo "<p>Connection failed: </p>" . $e->getMessage();
        }
        $conn = null; 
        ?>
    </body>
</html>






































