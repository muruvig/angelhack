

<html>
    <head>
        
        
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
        <script src="http://code.highcharts.com/highcharts.js"></script>

        <script>
            
          <?php  $search = $_GET['input'];
            $search = ucfirst($search); 

            $myFile = "keyword.txt";
            $fh = fopen($myFile, 'w') or die("can't open file");
            fwrite($fh, $search);
            fclose($fh);
            ?>
        </script>
       
          <style>
              
            #bg {
                text-align: center; 
                background-image: url(/style/grid.png);
                background-size: cover;
            }
            
            #results {
                height: 15%;
                width: 33%;
            }
            
            #data {
                text-align: center;
            }
              
            #container {
                border: 2px;
                border-color: navy;
                margin: auto;
            }
            
        </style>
        
    </head>
    <body id="bg">
        
        <img id="results" src="style/results.png">
        
        <span id="printHere"></span>
        
        <div id="container" style="width:900px; height:500px;"></div><br>
        
        <div id="fb-root"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&appId=166405163445053&version=v2.0";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>


<div class="fb-like" data-href="http://1heart.github.io/Yixin-Lin/" data-layout="button" data-action="like" data-show-faces="true" data-share="true"></div>



<!-- Place this code where you want the badge to render. -->
<a href="//plus.google.com/u/0/103861980136011182474?prsrc=3"
   rel="publisher" target="_top" style="text-decoration:none;display:inline-block;color:#333;text-align:center; font:13px/16px arial,sans-serif;white-space:nowrap;">
<span style="display:inline-block;font-weight:bold;vertical-align:top;margin-right:5px; margin-top:8px;"></span><span style="display:inline-block;vertical-align:top;margin-right:15px; margin-top:8px;"></span>
<img src="//ssl.gstatic.com/images/icons/gplus-32.png" alt="Google+" style="border:0;width:32px;height:32px;"/>
</a>
        
      
            
            
        <?php
 
           
            system('python jsonthingy.py');
           
           

            
        ?>
        
        
         <script>
         var options = {
            chart: {
            renderTo: 'container',
            defaultSeriesType: 'line'
        },
        title: {
            text: "<?php print($search); ?>"
            },
        xAxis: {
            categories: []
        },
        yAxis: {
                title: {
                    text: 'Units'
                }
            },
            series: []
            };
        </script>

        <script>
        $.get('dump.csv', function(data)
        {
            var lines = data.split('\n');
            $.each(lines, function(lineNo, line)
            {
                var items = line.split(',');

                if (lineNo === 0)
                {
                    $.each(items, function(itemNo, item)
                        {   
                        if (itemNo > 0)
                        {
                            if(item == 'Date')
                            {
                                options.series.push(
                                {
                                    name:item,
                                    lineWidth: 5, 
                                    data:[]
                                });
                            }
                            else
                            {
                                options.series.push(
                                {
                                    name:item,
                                    data:[]
                                });
                            }
                        }
                    });
                }
                else
                    {
                    $.each(items, function(itemNo, item)
                        {
                        if(itemNo == 0)
                            {
                                options.xAxis.categories.push(item);
                            }
                        else if (item == "null")
                            {
                                options.series[itemNo-1].data.push(null);
                            }
                        else
                            {
                                options.series[itemNo-1].data.push(parseFloat(item));
                            }
                        });
                    }
                });
                var chart = new Highcharts.Chart(options);
            });
            
            
        </script>

        <script>
        
            Highcharts.createElement('link', {
               href: 'http://fonts.googleapis.com/css?family=Unica+One',
               rel: 'stylesheet',
               type: 'text/css'
            }, null, document.getElementsByTagName('head')[0]);

            Highcharts.theme = {
               colors: ["#2b908f", "#90ee7e", "#f45b5b", "#7798BF", "#aaeeee", "#ff0066", "#eeaaee",
                  "#55BF3B", "#DF5353", "#7798BF", "#aaeeee"],
               chart: {
                  backgroundColor: {
                     linearGradient: { x1: 0, y1: 0, x2: 1, y2: 1 },
                     stops: [
                        [0, '#2a2a2b'],
                        [1, '#3e3e40']
                     ]
                  },
                  style: {
                     fontFamily: "'Unica One', sans-serif"
                  },
                  plotBorderColor: '#606063'
               },
               title: {
                  style: {
                     color: '#E0E0E3',
                     textTransform: 'uppercase',
                     fontSize: '20px'
                  }
               },
               subtitle: {
                  style: {
                     color: '#E0E0E3',
                     textTransform: 'uppercase'
                  }
               },
               xAxis: {
                  gridLineColor: '#707073',
                  labels: {
                     style: {
                        color: '#E0E0E3'
                     }
                  },
                  lineColor: '#707073',
                  minorGridLineColor: '#505053',
                  tickColor: '#707073',
                  title: {
                     style: {
                        color: '#A0A0A3'

                     }
                  }
               },
               yAxis: {
                  gridLineColor: '#707073',
                  labels: {
                     style: {
                        color: '#E0E0E3'
                     }
                  },
                  lineColor: '#707073',
                  minorGridLineColor: '#505053',
                  tickColor: '#707073',
                  tickWidth: 1,
                  title: {
                     style: {
                        color: '#A0A0A3'
                     }
                  }
               },
               tooltip: {
                  backgroundColor: 'rgba(0, 0, 0, 0.85)',
                  style: {
                     color: '#F0F0F0'
                  }
               },
               plotOptions: {
                  series: {
                     dataLabels: {
                        color: '#B0B0B3'
                     },
                     marker: {
                        lineColor: '#333'
                     }
                  },
                  boxplot: {
                     fillColor: '#505053'
                  },
                  candlestick: {
                     lineColor: 'white'
                  },
                  errorbar: {
                     color: 'white'
                  }
               },
               legend: {
                  itemStyle: {
                     color: '#E0E0E3'
                  },
                  itemHoverStyle: {
                     color: '#FFF'
                  },
                  itemHiddenStyle: {
                     color: '#606063'
                  }
               },
               credits: {
                  style: {
                     color: '#666'
                  }
               },
               labels: {
                  style: {
                     color: '#707073'
                  }
               },

               drilldown: {
                  activeAxisLabelStyle: {
                     color: '#F0F0F3'
                  },
                  activeDataLabelStyle: {
                     color: '#F0F0F3'
                  }
               },

               navigation: {
                  buttonOptions: {
                     symbolStroke: '#DDDDDD',
                     theme: {
                        fill: '#505053'
                     }
                  }
               },

               // scroll charts
               rangeSelector: {
                  buttonTheme: {
                     fill: '#505053',
                     stroke: '#000000',
                     style: {
                        color: '#CCC'
                     },
                     states: {
                        hover: {
                           fill: '#707073',
                           stroke: '#000000',
                           style: {
                              color: 'white'
                           }
                        },
                        select: {
                           fill: '#000003',
                           stroke: '#000000',
                           style: {
                              color: 'white'
                           }
                        }
                     }
                  },
                  inputBoxBorderColor: '#505053',
                  inputStyle: {
                     backgroundColor: '#333',
                     color: 'silver'
                  },
                  labelStyle: {
                     color: 'silver'
                  }
               },

               navigator: {
                  handles: {
                     backgroundColor: '#666',
                     borderColor: '#AAA'
                  },
                  outlineColor: '#CCC',
                  maskFill: 'rgba(255,255,255,0.1)',
                  series: {
                     color: '#7798BF',
                     lineColor: '#A6C7ED'
                  },
                  xAxis: {
                     gridLineColor: '#505053'
                  }
               },

               scrollbar: {
                  barBackgroundColor: '#808083',
                  barBorderColor: '#808083',
                  buttonArrowColor: '#CCC',
                  buttonBackgroundColor: '#606063',
                  buttonBorderColor: '#606063',
                  rifleColor: '#FFF',
                  trackBackgroundColor: '#404043',
                  trackBorderColor: '#404043'
               },

               // special colors for some of the
               legendBackgroundColor: 'rgba(0, 0, 0, 0.5)',
               background2: '#505053',
               dataLabelsColor: '#B0B0B3',
               textColor: '#C0C0C0',
               contrastTextColor: '#F0F0F3',
               maskColor: 'rgba(255,255,255,0.3)'
            };

            Highcharts.setOptions(Highcharts.theme);
        
        </script>
        
    </body>
</html>