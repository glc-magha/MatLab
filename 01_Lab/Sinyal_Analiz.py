"""1. Temel Sinyal Oluşturma
Fs = 1000;             % Örnekleme frekansı (Hz)
t = 0:1/Fs:1-1/Fs;     % Zaman vektörü (1 saniyelik)
f = 10;                % Frekans (Hz)
x = sin(2*pi*f*t);     % 10 Hz'lik sinüs sinyali
plot(t, x);
title('10 Hz Sinüs Sinyali');
xlabel('Zaman (s)');
ylabel('Genlik');

 2. Fourier Dönüşümü (FFT ile Frekans Analizi)
X = fft(x);
n = length(x);
f = (0:n-1)*(Fs/n);       % Frekans vektörü
mag = abs(X)/n;           % Genlik spektrumu
plot(f, mag);
title('Frekans Spektrumu');
xlabel('Frekans (Hz)');
ylabel('Genlik');
xlim([0 50]);             % İlk 50 Hz'e bak

 3. Birden Fazla Frekans İçeren Sinyal
x = sin(2*pi*10*t) + 0.5*sin(2*pi*40*t);  % 10 Hz ve 40 Hz
plot(t, x);
title('Karma Sinyal');

 4. Low-Pass Filtreleme (Düşük geçiren filtre)
fc = 20;  % Kesim frekansı
[b,a] = butter(4, fc/(Fs/2));         % 4. dereceden Butterworth filtresi
y = filter(b, a, x);                  % Filtre uygula
plot(t, y);
title('Filtrelenmiş Sinyal (Low-pass)');

5. Zaman-Frekans Analizi – Spectrogram
spectrogram(x, 128, 120, 128, Fs, 'yaxis');
title('Spectrogram');

 6. Sinyalin Güç Spektral Yoğunluğu (PSD)
pwelch(x, [], [], [], Fs);
title('Güç Spektral Yoğunluğu');

 7. Sinyal Düzeyinde Gürültü Ekleme
x_noisy = x + 0.5*randn(size(x));    % Beyaz gürültü ekle
plot(t, x_noisy);
title('Gürültülü Sinyal');

8. Sinyal Karakteristikleri (RMS, Tepe Değer, Ortalama)
rms_val = rms(x);
peak_val = max(abs(x));
mean_val = mean(x);
disp(['RMS: ' num2str(rms_val) ', Peak: ' num2str(peak_val) ', Mean: ' num2str(mean_val)]);

 9. Zaman Gecikmesi Hesabı (Cross-correlation)

x1 = sin(2*pi*10*t);
x2 = [zeros(1,50), x1(1:end-50)];
[c, lags] = xcorr(x1, x2);
[~, idx] = max(c);
time_delay = lags(idx)/Fs;
disp(['Zaman Gecikmesi: ' num2str(time_delay) ' saniye']);


 10. Sinyal Veri Dosyasından Okuma (örneğin .wav dosyası)
[y, Fs] = audioread('ornek.wav');
plot((1:length(y))/Fs, y);
title('Ses Dosyası Sinyali');
xlabel('Zaman (s)');
ylabel('Genlik');


 11. Kare Dalga Üretimi
Fs = 1000;
t = 0:1/Fs:1-1/Fs;
x = square(2*pi*5*t);
plot(t, x);
title('Kare Dalga Sinyali (5 Hz)');

 12. Üstel Zayıflama (Düşen sinyal)
x = sin(2*pi*10*t) .* exp(-2*t);
plot(t, x);
title('Üstel Zayıflamalı Sinüs');

13. Band-pass Filtreleme
[b, a] = butter(4, [10 30]/(Fs/2), 'bandpass'); % 10-30 Hz geçiren filtre
x = sin(2*pi*5*t) + sin(2*pi*20*t) + sin(2*pi*50*t);
y = filter(b, a, x);
plot(t, y);
title('Band-pass Filtre Sonucu (10-30 Hz)');

 14. Wavelet Dönüşümü ile Sinyal Analizi
x = sin(2*pi*10*t) + randn(size(t))*0.5;
cwt(x, Fs);  % Continuous wavelet transform (zaman-frekans)
title('CWT ile Zaman-Frekans Analizi');

 15. Hilbert Dönüşümü ile Anlık Genlik & Faz

xh = hilbert(x);
amplitude = abs(xh);   % Anlık genlik
phase = angle(xh);     % Anlık faz
plot(t, amplitude);
title('Anlık Genlik (Hilbert ile)');

 16. Autocorrelation (Oto-korelasyon)
r = xcorr(x, 'coeff');
lags = -length(x)/2:length(x)/2 - 1;
plot(lags, r);
title('Oto-korelasyon');

 17. Zarf (Envelope) Tespiti
env = abs(hilbert(x));
plot(t, x, t, env);
legend('Sinyal', 'Zarf');
title('Zarf Tespiti');

 18. STFT – Short-Time Fourier Transform
stft(x, Fs, 'Window', hann(128), 'OverlapLength', 100, 'FFTLength', 256);
title('STFT – Kısa Zamanlı Fourier Dönüşümü');

 19. Sinyal Normalizasyonu
x_norm = (x - min(x)) / (max(x) - min(x));
plot(t, x_norm);
title('Normalize Edilmiş Sinyal');


 20. Kendi FIR Filtreni Tasarla ve Uygula
d = designfilt('lowpassfir', 'PassbandFrequency', 30, ...
               'StopbandFrequency', 50, 'SampleRate', Fs);
x = sin(2*pi*10*t) + sin(2*pi*60*t);
y = filter(d, x);
plot(t, y);
title('FIR Filtre ile Gürültü Giderme');"""