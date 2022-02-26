# Plinko
This is a simple script for simulating millions of games of plinko and calculating statistics.
Change the number of games or the bet size in th file directly.
Script will output wins as they happen with the game number that they happened in. (Wins are defined as hitting 1000x)

## Requirements
numpy

## Example Output
<pre>1000x:
68589
83478
86750
98372
103597
[...]
1850832
1892175
1944924
1956841
1966928

Stats:
[28, 499, 3576, 16991, 55601, 133730, 243778, 349199, 393283, 349236, 244378, 133041, 55427, 17050, 3670, 479, 34]
winit:  28  payit:  1000  z:  27972000
winit:  499  payit:  130  z:  64371000
winit:  3576  payit:  26  z:  89400000
winit:  16991  payit:  9  z:  135928000
winit:  55601  payit:  4  z:  166803000
winit:  133730  payit:  2  z:  133730000
winit:  243778  payit:  0.2  z:  -195022400.0
winit:  349199  payit:  0.2  z:  -279359200.0
winit:  393283  payit:  0.2  z:  -314626400.0
winit:  349236  payit:  0.2  z:  -279388800.0
winit:  244378  payit:  0.2  z:  -195502400.0
winit:  133041  payit:  2  z:  133041000
winit:  55427  payit:  4  z:  166281000
winit:  17050  payit:  9  z:  136400000
winit:  3670  payit:  26  z:  91750000
winit:  479  payit:  130  z:  61791000
winit:  34  payit:  1000  z:  33966000

profits:  -22466200.0
rtp:  -11.2331
rtp percent:  98.87669
Max time to 1000x:  165339
Min time to 1000x:  170
Average time to win:  31724.645161290322
Median time to win:  22293.5
RTP Min:  96.45186666666667
RTP Max:  101.9428
Rolling 1000x Min:  5
Rolling 1000x Max:  18
</pre>
