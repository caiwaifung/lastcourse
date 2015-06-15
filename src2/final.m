function res = final(data, data_labels, test, test_labels)
    % want z(i,j) = sum (data(i,k) - test(j,k))^2
    d2 = sum(data'.^2)';
    t2 = sum(test'.^2);
    z = data * test' * (-2);
    z = bsxfun(@plus, z, d2);
    z = bsxfun(@plus, z, t2);

    % tmp(i,j) for data(i) and test(j): 0 if same label; 1 if different
    tmp = (bsxfun(@minus, data_labels, test_labels') ~= 0);
    tmp = tmp * 10 + 1;
    % set large penalty (10x) if different label
    z2 = z .* tmp; 

    res = zeros(size(test,1), 20);

    [vals, inds] = sort(z2);
    res(:, 1:10) = inds(1:10, :)';

    [vals, inds] = sort(z);
    res(:, 11:20) = inds(1:10, :)';

    %res = zeros(size(test, 1), 2);
    %[vals, inds] = min(z);
    %[vals2, inds2] = min(z2);
    %res(:, 1) = inds2';
    %res(:, 2) = inds';

    dlmwrite('../result2/final.txt', res);
end
