#!/usr/bin/env python
# coding: utf-8

# # CS-E4850 Computer Vision Exercise Round 8
# 
# The problems should be solved before the exercise session and solutions returned via
# MyCourses. For this exercise round you should return a pdf file containing written answers to the questions below. 
# 
# ### Exercise 1. Face tracking example using KLT tracker
# 
# Run the example as instructed below and answer the questions.
# 
# a) Run ```Exercise8.ipynb```<br>
# b) Run ```Exercise8.ipynb``` with a different input by changing the input to obama.avi: ```frames=faceTracker('obama.avi')```<br>
# c) What could be the main reasons why most of the features are not tracked very long in case b) above?<br>
# d) How could one try to avoid the problem of gradually losing the features? Suggest one or more improvements.<br>
# e) Voluntary task: Capture a video of your own face or of a picture of a face, and check that whether the tracking works for you. That is, replace the input video path in ```faceTrackingDemo.py``` with the path to your own video. 
# 
# ### Exercise  2. Kanade-Lucas-Tomasi  (KLT)  feature  tracking  (Pen  &  paper  problem)
# Read Sections 2.1 and 2.2 from the [paper by Baker and Matthews](https://www.ri.cmu.edu/pub_files/pub3/baker_simon_2002_3/baker_simon_2002_3.pdf). Show that the Equation (10) in the paper gives the same solution as the equations on slide 25 of Lecture 7, when the geometric warping W 
# (between the current frame and the template window in the previous frame) is a translation.


import os
from IPython.display import HTML

HTML('''<script>
code_show=true;
function code_toggle() {
if (code_show){
$('div.input').hide();
} else {
$('div.input').show();
}
code_show = !code_show
}
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click here to toggle on/off the raw code."></form>''')



# Description:
#   Exercise8 python demo.
#
# Copyright (C) 2018 Santiago Cortes, Juha Ylioinas, Tapio Honka
#
# This software is distributed under the GNU General Public 
# Licence (version 2 or later); please refer to the file 
# Licence.txt, included with the software, for details.

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML
from faceTrackingDemo import faceTracker



fig = plt.figure(figsize=(10,10))

# frames of the processed input video
# change the input to obama.avi in part b)
frames = faceTracker('santi.avi')
#frames = faceTracker('qr.avi')

# create an animation that can be embedded in the notebook
ani = animation.ArtistAnimation(fig, frames, interval=50, blit=True, repeat_delay=2000)

#display(HTML(ani.to_html5_video()))







