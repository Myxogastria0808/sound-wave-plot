import librosa
import librosa.display
import matplotlib.pyplot as plt

a, sr = librosa.load('sample.wav')
librosa.display.waveplot(a, sr=sr)


#タイトルの付与
plt.title("sample.wav", style = "italic", fontweight = "bold", color = "black", fontsize = 20)
#ラベルの付与
plt.xlabel("time", color = "black", fontsize = 15)
plt.ylabel("A", color = "black", fontsize = 15)
#目盛り幅の調整
#plt.xlim( , )
plt.ylim(-0.6, 0.6)
#目盛りのマス目表示
#plt.grid()
#より細かい目盛りの付与
#plt.minorticks_on()

#グラフの表示
plt.show()