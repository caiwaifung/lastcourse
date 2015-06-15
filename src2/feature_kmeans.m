function features = feature_kmeans(data, kms)
    num = 0;
    for i = 1:size(data)
        num = num + size(data{i}, 1);
        assert(size(data{i}, 2) == 108);
    end
    ids = zeros(num, 1);
    patches = zeros(num, 108);
    cur = 0;
    for i = 1:size(data)
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
    features = d;
end

