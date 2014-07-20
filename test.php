<!DOCTYPE html>
<html>
    <head>
        <link href="hack.css" rel="stylesheet">
        
    </head>
    <body>
        
        <img id= "logo" src="style/pulse.png">
        <h1 class="move">wavepulse.</h1>
        <form class= "move" action="getresult.php" method="GET">
            <input id="input" type="text" name="input" placeholder="Search" />
        </form>
        
        
        <script type ="text/javascript">
        function WriteToFile(passForm) {

        set fso = CreateObject("Scripting.FileSystemObject");  
        set s = fso.CreateTextFile("keyword.txt", True);
        s.writeline(document.passForm.input1.value);
        s.Close();
        }
        </script>
        
    </body>
</html>