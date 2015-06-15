% [in] data: N*P doubles
% [in] k:  number of centroids
% [out] kms: K*P doubles (centroids)
function kms = kmeans_train(data, k)
    %[idx, c] = kmeans(data, k, 'start', 'uniform', 'emptyaction', 'singleton');
    %kms = c;
    kms = my_kmeans(data, k);
end


function centroids = my_kmeans(data, k)
    n = size(data, 1);
    p = size(data, 2);
    centroids = randn(k, p);
    
    iterations = 50;
    %progress.textprogressbar('  extract: ');
    for itr = 1:iterations
        %progress.textprogressbar(100*itr/iterations);

        % want z(i,j) = distance centroids(i) data(j)
        c2 = sum(centroids'.^2)';
        d2 = sum(data'.^2);
        z = centroids * data' * (-2);
        z = bsxfun(@plus, z, c2);
        z = bsxfun(@plus, z, d2);

        % update min
        new_centroids = zeros(k, p);
        cnt = zeros(k, 1);
        [vals, inds] = min(z);
        for i = 1:size(z,2)
            ind = inds(1, i);
            new_centroids(ind, :) = new_centroids(ind, :) + data(i, :);
            cnt(ind, 1) = cnt(ind, 1) + 1;
        end

        % divide
        for i = 1:k
            if cnt(i, 1) > 0
                centroids(i, :) = new_centroids(i, :) / cnt(i, 1);
            else
                centroids(i, :) = randn(1, p);
            end
        end
    end
    %progress.textprogressbar('  done');
end
