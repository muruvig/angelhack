<html>
    <head>
        
        <style>
            
            #bg {
                text-align: center; 
                background-image: url(/style/Uber_Grid_White_RGB.png);
            }
            
            #results {
                height: 20%;
                width: 40%;
            }
            
            #data {
                text-align: center;
            }
            
        </style>
        
    </head>
    <body id="bg">
        
        <img id="results" src="style/Untitled-5.png">
        
        <div id="data">
        <?php
            echo $_POST['username'];
            echo $_REQUEST['username'];
        ?>
        </div>
        
    </body>
</html>