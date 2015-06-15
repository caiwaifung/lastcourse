% [in] data: N*P doubles
% [out] model: the whitening model
function model = whitening_train(data)
    mu = mean(data);
    X = bsxfun(@minus, data, mu);
    A = X'*X;
    [V,D,notused] = svd(A);
    whMat = sqrt(size(X,1)-1)*V*sqrtm(inv(D + eye(size(D))*1e-6))*V';
    invMat = pinv(whMat);
    model={mu,whMat,invMat};
end
