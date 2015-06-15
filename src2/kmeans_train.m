function kms = kmeans_train(data, k)
    [idx, c] = kmeans(data, k, 'emptyaction', 'singleton', 'MaxIter', 1000);
    kms = c;
end
