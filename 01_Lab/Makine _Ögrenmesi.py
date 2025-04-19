1. Veri Kümesi Yükleme ve İnceleme
load fisheriris;  % Fisher iris veri setini yükle
disp(head(meas)); % Veri setinin ilk birkaç satırını görüntüle

2. Veri Ön İşleme (Normalizasyon)
X = meas;          % Özellikler (features)
X_norm = (X - mean(X)) ./ std(X);  % Z-sskala normalizasyonu


3. K-En Yakın Komşu (KNN) ile Sınıflandırma
Mdl = fitcknn(meas, species, 'NumNeighbors', 5);
cvMdl = crossval(Mdl);
L = kfoldLoss(cvMdl);
disp(['Kfold Loss: ', num2str(L)]);


4. Destek Vektör Makineleri (SVM) ile Sınıflandırma
Mdl = fitcsvm(meas, species, 'KernelFunction', 'linear');
cvMdl = crossval(Mdl);
L = kfoldLoss(cvMdl);
disp(['Kfold Loss: ', num2str(L)]);


5. Karar Ağaçları ile Sınıflandırma
Mdl = fitctree(meas, species);
view(Mdl, 'Mode', 'graph');  % Karar ağacını görselleştir


6. Rastgele Ormanlar (Random Forest) ile Sınıflandırma
Mdl = fitcensemble(meas, species, 'Method', 'Bag', 'NumLearningCycles', 100);
cvMdl = crossval(Mdl);
L = kfoldLoss(cvMdl);
disp(['Kfold Loss: ', num2str(L)]);


7. Lojistik Regresyon ile Sınıflandırma
Mdl = fitclinear(meas, species, 'Learner', 'logistic');
cvMdl = crossval(Mdl);
L = kfoldLoss(cvMdl);
disp(['Kfold Loss: ', num2str(L)]);


8. Naive Bayes ile Sınıflandırma
Mdl = fitcnb(meas, species);
cvMdl = crossval(Mdl);
L = kfoldLoss(cvMdl);
disp(['Kfold Loss: ', num2str(L)]);


9. Lineer Regresyon ile Tahmin
Mdl = fitlm(meas(:,1), meas(:,2));  % 1. ve 2. sütunlar arasında regresyon
disp(Mdl);


10. Kümeleme (K-Means)
[idx, C] = kmeans(meas, 3);  % 3 kümeye ayır
figure;
gscatter(meas(:,1), meas(:,2), idx);
title('K-Means Kümeleme');


11. Ana Bileşenler Analizi (PCA)
[coeff, score, latent] = pca(meas);  % PCA analizi
figure;
scatter(score(:,1), score(:,2));
title('PCA Sonuçları');

12. Zayıf Öğrenme (AdaBoost) ile Sınıflandırma
Mdl = fitcensemble(meas, species, 'Method', 'AdaBoostM1', 'NumLearningCycles', 50);
cvMdl = crossval(Mdl);
L = kfoldLoss(cvMdl);
disp(['Kfold Loss: ', num2str(L)]);

13. Özellik Seçimi (Feature Selection)
opts = statset('UseParallel', true);
[fs, history] = sequentialfs(@(X,Y)sum((X*Y').^2), meas, species, 'cv', opts);
disp(fs);

14. Derin Öğrenme (Deep Learning) - Yapay Sinir Ağı
layers = [
    featureInputLayer(4)
    fullyConnectedLayer(3)
    softmaxLayer
    classificationLayer
];
options = trainingOptions('sgdm', 'MaxEpochs', 100, 'Verbose', 0);
net = trainNetwork(meas, species, layers, options);

15. Sinir Ağı ile Regresyon
X = meas(:,1:2);  % Özellikler
Y = meas(:,3);    % Hedef
net = fitnet(10);  % 10 nöronlu bir sinir ağı
[net, tr] = train(net, X', Y');
Y_pred = net(X');

16. Doğrusal Sınıflandırıcı - LDA (Linear Discriminant Analysis)
Mdl = fitcdiscr(meas, species);
cvMdl = crossval(Mdl);
L = kfoldLoss(cvMdl);
disp(['Kfold Loss: ', num2str(L)]);

17. Görüntü Tanıma İçin Convolutional Neural Networks (CNN)
imageData = imageDatastore('path_to_images', 'LabelSource', 'foldernames');
layers = [
    imageInputLayer([28 28 1])
    convolution2dLayer(3, 8)
    reluLayer
    fullyConnectedLayer(2)
    softmaxLayer
    classificationLayer
];
options = trainingOptions('sgdm', 'MaxEpochs', 10, 'InitialLearnRate', 0.001);
net = trainNetwork(imageData, layers, options);


18. Karmaşık Modeller İçin XGBoost
X = meas;
Y = species;
model = fitcensemble(X, Y, 'Method', 'LogitBoost');


19. Veri Bölme ve Eğitim Seti
cv = cvpartition(length(species), 'HoldOut', 0.3);  % Eğitim seti %70, test %30
trainData = meas(training(cv), :);
testData = meas(test(cv), :);

20. Sürekli Veri İçin Gaussian Naive Bayes
Mdl = fitcnb(meas, species, 'Distribution', 'kernel');
cvMdl = crossval(Mdl);
L = kfoldLoss(cvMdl);
disp(['Kfold Loss: ', num2str(L)]);