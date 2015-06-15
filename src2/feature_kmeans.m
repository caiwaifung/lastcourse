% [in] data: {N}*M*108
% [in] kms: K*108
% [out] f:  N*K
function features = feature_kmeans(data, kms)
    num = 0;
    for i = 1:size(data, 1)
        num = num + size(data{i}, 1);
        assert(size(data{i}, 2) == 108);
    end
    ids = zeros(num, 1);
    patches = zeros(num, 108);
    cur = 0;
    for i = 1:size(data, 1)
        for j = 1:size(data{i}, 1)
            cur = cur + 1;
            ids(cur, 1) = i;
            patches(cur, :) = data{i}(j, :);
        end
    end

    % have patches=N*P, kms=K*P
    % want d=N*K, where d(i,j)=sum (patches(i,k)-kms(j,k))^2
    p2 = sum(patches'.^2)';
    k2 = sum(k'.^2);
    d = patches * kms' * (-2) + p2 + k2;

    d = (d - mean(d')') ./ var(d')';
    d = max(-d, 0);

    features = zeros(size(data, 1), 108);
    for i = 1:size(d,1)
        features(ids(i, 1), :) += d(i, :);
    end
end
