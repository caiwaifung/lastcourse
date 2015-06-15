% [in] data: N*P doubles
% [in] whm: ?*? doubles (the whitening model)
% [out] res: N*P doubles (the whitened data)
function res = whitening_perform(data, model, d)
    %res = data * whm;
    if d == 1
        X = bsxfun(@minus, data, model{1});
        res = X*model{2};
    elseif d == -1
        X = data*inv(model{2});
        res = bsxfun(@plus, X, model{1});
    end
end
