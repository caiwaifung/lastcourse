function kms = kmeans_train(data, k)
    [idx, c] = kmeans(data, k, 'start', 'uniform', 'emptyaction', 'singleton');
    kms = c;
end
