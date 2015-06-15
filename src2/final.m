function res = final(data, data_labels, test, test_labels)
    res = zeros(size(test, 1), 2);

    % want z(i,j) = sum (data(i,k) - test(j,k))^2
    d2 = sum(data'.^2)';
    t2 = sum(test'.^2);
    z = data * test' * (-2);
    z = bsxfun(@plus, z, d2);
    z = bsxfun(@plus, z, t2);

    %[vals, inds] = min(z);
    %res = inds';
    for i = 1:size(test, 1)
        best = 1e50;
        bestpos = -1;
        for j = 1:size(data, 1)
            if data_labels(j) != test_labels(i)
                continue
            end
            dis = z(j, i);
            if dis < best
                best = dis;
                bestpos = j;
            end
        end
        res(i, 1) = bestpos;
    end
    for i = 1:size(test, 1)
        best = 1e50;
        bestpos = -1;
        for j = 1:size(data, 1)
            dis = z(j, i);
            if dis < best
                best = dis;
                bestpos = j;
            end
        end
        res(i, 2) = bestpos;
    end

%    for i = 1:size(test, 1)
%        fprintf('i=%d/%d: ',i,size(test,1)); fflush(stdout);
%        best = 1e50;
%        bestpos = -1;
%        for j = 1:size(data, 1)
%            if data_labels(j) != test_labels(i)
%                continue
%            end
%            x = test(i, :);
%            y = data(j, :);
%            dis = norm(x - y);
%            if dis < best
%                best = dis;
%                bestpos = j;
%            end
%        end
%        fprintf('  %d %.4f\n',bestpos,best);
%        res(i, 1) = bestpos;
%    end
    dlmwrite('../result2/final.txt', res);
end
