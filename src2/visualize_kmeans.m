load('../data/kmeans_model.mat', 'kms');

n = size(kms, 1);
for i=1:n
    s = reshape(kms(i,:), [], 6, 3);
    mn = min(s(:));
    mx = max(s(:));
    s = (s - mn) / (mx - mn);
    s = imresize(s, 32);
    imwrite(s, ['../data/KMeans_visualize/' int2str(i) '.png'], 'PNG');

end
fprintf('See ../data/KMeans_visualize/*.png\n');
