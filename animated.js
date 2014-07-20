<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <title>Google Visualization API Sample</title>
  <script type="text/javascript" src="//www.google.com/jsapi"></script>
  <script type="text/javascript">
    google.load('visualization', '1', {packages: ['motionchart']});

    function drawVisualization() {
      var data = new google.visualization.DataTable();
      data.addColumn('string', 'INPUT NAME OF CATEGORY'); //ADD AS MANY THINGS AS YOU CAN WITH THIS LINE
      data.addRows([
        ['NAME OF CATEGORY', new Date("DATE"), 'X VALUE', 'Y VALUE', 'DESCRIPTION'],
      ]);
    
      var motionchart = new google.visualization.MotionChart(
          document.getElementById('visualization'));
      motionchart.draw(data, {'width': 800, 'height': 400});
    }
    

    google.setOnLoadCallback(drawVisualization);
  </script>
</head>
<body style="font-family: Arial;border: 0 none;">
<div id="visualization" style="width: 800px; height: 400px;"></div>
</body>
</html>