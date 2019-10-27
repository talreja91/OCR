This uses pyterreract and opencv to extract the text from the images. 
We can still see some trades-off which can be corrected by recompiling the tessertact NN and training it with your dataset

To run this code
<ul> 
  <li>Extract the files in the dir. </li>
  For ocr.py -- which uses a extra feature enhancement with preprocessing the image
  <ol>
  <li> <b> python <fileName>.py -i imageName.png -p blur</b> </li>
  <li>Note: -p is optional. Default value for preprocessing is threshold. which can be changed to <i>blur</i> by using the argument</li>
  </ol>
  For handocr.py
<ol>
  <li> <b> python <fileName>.py -i imageName.png</b> </li>
  </ol>
 </ul>
