# -*- coding: utf-8 -*-

"""
Created on Fri Dec 13 15:05:09 2019

@author: Rob
Code used to make three separate figures for a review article on the effect of 
alternating current stimulation.

First figure has 3 subplots on the effects of tACS for amplitude change, 
frequency change, and phase change.

Second figure indicates out-of-phase and in-phase sine waves

Third figure used to demonstrate ampltitude modulated cross-frequency coupling
of theta and gamma signals at 6Hz and 40Hz respectively.

Each figure is saved as a separate PNG file: Figure Output, Phase, AM


v2. Updated to turn the amplitude and settings into functions 
and avoid repetition.
"""

#Figure making notes
#matplotlib.pyplot.subplots_adjust

#Tunes the subplot layout.

#The parameter meanings (and suggested defaults) are:

#left = 0.125  # the left side of the subplots of the figure
#right = 0.9   # the right side of the subplots of the figure
#bottom = 0.1  # the bottom of the subplots of the figure
#top = 0.9     # the top of the subplots of the figure
#wspace = 0.2  # the amount of width reserved for space between subplots,
              # expressed as a fraction of the average axis width
#hspace = 0.2  # the amount of height reserved for space between subplots,
              # expressed as a fraction of the average axis height

### AMPLITUDE

#PLOTS AREN'T BEING STACKED> USE THIS LINL: https://matplotlib.org/devdocs/gallery/subplots_axes_and_figures/subplots_demo.html
import numpy as np
import matplotlib.pyplot as plt

#fig, ax = plt.subplots()
#Make a figure with a 2x2 grid layout of axes objects.
fig1, axs = plt.subplots (2,2)

#Adds a height reserved between each subplots.
fig1.subplots_adjust(hspace = 0.3)

#Generates a range of values from 0 to 1 with an interval of 0.01
#Tweak this to create 1 second of data, or 2 seconds etc.
t = np.arange(0.0, 1.0, 0.01)
t2 = np.arange(1.0, 2.0, 0.01)

# Function to calculate amplitude over time. Enter mV as an integer or floating
# point, and enter time as a numpy array. Array is a period of second(s) in
# intervals of 0.01 seconds [10 ms]

def amp(mV, time):
    amplitude = (mV * np.sin(2* np.pi * 4 *time))
    return amplitude


# Function to create values over time based on inputted frequency and amplitude
# Input of amplitude in mV, frequency in hertz, and time as numpy array.

def frequency(mV, hertz, time):
    frequency_array = (mV * np.sin(2*np.pi*hertz*time))
    return frequency_array


amp1 = amp(1, t)
amp2 = amp(2, t2)

freq1 = frequency(1, 4, t)
freq2 = frequency(1, 6, t2)

#Create an overall figure title, or super title => suptitle
#The y coordinate given places it up above the axes a bit so the title doesn't
#overlap with the plot titles

fig1.suptitle('Effects of tACS', y = 0.98)


#For a 2x2 box. The coords are:
# 0,0    0,1
# 1,0    1,1
axs[0,0].plot(t, amp1)
axs[0,0].plot(t2,amp2)
axs[0,0].set_title('A', fontweight = 'bold', x = 0.1)

axs[1,0].plot(t,freq1)
axs[1,0].plot(t2,freq2)

axs[1,0].set_title('B', fontweight = 'bold', x = 0.1)
axs[1,0].set_ylim(-1,2)

axs[1,0].annotate('4 Hz', xy=(0.1,1.5), fontsize=12)
axs[1,0].annotate('6 Hz', xy=(1.25,1.5), fontsize = 12)

#Get rid of the top right plot so we can put in a legend that's not way
# off the figure.
fig1.delaxes(axs[0,1])

#This is a small loop. For ax in axs.flat means to go over all objects in axs.flat.
#Axs are our subplots. the .flat turns a matrix/grid style bit of information into a flat string
#of values, i.e. [1,2,3,4]

for ax in axs.flat:
    ax.set(xlabel='time (sec)', ylabel='Amplitude (mV)')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()


for ax in axs.flat:
    ax.axvline(x=1,ymin=0, ymax=1, linestyle='dashdot', color='r', label='Onset of tACS')

#axs[0,0].axvline(x=0.5,ymin=0, ymax=1, linestyle='dashdot', color='r', label='Onset of tACS')

#axs[1,0].axvline(x=1.0,ymin=0, ymax=1, linestyle='dashdot', color='r', label='Onset of tACS')

#axs[1,1].axvline(x=1.0,ymin=0, ymax=1, linestyle='dashdot', color='r', label='Onset of tACS')
 
axs[0,1].axis('off')

#GIVE A LEGEND FOR THE DASHED RED LINE
#labels = ['Onset of tACS']
#Handles,labels grabs the information from the ax object.
handles, labels = ax.get_legend_handles_labels()

fig1.legend(handles, labels, loc =(0.57,0.8))

#Synchronisation shift plot

wave1 = (1*np.sin(2*np.pi*4*t))

wave2 = (1*np.sin(2*np.pi*4*t+np.pi/2))

wave3 = (1*np.sin(2*np.pi*4*t2))

wave4 = (1*np.sin(2*np.pi*4*t2))

axs[1,1].plot(t,wave1)
axs[1,1].plot(t,wave2)
axs[1,1].set_title('C', fontweight = 'bold', x = 0.1)
axs[1,1].plot(t2,wave3,'blue',alpha=1)
axs[1,1].plot(t2,wave4, 'black',':', alpha = 1)

#axs.plot

####
#xx = np.arange(1,100,1)
#yy = xx*xx
#fig2, ax = plt.subplots()
#ax.annotate('Squared baby', xy=(40,4000))
#ax.plot(xx,yy)


#Save the figure
fig1.savefig('Figure Output', dpi=300)



# Produce two subplots to demonstrate two out of phases theta waves at 4 Hz
# and then when perfectly in-phase. In-phase is reduced to 0.9 Mv so that
# the two signals are not overlapping.

phase1 = (1*np.sin(2*np.pi*4*t))

# Horizontal phase shift of 8. Vertical phase shifts would be outside the 
# brackets
phase2 = (1*np.sin(2*np.pi*4*t+8))

in_phase = (0.9*np.sin(2*np.pi*4*t))

fig, (ax1,ax2) = plt.subplots(2,1)

ax1.plot(t,phase1)
ax1.plot(t,phase2)
ax2.plot(t,phase1)
ax2.plot(t,in_phase)
plt.xlabel('time (sec)')
plt.ylabel('Amplitude (mV)')

fig.savefig('Phase',dpi=300)


# Figure to show cross-frequency coupling between theta and gamme frequency
# Coordinates a 6 hertz theta wave with a 40 hertz gamma wave
# Amplitude modulated, whereby gamma amplitude decreases when at the trough
# of the theta wave.

fig2, ax2 = plt.subplots()

mod_index = 0.8
t2 = np.linspace (0, 1, 500)
theta_signal = 1*np.cos(2*np.pi*6*t2)
gamma_signal = 0.5*np.cos(2*np.pi*40*t2)
am_gamma = 0.5*(1+mod_index*np.cos(2*np.pi*6*t2))*np.cos(2*np.pi*40*t2)
#gamma_frequency = (0.7*np.sin(2*np.pi*40*t2)) + (0.5*np.sin(2*np.pi*(40+6)*t2)) + (np.sin(2*np.pi*(60-6)*t2))


ax2.plot(t2,theta_signal)
ax2.plot(t2,am_gamma)

fig2.savefig('AM',dpi=300)