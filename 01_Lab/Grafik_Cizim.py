"""1. Basit 2D Grafik (Çizgi Grafik)
x = 0:0.1:10;
y = sin(x);
plot(x, y);
title('Sinüs Fonksiyonu');
xlabel('X Ekseni');
ylabel('Y Ekseni');


2. Çoklu Grafik
x = 0:0.1:10;
y1 = sin(x);
y2 = cos(x);
plot(x, y1, x, y2);
legend('Sin(x)', 'Cos(x)');

3. Scatter Grafik (Dağılım Grafiği)
x = randn(1, 100);
y = randn(1, 100);
scatter(x, y);
title('Dağılım Grafiği');

4. Histogram
data = randn(1, 1000);
histogram(data, 20);
title('Histogram');

5. Bar Grafik
x = [1, 2, 3, 4];
y = [10, 20, 30, 40];
bar(x, y);
title('Bar Grafiği');

6. Pasta Grafik (Pie Chart)
x = [1, 2, 3, 4];
labels = {'A', 'B', 'C', 'D'};
pie(x, labels);
title('Pasta Grafiği');

7. Subplot Kullanarak Çoklu Grafik
x = 0:0.1:10;
subplot(2, 2, 1);
plot(x, sin(x));
subplot(2, 2, 2);
plot(x, cos(x));
subplot(2, 2, 3);
histogram(randn(1, 1000));
subplot(2, 2, 4);
scatter(randn(1, 100), randn(1, 100));

8. 3D Grafik (Plot3)
x = linspace(-5, 5, 100);
y = linspace(-5, 5, 100);
z = sin(sqrt(x.^2 + y.^2));
plot3(x, y, z);
title('3D Grafik');

9. Mesh Grafik
[x, y] = meshgrid(-5:0.1:5, -5:0.1:5);
z = sin(sqrt(x.^2 + y.^2));
mesh(x, y, z);
title('Mesh Grafik');
10. Contour Grafik
[x, y] = meshgrid(-5:0.1:5, -5:0.1:5);
z = sin(sqrt(x.^2 + y.^2));
contour(x, y, z);
title('Contour Grafik');

11. Polar Grafik
theta = 0:0.01:2*pi;
r = abs(sin(2*theta));
polarplot(theta, r);
title('Polar Grafik');

12. Stacked Bar Grafik
x = [1, 2, 3];
y1 = [10, 20, 30];
y2 = [15, 25, 35];
bar(x, [y1', y2'], 'stacked');
title('Stacked Bar Grafik');

13. Area Grafik
x = 0:0.1:10;
y1 = sin(x);
y2 = cos(x);
area(x, [y1' y2']);
title('Area Grafik');

14. Heatmap
data = rand(10, 10);
heatmap(data);
title('Heatmap');

15. Boxplot
data = randn(100, 1);
boxplot(data);
title('Boxplot');

16. Multiple Axes Grafik
x = 0:0.1:10;
y1 = sin(x);
y2 = cos(x);
figure;
ax1 = subplot(2, 1, 1);
plot(ax1, x, y1);
ax2 = subplot(2, 1, 2);
plot(ax2, x, y2);

17. Bar Chart with Error Bars
x = [1, 2, 3];
y = [3, 5, 2];
errors = [0.5, 0.2, 0.3];
bar(x, y);
hold on;
errorbar(x, y, errors, 'k', 'LineStyle', 'none');
title('Bar Chart with Error Bars');

18. Bubble Grafik
x = randn(1, 100);
y = randn(1, 100);
z = rand(1, 100)*1000;
bubblechart(x, y, z);
title('Bubble Grafik');
19. Logaritmik Grafik
x = 1:0.1:10;
y = log(x);
semilogx(x, y);
title('Logaritmik Grafik (X Ekseni)');

20. Exponential Grafik
x = 0:0.1:5;
y = exp(x);
plot(x, y);
title('Exponential Grafik');"""