function [X, Y] = read_data(fname, n, dim)
    fid = fopen(fname, 'r');
    d = fread(fid, 1, 'int');
    assert(d == dim);
%{
    X = fscanf(f, '%f', [dim + 1, n])';
    fclose(f);
    Y = X(:, 1) + 1;
    X = X(:, 2:size(X,2));
%}
    X = zeros(n, dim);
    Y = zeros(n, 1);
    for i = 1 : n
        Y(i) = fread(fid, 1, 'int') + 1;
        X(i, :) = fread(fid, dim, 'float');
    end
    fclose(fid);
    %X = [X, ones(size(X,1),1)];
end

