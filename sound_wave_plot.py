import librosa
import librosa.display
import matplotlib.pyplot as plt

a, sr = librosa.load('sample.wav')
librosa.display.waveplot(a, sr=sr)


#Giving a title
plt.title("sample.wav", style = "italic", fontweight = "bold", color = "black", fontsize = 20)
#Giving a label
plt.xlabel("time", color = "black", fontsize = 15)
plt.ylabel("A", color = "black", fontsize = 15)
#Adjusting a scale width
#plt.xlim( , )
plt.ylim(-0.6, 0.6)
#Giving squares
#plt.grid()
#Giving detail squares
#plt.minorticks_on()

#Displaying a Graph
plt.show()