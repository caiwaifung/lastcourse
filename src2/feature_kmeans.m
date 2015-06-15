% [in] data: {N}*M*108
% [in] kms: K*108
% [out] f:  N*K
function features = feature_kmeans(data, kms)
    features = zeros(size(data, 1), size(kms, 1));
    BATCH = 100;
    le = 1;
    progress.textprogressbar('  files: ');
    while le <= size(data, 1)
        progress.textprogressbar(100*le/size(data, 1));
        ri = min(le + BATCH, size(data, 1));
        features(le:ri, :) = extract_batch(data(le:ri, 1), kms);
        le = ri + 1;
    end
    progress.textprogressbar('  done');
end


function features = extract_batch(data, kms)
    num = 0;
    for i = 1:size(data, 1)
        num = num + size(data{i,1}, 1);
        assert(size(data{i,1}, 2) == 108);
    end
    ids = zeros(num, 1);
    patches = zeros(num, 108);
    cur = 0;
    for i = 1:size(data, 1)
        for j = 1:size(data{i,1}, 1)
            cur = cur + 1;
            ids(cur, 1) = i;
            patches(cur, :) = data{i,1}(j, :);
        end
    end

    % have patches=N*P, kms=K*P
    % want d=N*K, where d(i,j)=sum (patches(i,k)-kms(j,k))^2
    p2 = sum(patches'.^2)';
    k2 = sum(kms'.^2);
    d = patches * kms' * (-2);
    d = bsxfun(@plus, d, p2);
    d = bsxfun(@plus, d, k2);
    for i = 1:size(d,1)
        d(i,:) = d(i,:) - mean(d(i,:));
    end
    d = normr(d);
    d = max(-d, 0);

    features = zeros(size(data, 1), size(d, 2));
    for i = 1:size(d,1)
        features(ids(i, 1), :) = features(ids(i, 1), :) + d(i, :);
    end
end
